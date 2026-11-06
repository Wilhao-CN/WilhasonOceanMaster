# WilhasonOceanMaster V1.0.1

海洋水面系统数字孪生平台 · A Physics-Based Digital Twin for Marine Surface Systems

由华南理工大学 NOF 创新创业团队、海洋科学与工程学院出品并持续维护。
Produced and continuously maintained by the NOF Innovation & Entrepreneurship Team and the School of Marine Science and Engineering, South China University of Technology.

## 目录结构 / Repository Structure

| 目录 | 内容 | 许可证 |
| --- | --- | --- |
| `digital_twin/` | 数字孪生环境包：可运行仿真程序 V1（Windows x64） | Apache-2.0 |
| `LandStation/` | 精简版地面站运行版 v1.0.1 | GPL-3.0 |
| `LandStation-Lite-v1.0.1-src.zip` | 地面站完整源代码压缩包 | GPL-3.0 |
| `docs/` | 通信协议、安全说明（[`SAFETY.md`](docs/SAFETY.md)）等文档 | 随根仓库 MIT（除非文件内另有声明） |
| `parameters/` | 完整动力学参数 | 随根仓库 MIT（除非文件内另有声明） |
| `usv/` | 对应真实 USV 资料 | 随根仓库 MIT（除非文件内另有声明） |

## 安全 / Safety

> 🔴 **接真实硬件前必读**：[`docs/SAFETY.md`](docs/SAFETY.md)

本仓库包含一套可驱动**真实推进器、舵机与继电器**的地面站。代码中已实现的安全机制
（免责门禁、手动安全锁、软件急停、推力限幅、上行帧校验）与**尚未实现**的保护
（失联自动停船、指令超时、下行 ACK、硬件级遥控接管）在 [`docs/SAFETY.md`](docs/SAFETY.md) 中
逐条列出，并给出对应的处置建议与部署待办。

地面站**不负责**通信失联后的兜底——该保护必须由 MCU 固件实现。下水前请确认这一点，
并务必在实船上保留一套独立于软件的物理断电开关。

Before connecting to real hardware, read [`docs/SAFETY.md`](docs/SAFETY.md). Several failsafe
mechanisms are **not** implemented on the ground-station side.

## 流量统计 / Traffic

![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FWilhao-CN%2FWilhasonOceanMaster%2Fmain%2Ftraffic-data%2Ftraffic-summary.json&query=%24.message&label=traffic&color=blue)

> 数据由 GitHub Actions 每日自动抓取并更新至 [`traffic-data/`](traffic-data/)（clones 与 views 按日期去重累积）。
> Data is collected daily by GitHub Actions and archived in `traffic-data/`.

## 开源协议 / License

本仓库为**多许可证仓库**，各目录/发布包相互独立，以对应目录内的 `LICENSE` 为准。

| 范围 | 许可证 | 说明 |
|---|---|---|
| 根目录文档、配置文件、仓库骨架 | **MIT** | 仅适用于非 `digital_twin/`、非 `LandStation/` 的仓库级文件；全文见根目录 [`LICENSE`](LICENSE) |
| `digital_twin/` 数字孪生环境包 | **Apache License 2.0** | 以 `digital_twin/LICENSE` 为准；第三方组件见包内 `THIRD_PARTY_NOTICES.md` |
| `LandStation/` 地面站运行版 | **GNU GPL v3** | 以 `LandStation/LICENSE` 为准；完整源代码见仓库根目录 `LandStation-Lite-v1.0.1-src.zip` |
| `LandStation-Lite-v1.0.1-src.zip` 地面站源码包 | **GNU GPL v3** | 公开下载、无前置条件；以压缩包内 `LICENSE` 为准 |

> **边界声明**：根目录 MIT 许可证**不覆盖** `digital_twin/` 与 `LandStation/`。使用 `LandStation/` 中任何内容即受 GPL-3.0 约束；使用 `digital_twin/` 中任何内容受 Apache-2.0 约束。各子目录许可证不可混用。

Each directory/package carries its own license. The root MIT license **does not** cover `digital_twin/` or `LandStation/`.

## 从源码构建 / Building from source

地面站源码包内含完整构建说明（PyInstaller 重建 `.spec`、`build_exe.bat` 自检、依赖与环境要求），见
`LandStation-Lite-v1.0.1-src.zip` 中的 `BUILD.md`。
The source archive contains full build instructions (`BUILD.md`): PyInstaller `.spec`, `build_exe.bat`, dependencies, and environment requirements.

## 参与贡献 / Contributing

欢迎提交 Issue 与 Pull Request。请按修改目标目录遵守对应许可证：

- 根目录骨架/文档：**MIT**
- `digital_twin/`：**Apache-2.0**
- `LandStation/` 及源码包：**GPL-3.0**

提交 PR 时请注明目标目录。向 `LandStation/` 提交的贡献按 **GPL-3.0** 授权；向 `digital_twin/` 提交的贡献按 **Apache-2.0** 授权。品牌与商标保护范围见源码包内 `TRADEMARK.md`。

Issues and pull requests are welcome. Contributions are licensed under the license of the target directory.

## 引用 / Citation

若本平台支撑了您的研究，请在论文中引用本项目。
If this platform supports your research, please cite this project in your publications.
