# 数字孪生仿真环境 · V1 / Digital Twin Simulation Environment · V1

> Unmanned Surface Vehicle (USV) Digital Twin — Unity Simulation Environment
>
> **版本**：V1 · **构建日期**：2026-10-07 · **发布**：2026-10-08 · **平台**：Windows 10/11 x64
> **产品名**：`USV_Sim2Real_Simulation_Platform`（公司：`SCUT_NOE`）

可直接运行的无人船（USV）数字孪生仿真程序，含完整的运行时与随包文档。
A ready-to-run USV digital twin simulation program with full runtime and bundled documentation.

## 目录 / Contents

| 路径 | 说明 |
| --- | --- |
| `Build_GCS_Compatible/USV_Sim2Real_Simulation_Platform.exe` | 主程序入口（Windows x64）/ Main executable |
| `Build_GCS_Compatible/USV_Sim2Real_Simulation_Platform_Data/` | 资源与托管程序集 / Assets & managed assemblies |
| `Build_GCS_Compatible/README_V1.md` | **V1 版本说明与使用指南**（先读这份）/ V1 release notes & user guide |
| `Build_GCS_Compatible/JOINT_README.md` | 数字孪生 ↔ 地面站对接必读（十条条目权威落点）/ Joint integration guide |
| `Build_GCS_Compatible/GROUND_STATION_INTERFACE.md` | **端口 / 帧格式 / 协议权威定义** / Ground station interface spec |
| `Build_GCS_Compatible/README.md` | V0.5 超前预览版说明（历史参考）/ Legacy V0.5 notes |
| `Build_GCS_Compatible/gcs_target_ip.txt` | 地面站目标 IP（默认 `127.0.0.1`）/ Ground station target IP |
| `Build_GCS_Compatible/dt_params.json` | 运行参数存档（仅保存非默认项）/ Runtime parameters (non-defaults only) |
| `Build_GCS_Compatible/ParamsExport/` | 参数导出快照 / Parameter export snapshots |

## 运行 / Run

1. 进入 `digital_twin/Build_GCS_Compatible/`
2. 双击 `USV_Sim2Real_Simulation_Platform.exe`
3. 首次运行若被 Windows SmartScreen 拦截：「更多信息 → 仍要运行」
4. 与地面站联机时，先编辑 `gcs_target_ip.txt` 指向地面站 IP；接口约定见包内 `GROUND_STATION_INTERFACE.md`

## 状态 / Status

- V1 已完成 M0–M5 全部里程碑（依赖裁剪、参数窗口、精简定位、打包与验收）
- 与精简版地面站联调回归 **12/12 通过**（2026-10-08）
- 详细变更与验收记录见包内 `README_V1.md`

## 占位目录 / Placeholders

本仓库根目录的 `docs/`、`parameters/`、`usv/` 仍为占位，按根 README 约定后续填充。
The root-level `docs/`, `parameters/` and `usv/` directories remain placeholders for future content.
