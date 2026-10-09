#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
孪生关卡配置读取（T4）
======================

读取 `ui/map/twin_maps/scenes.json`，为地面站的「🌐 孪生底图」菜单
与 E2 范围校验提供关卡元数据（四角经纬度、可航半径、形状等）。

设计说明
--------
* **必须由 Python 读取，不能用 JS `fetch`** ——
  `file://` 页面下 QtWebEngine 会拦截 `fetch`，且本工程未开
  `LocalContentCanAccessFileUrls`。故读好后把四角**作为参数**传给
  `runJavaScript`（见 `showTwinMap(...)`）。
* 配置缺失/损坏时**不抛异常**，只记日志并回退到"无孪生关卡"，
  以保证**实船路径完全不受影响**。
* 纯新增模块，不修改任何既有行为。
"""

import json
import os

# 💡 打包(frozen)适配：定位 scenes.json 统一走 app_paths.resolve()
#    开发态 = 工程根/ui/map/twin_maps/scenes.json（与原先行为一致）
#    打包后 = 优先 exe 旁边的同名文件（换关卡不用重新打包），
#             否则回退到随包内置副本
import app_paths

# 兜底：Unity 未提供 navigableRadiusMeters 时，按"半边长 − 1 m"估算。
# 依据：边界几何体通常有约 2 m 厚度，内表面即半边长 − 1。
_FALLBACK_MARGIN_M = 1.0


class TwinSceneConfig:
    """孪生关卡配置。`levels` 为 `{scene_name: dict}`。"""

    def __init__(self, path: str = None):
        if path is None:
            path = app_paths.resolve("ui", "map", "twin_maps", "scenes.json")
        self.path = path
        self.levels = {}
        self.error = None
        self._load()

    # ---------------------------------------------------------------- 载入

    def _load(self) -> None:
        if not os.path.isfile(self.path):
            self.error = f"未找到关卡配置: {self.path}"
            print(f"[TwinMap] {self.error}")
            return
        try:
            with open(self.path, "r", encoding="utf-8") as fh:
                payload = json.load(fh)
        except (OSError, ValueError) as exc:
            self.error = f"读取关卡配置失败: {exc}"
            print(f"[TwinMap] {self.error}")
            return

        for lv in payload.get("levels", []) or []:
            scene = lv.get("scene")
            if not scene:
                continue
            if not self._is_usable(lv):
                print(f"[TwinMap] 跳过关卡 {scene}: 四角字段不完整")
                continue
            self.levels[scene] = lv

        if not self.levels:
            self.error = "关卡配置中无可用条目"
            print(f"[TwinMap] {self.error}")
        else:
            print(f"[TwinMap] 已载入 {len(self.levels)} 个关卡: "
                  f"{', '.join(self.levels.keys())}")

    @staticmethod
    def _is_usable(lv: dict) -> bool:
        """四角齐全且非退化，才可用（否则位置会算错）。"""
        need = ("topLat", "bottomLat", "leftLon", "rightLon")
        if not all(k in lv for k in need):
            return False
        try:
            top, bottom = float(lv["topLat"]), float(lv["bottomLat"])
            left, right = float(lv["leftLon"]), float(lv["rightLon"])
        except (TypeError, ValueError):
            return False
        return top > bottom and right > left

    # ---------------------------------------------------------------- 查询

    def get(self, scene: str):
        """取某关卡的配置 dict；不存在返回 None。"""
        return self.levels.get(scene)

    def names(self):
        """关卡名列表（保持 JSON 中的顺序）。"""
        return list(self.levels.keys())

    def available(self) -> bool:
        return bool(self.levels)

    # ------------------------------------------------------- 供 JS 的参数

    def bounds_for_js(self, scene: str):
        """返回可安全交给 runJavaScript 的四角 dict（只含数值）。"""
        lv = self.get(scene)
        if not lv:
            return None
        return {k: float(lv[k]) for k in
                ("topLat", "bottomLat", "leftLon", "rightLon")}

    def image_for(self, scene: str):
        lv = self.get(scene)
        return (lv or {}).get("image")

    def image_px(self, scene: str) -> int:
        """底图边长（像素）；缺失按 1024。"""
        lv = self.get(scene) or {}
        try:
            w = int(lv.get("width") or 1024)
            h = int(lv.get("height") or w)
            return max(w, h)
        except (TypeError, ValueError):
            return 1024

    def navigable_radius(self, scene: str):
        """可航半径（米）。缺失时按半边长 −1 估算；再不行返回 None。"""
        lv = self.get(scene)
        if not lv:
            return None
        r = lv.get("navigableRadiusMeters")
        if r is not None:
            try:
                r = float(r)
                if r > 0:
                    return r
            except (TypeError, ValueError):
                pass
        # 回退：半边长 − 1 m
        ext = lv.get("sceneExtentMeters")
        try:
            if ext is not None:
                half = float(ext) / 2.0
                if half > _FALLBACK_MARGIN_M:
                    return half - _FALLBACK_MARGIN_M
        except (TypeError, ValueError):
            pass
        # 再回退：由纬度跨度推（1° ≈ 111320 m）
        try:
            half = (float(lv["topLat"]) - float(lv["bottomLat"])) * 111320.0 / 2.0
            if half > _FALLBACK_MARGIN_M:
                return half - _FALLBACK_MARGIN_M
        except (KeyError, TypeError, ValueError):
            pass
        return None

    def bounds_shape(self, scene: str) -> str:
        """边界形状：'circle'（圆形判据）或 'square'（默认，向后兼容）。

        L1 是圆形湖（方图四角是陆地）→ 'circle'
        L2 是方形墙 → 'square'
        """
        lv = self.get(scene) or {}
        shape = str(lv.get("boundsShape") or "square").strip().lower()
        return shape if shape in ("circle", "square") else "square"

    def origin(self, scene: str):
        """圆心/原点 (lat, lon)；缺失时用四角中心兜底。"""
        lv = self.get(scene)
        if not lv:
            return None
        try:
            return float(lv["originLat"]), float(lv["originLon"])
        except (KeyError, TypeError, ValueError):
            try:
                return ((float(lv["topLat"]) + float(lv["bottomLat"])) / 2.0,
                        (float(lv["leftLon"]) + float(lv["rightLon"])) / 2.0)
            except (KeyError, TypeError, ValueError):
                return None

    def describe(self, scene: str) -> str:
        """状态栏用的一句话描述。"""
        lv = self.get(scene)
        if not lv:
            return scene
        shape = self.bounds_shape(scene)
        r = self.navigable_radius(scene)
        unit = "半径" if shape == "circle" else "半边长"
        if r is None:
            return scene
        return f"{scene}（{unit} {r:g} m）"
