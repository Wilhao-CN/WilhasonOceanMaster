# LandStation-Lite v1.0.1 · 地面站运行版

**无人船地面站 —— 免安装可运行程序（Windows x64）**
Ground Station Runtime Package — no Python, no setup required.

> 这是**已经打包好的程序**，不需要安装 Python，也不需要配置任何环境。
> 完整使用说明见同目录的 **`使用说明.txt`**（先看这个）。

---

## 安全须知 / Safety

> 🔴 **本程序会驱动真实推进器、舵机与继电器。接真实船体前请先读 [`docs/SAFETY.md`](../docs/SAFETY.md)。**

几条必须先知道的结论（详见该文档 §3、§5）：

- **急停按钮依赖本程序存活**。程序崩溃、笔记本断电、串口线脱落时急停不可用——
  实船上**必须**另配一套独立于软件的物理断电开关。
- **本程序不做失联兜底**。链路中断后不会自动停船；「控制指令超时停船」必须由 MCU 固件实现。
- **急停帧只发一次**，不重发、不等 ACK。链路丢一帧，船不会停。
- **首次通电请拆桨或架空船体**，先验证电机转向与推力分配，再下水。

Before connecting to real hardware, read [`docs/SAFETY.md`](../docs/SAFETY.md).
The E-Stop is software-only and the ground station does **not** implement a
link-loss failsafe — keep an independent physical power cut-off on the vessel.

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
| `data_logs/` | 运行期自动生成的日志与遥测数据 |
| `README.md` | LandStation-Lite v1.0.1 · 地面站运行版·使用指南 |

---

## 配套使用 / Pairing with the digital twin

本地面站与同仓库的 [`digital_twin/`](../digital_twin/)（数字孪生仿真环境）配套：

1. 先将数字孪生平台（`USV_Sim2Real_Simulation_Platform.exe`）所在文件夹（`../digital_twin/Build_GCS_Compatible`）填入 `LandStation\config\simulator.json`中
2. 再启动本地面站
3. 在工具栏点「🚀 一键启动数字孪生」即可联调

---

## 视觉插件（预览版） / Vision Plugin (Preview)

本项目提供视频采集、画面显示与视觉窗口 UI。与之配套的 **NOF 自研视觉能力**（包括浮标识别、视觉居中、ArUco 靠泊测距等），已封装为一体化预览插件。

- **当前状态**：预览测试版。以独立模块形式接入，提供画面叠加与状态提示。
- **源码分发**：核心算法源码不随本包分发。完整接口与安装包将在后续版本中逐步开放。
- **底层依赖**：基于业界广泛使用的开源计算机视觉框架构建，遵循其原始许可条款；本项目自身代码遵循同目录声明的 GPL v3 协议。

> Vision Plugin (Preview): The core algorithm for buoy recognition, visual centering, and ArUco docking is packaged as a preview module. The core algorithm source code is closed-source in this release. The underlying software is built on widely-used open-source computer vision frameworks and complies with their original licenses.

---

## 开源协议 / License

本程序以 **GNU GPL v3** 发布（因其依赖 GPL 授权的 PyQt5），完整条款见同目录 `LICENSE`；
第三方组件的许可与归属见 `THIRD_PARTY_NOTICES.md`。

依 GPL-3.0，分发本可执行程序时应同时提供对应的完整源代码。
本程序对应的**完整源代码**见**本仓库根目录**的
[`LandStation-Lite-v1.0.1-src.zip`](../LandStation-Lite-v1.0.1-src.zip)，
公开可下载，无需注册、无需联系任何人。
如希望参与二次开发或加入兴趣小组，欢迎发送邮件至 **2571217194@qq.com**。

This program is released under **GPL-3.0** (it depends on GPL-licensed PyQt5).
The complete source code corresponding to this executable is publicly available
as [`LandStation-Lite-v1.0.1-src.zip`](../LandStation-Lite-v1.0.1-src.zip) at the
repository root — no registration or contact required.

---

## 出处 / Credits

华南理工大学 NOF 创新创业团队 · 海洋科学与工程学院
New Ocean Force (NOF), School of Marine Science and Engineering,
South China University of Technology.