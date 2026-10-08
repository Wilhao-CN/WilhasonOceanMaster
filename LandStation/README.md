# 精简版地面站 · LandStation-Lite v1.0.0（源码发布包）

> Ground Station for USV Twin-Vessel Cooperative Control — LandStation-Lite v1.0.0 Source Release
>
> **版本**：v1.0.0 · **发布日期**：2026-10-08 · **平台**：Windows 10/11 x64 · **许可**：GPL-3.0
> **包文件**：`LandStation-Lite-v1.0.0-src.zip`（17 MB · 122 个文件 · SHA256 `4a8e31713f1bf613f79d79b5b5a729aeb487b3048b7c9bc8ebb8af49d1a2d378`）

双无人船（USV + 浮船坞）协同控制地面站的**精简版源码发布包**，含完整源码、预置配置与随包文档。
A source release of the lightweight ground station for dual-USV cooperative control, with full source code, preset configuration and bundled documentation.

## 包内清单 / Contents

| 路径 | 说明 |
| --- | --- |
| `README.md` | 项目总览、功能特性、FAQ（开源发布版措辞）/ Project overview & FAQ |
| `环境配置说明.md` | **环境搭建权威文档**（Python 3.10 / 依赖 / 常见问题）/ Environment setup guide |
| `start_groundstation.bat` | 一键启动脚本 / One-click launcher |
| `run_start_with_log.bat` | 带日志启动（排障用）/ Launcher with log output |
| `requirements.txt` / `requirements-optional.txt` | 必需依赖 / 可选依赖（YOLOv8 目标检测） |
| `main.py` · `_version.py` | 程序入口与版本元信息 / Entry point & version metadata |
| `LICENSE` · `THIRD_PARTY_NOTICES.md` | **GPL-3.0 全文** / 第三方组件许可与致谢 |
| `missions.json` | 预置演示任务（**形状保真演示版**，非真实坐标）/ Demo missions |
| `config/` | 手柄映射、模拟器等预置配置（隐私脱敏版）/ Preset configs (sanitized) |
| `core/` `ui/` `vision/` `Tools/` `docs/` | 协议与控制链 / 界面 / 视觉 / 工具与验收脚本 / 联调文档 |

## 获取与运行 / Run

1. 下载 `LandStation-Lite-v1.0.0-src.zip` 并解压到**纯 ASCII 路径**（例如 `D:\LandStation-Lite`；
   中文路径会导致 QtWebEngine 资源加载失败，表现为双击无反应）
2. 准备环境：`py -3.10 -m venv venv_usv`
3. 安装依赖：`venv_usv\Scripts\python.exe -m pip install -r requirements.txt`
4. 自检（可选但推荐）：`venv_usv\Scripts\python.exe Tools\check_env.py`
5. 启动：双击 `start_groundstation.bat`（排障时用 `run_start_with_log.bat` 看日志）

> 需要 YOLOv8 目标检测时另装：`pip install -r requirements-optional.txt`
>（自训权重 `best.pt` / `boat_NOF.pt` 已随包；Ultralytics 框架本身为 AGPL-3.0，见 `THIRD_PARTY_NOTICES.md`）

## 与数字孪生环境联调 / Joint Integration

- 配套的 Unity 数字孪生仿真环境见 [`../digital_twin/`](../digital_twin/README.md)
- 端口、帧格式与联调口径以包内 `docs/联调_数字孪生V1_M5口径与验收.md` 及
  `digital_twin/Build_GCS_Compatible/GROUND_STATION_INTERFACE.md` 为准
- 联调回归 **12/12 通过**（2026-10-08）

## 状态 / Status

- 验收全绿（2026-10-08）：控制链 30 项 · 协议基线 121 项 0 差异 · 数字孪生 6 组 · UI 断言 · 环境自检 · WebEngine 资源
- 发布门禁：隐私脱敏与悬空引用扫描 **0 告警**（由 `Tools/package_release.py` 四道关卡强制执行）
- 本仓库仅发布打包产物；开发源码仓与内部调试资料**不对外**

## 许可 / License

- 本包以 **GPL-3.0** 发布，完整条款见包内 `LICENSE`；第三方组件许可见包内 `THIRD_PARTY_NOTICES.md`
- 选择 GPL-3.0 的原因：依赖 PyQt5 / PyQtWebEngine（GPL v3 与商业双授权），详见包内 `README.md` 许可节
