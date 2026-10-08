# LandStation-Lite v1.0.0 · 地面站运行版

**精简版无人船地面站 —— 免安装可运行程序（Windows x64）**
Ground Station Runtime Package — no Python, no setup required.

> 这是**已经打包好的程序**，不需要安装 Python，也不需要配置任何环境。
> 完整使用说明见同目录的 **`使用说明.txt`**（先看这个）。

---

## 三步跑起来

1. 把**整个文件夹**复制到一个**纯英文（ASCII）路径**下，例如 `D:\LandStation-Lite\`
2. 双击 `LandStation-Lite.exe`
3. 阅读弹出的「免责声明与使用许可」，勾选后点「我已阅读并同意」（点「不同意并退出」则程序关闭）

> ⚠️ **不要只拷 `LandStation-Lite.exe` 单个文件。**
> 同级的 `_internal/` 目录是程序运行必需的（Qt、OpenCV、Python 运行时都在里面），
> 实测只拷 exe 会立刻退出、连窗口都不会出现。必须整个文件夹一起复制。
>
> ⚠️ **路径含中文会跑不起来**（QtWebEngine 的已知限制，会闪退或地图空白）。
> 详见 `使用说明.txt` 第二节。

---

## 本目录里都是什么

| 文件 / 目录 | 说明 |
| --- | --- |
| `LandStation-Lite.exe` | **主程序**，双击启动 |
| `使用说明.txt` | **面向使用者的完整说明书**（怎么跑、路径要求、系统要求、日志、常见问题） |
| `_internal/` | 程序运行必需的运行时与依赖库，**不要删、不要改** |
| `config/` | 预置配置（手柄映射 `joystick_mapping.json`、孪生路径 `simulator.json`） |
| `missions.json` | 预置演示任务（形状保真演示版，非真实坐标） |
| `LICENSE` · `THIRD_PARTY_NOTICES.md` | GPL-3.0 全文 / 第三方组件许可与致谢 |
| `环境配置说明-源码工程.md` | ⚠️ **源码工程**的环境搭建文档，**与运行本程序无关** |
| `README-源码工程.md` | ⚠️ **源码工程**的项目说明，**与运行本程序无关** |
| `docs/` | 联调口径文档（数字孪生对接用） |
| `data_logs/` | 运行期自动生成的日志与遥测数据 |

---

## 配套使用 / Pairing with the digital twin

本地面站与同仓库的 [`digital_twin/`](../../digital_twin/)（数字孪生仿真环境）配套：

1. 先启动 `digital_twin/Build_GCS_Compatible/USV_Sim2Real_Simulation_Platform.exe`
2. 再启动本地面站
3. 在工具栏点「🚀 一键启动数字孪生」即可联调

---

## 开源协议 / License

本程序以 **GNU GPL v3** 发布（因其依赖 GPL 授权的 PyQt5），完整条款见同目录 `LICENSE`；
第三方组件的许可与归属见 `THIRD_PARTY_NOTICES.md`。

依 GPL-3.0，分发本可执行程序时应同时提供对应的完整源代码。本仓库当前只分发可执行程序；
如你需要对应源码（用于修改、审计或再分发），请通过本仓库的 Issue 或作者主页联系获取。

This program is released under **GPL-3.0** (it depends on GPL-licensed PyQt5).
This repository currently distributes the executable only; please contact the authors via
this repository's Issues if you need the corresponding source code.

---

## 出处 / Credits

华南理工大学 NOF 创新创业团队 · 海洋科学与工程学院
NOF Innovation & Entrepreneurship Team, School of Marine Science and Engineering,
South China University of Technology.
