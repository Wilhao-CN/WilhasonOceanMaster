# 数字孪生仿真环境 · V1 / Digital Twin Simulation Environment · V1

> Unmanned Surface Vehicle (USV) Digital Twin — Unity Simulation Environment
>
> **版本**：V1 · **构建日期**：2026-10-30 · **发布**：2026-10-31 · **平台**：Windows 10/11 x64
> **产品名**：`USV_Sim2Real_Simulation_Platform`（公司：`SCUT_NOF`）

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
| `Build_GCS_Compatible/gcs_target_ip.txt` | 地面站目标 IP（默认 `127.0.0.1`）/ Ground station target IP |
| `Build_GCS_Compatible/THIRD_PARTY_NOTICES.md` | **第三方组件声明与许可全文** / Third-party notices & license texts |
| `Build_GCS_Compatible/LICENSE-APACHE.txt` | Apache License 2.0 全文 / Full text of Apache 2.0 |
| `Build_GCS_Compatible/dt_params.json` | 运行参数存档（仅保存非默认项；首次运行不生成，修改并保存参数后自动出现）/ Runtime parameters (non-defaults only) |
| `Build_GCS_Compatible/ParamsExport/` | 参数导出快照（点击「导出」后自动创建）/ Parameter export snapshots (created on export) |
| `LICENSE` | Apache License 2.0 全文 / Full text of Apache 2.0 |
| `LICENSE-APACHE.txt` | Apache License 2.0 全文副本（保留兼容）/ Apache 2.0 full text copy |
| `THIRD_PARTY_NOTICES.md` | 第三方组件声明与许可全文 / Third-party notices & license texts |
| `NOTICE` | Apache-2.0 NOTICE 文件/ Apache NOTICE file |
| ` Build_GCS_Compatible/UnityPlayer.dll 及相关引擎组件 `| Unity 引擎运行时组件 / Unity engine runtime components |

## 运行 / Run

1. 解压发布包到任意路径（路径建议不含中文或空格）。
2. 进入 `Build_GCS_Compatible/` 目录。
3. 双击 `USV_Sim2Real_Simulation_Platform.exe` 启动。
4. 首次运行若被 Windows SmartScreen 拦截：「更多信息 → 仍要运行」。
5. 与地面站联机时，先编辑 `gcs_target_ip.txt` 指向地面站 IP；接口约定见包内 `GROUND_STATION_INTERFACE.md`。

## 安全 / Safety

数字孪生环境本身**不下达任何真实硬件指令**，是安全的试验场——这正是它存在的意义：
先在孪生里把算法、PID 参数与任务流程跑通，再考虑接实船。

> 但请注意：**孪生调通 ≠ 实船调通**。力映射曲线可调，窗口顶部有常驻红字警告
> 「修改力映射后，孪生将不再代表真船」。接真实船体前，请先读
> [`docs/SAFETY.md`](../docs/SAFETY.md)，尤其 §5 的 L1→L2→L3 递进测试流程。

The digital twin never commands real hardware. Passing in simulation does **not**
guarantee safe real-vessel behaviour — read [`docs/SAFETY.md`](../docs/SAFETY.md) first.

## 许可 / License

- **项目自有代码**：**Apache License 2.0**，全文见本目录 `LICENSE`。
- **第三方组件**：Crest Ocean Framework（MIT）、IronPython（Apache-2.0）、Newtonsoft.Json（MIT）等，详见本目录 `THIRD_PARTY_NOTICES.md`。Apache License 2.0 全文亦见 `LICENSE-APACHE.txt`。
- **发布形式**：本发布包为**纯二进制发布物**，不含 Unity 工程源码。
- 使用本包即受 Apache-2.0 约束；本包许可证与仓库根目录 MIT、`LandStation/` 的 GPL-3.0 **相互独立**。

## 状态 / Status

- 详细内容与验收记录见包内 `README_V1.md`。