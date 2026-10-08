# WilhasonOceanMaster V1.0

海洋水面系统数字孪生平台 · A Physics-Based Digital Twin for Marine Surface Systems

由华南理工大学 NOF 创新创业团队、海洋科学与工程学院出品并持续维护。
Produced and continuously maintained by the NOF Innovation & Entrepreneurship Team and the School of Marine Science and Engineering, South China University of Technology.

## 目录结构 / Repository Structure

| 目录 | 内容 |
| --- | --- |
| `digital_twin/` | 数字孪生环境包：可运行仿真程序 V1（Windows x64），见其 [README](digital_twin/README.md) / Digital twin environment: runnable simulation package V1 |
| `LandStation/` | 精简版地面站源码包 LandStation-Lite v1.0.0（GPL-3.0），见其 [README](LandStation/README.md) / Ground station source release |
| `docs/` | 通信协议等文档（Communication protocol & docs） |
| `parameters/` | 完整动力学参数（Complete hydrodynamic parameters） |
| `usv/` | 对应真实 USV 资料（Real USV materials） |

## 开源协议 / License

仓库骨架采用 **MIT License**，完整条款见 [LICENSE](LICENSE)。
The repository skeleton is released under the MIT License (see [LICENSE](LICENSE)).

各发布包**自带独立许可**，以包内 `LICENSE` 为准：

- `LandStation/` 地面站源码包：**GPL-3.0**（依赖 PyQt5 的 GPL 授权，详见其 [README](LandStation/README.md)）
- `digital_twin/` 数字孪生环境包：见包内说明

Each release package carries its own license; see the `LICENSE` file inside each package.

## 引用 / Citation

若本平台支撑了您的研究，请在论文中引用本项目。
If this platform supports your research, please cite this project in your publications.
