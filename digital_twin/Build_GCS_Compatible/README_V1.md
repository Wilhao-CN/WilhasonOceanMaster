# 无人船数字孪生仿真环境 · V1

> Unmanned Surface Vehicle (USV) Digital Twin — Unity Simulation Environment
>
> **版本**：V1 · **构建日期**：2026-10-07 · **许可**：待定（见文末第三方组件）
> **产品名**：`USV_Sim2Real_Simulation_Platform`（公司：`SCUT_NOE`）
> **主程序**：`USV_Sim2Real_Simulation_Platform.exe`
>
> 📄 **对接地面站请先读**：[`JOINT_README.md`](JOINT_README.md)（双方联合口径 R1–R10）；
> 协议 / 端口权威：[`GROUND_STATION_INTERFACE.md`](GROUND_STATION_INTERFACE.md)。
>
> 本文件是 **V1 的对外说明**；同目录下的 `README.md` 是 **V0.5 预览版**的历史说明，**保留不动**。

---

## ⚠️ 从 V0.5 ／旧版升级的注意事项（**老用户先读这一节**）

| # | 事项 | 说明 |
|---|---|---|
| 1 | **主程序改名** | 旧 `DDPG USVS.exe` → 新 **`USV_Sim2Real_Simulation_Platform.exe`**。旧文件已从本目录移除（若你手上有旧版，请直接用新 exe） |
| 2 | **存档目录名跟着产品名变** | 用户数据目录 = `%USERPROFILE%\AppData\LocalLow\<公司名>\<产品名>\`，现在是 `…\LocalLow\SCUT_NOE\USV_Sim2Real_Simulation_Platform\`。**旧目录 `…\DefaultCompany\DDPG USVS\` 的内容需自行拷到新目录**（拷贝而非移动，旧目录留作回滚） |
| 3 | **参数文件优先落在 exe 同目录** | 参数存档是 `<exe 同目录>\dt_params.json`；**该目录不可写时**（例如装进 `Program Files`）才回退到上面的 `LocalLow` 目录 |
| 4 | **小心"参数看起来丢了"** | 见第 2 条：目录名一换，旧参数就"找不到"了。**不是文件被删** |
| 5 | **产品名与公司名从本版起冻结** | 它决定存档目录；**发布后不可再改**（改了老用户的参数与窗口布局会"消失"） |
| 6 | **本版不再包含 OPC UA 与 NDI** | 见下文「本版相对旧版的改动」 |

---

## 本版相对旧版的改动

| 项 | 改动 |
|---|---|
| **OPC UA** | **已彻底移除**（`Assets/Dll` 55 个 dll、`OPC_UA.cs`、`WindArea.cs` 及其引用点）⇒ 消除 GPL/RCL 许可风险 |
| **NDI 推流** | **已彻底移除**（`jp.keijiro.klak.ndi` 包 + `manifest.json` 条目）⇒ 消除专有运行时的再分发问题；三路视频一直走 **TCP**，功能面不变 |
| **包体** | 相比旧产物**减小约 40 MB** |
| **主程序名** | `DDPG USVS.exe` → `USV_Sim2Real_Simulation_Platform.exe` |

> 如果你的旧流程依赖 OPC UA 数据或 NDI 推流：**本版不支持**（这两项在真船/地面站链路里本来也未使用）。

---

## 这是什么

用 **Unity** 实现的**无人船（USV）数字孪生仿真环境**，在虚拟场景中 1:1 镜像真船的
物理行为、传感器遥测与地面站通信协议。它同时是三样东西：

- **物理仿真器** —— 双体无人船与浮船坞的运动、浮力、波浪、水动力阻尼；
- **协议从站** —— 完整实现真地面站的控制帧下行与遥测帧上行协议（逐字节对齐）；
- **可视化终端** —— 三路实时视频、遥测面板、小地图与定位打点系统。

主要用于**演示、控制算法联调与教学**，可与配套的地面站软件或自研算法对接。

---

## 运行环境

| 项 | 要求 |
|---|---|
| 操作系统 | Windows 10 / 11（64 位） |
| 硬件 | 支持 DirectX 11 的显卡；建议 8 GB 内存以上 |
| 分辨率 | 1600×900 或更高（界面按固定像素渲染） |
| 依赖 | **无需安装 Unity**，解压即用 |

---

## 快速开始

1. 解压整个文件夹到任意路径（**路径建议不含中文或空格**）
2. 确认 `gcs_target_ip.txt` 里的目标 IP：
   - 与地面站**同一台电脑**运行 → 保持 `127.0.0.1`
   - 地面站在**另一台电脑** → 填地面站的实际 IP
3. 双击 **`USV_Sim2Real_Simulation_Platform.exe`** 启动
4. 按 **`F8`** 展开控制面板

> 修改 `gcs_target_ip.txt` 后**直接重启程序即可生效，无需重新构建**。
> ⚠ 地面站的**「一键启动数字孪生」会把它覆盖为 `127.0.0.1`**（见 `JOINT_README.md` R6）。

---

## 默认网络参数

### 视频（Unity 作为 TCP 服务端）

| 端口 | 画面 |
|---:|---|
| 5001 | 船坞视角 |
| 5002 | 全局俯视（小地图） |
| 5003 | 无人船视角 |

### 数据（UDP）

| 载体 | 控制（地面站 → 孪生） | 遥测（孪生 → 地面站） |
|---|---:|---:|
| 无人船（ID `0x02`） | **8888** | **8889** |
| 浮船坞（ID `0x01`） | **8081** | **8080** |

- 控制帧 **33 字节**，遥测帧 **65 字节**，遥测频率 **50 Hz**
- 程序**忽略所有非 33 字节的扩展帧**（属正常行为，非故障）
- 孪生模拟源端口 **8890 / 8082** 地面站零命中，**可自由使用**

---

## 操作说明

| 操作 | 按键 |
|---|---|
| 展开 / 收起控制面板 | **`F8`** 或右上角 `◀ HUD` |
| **一键重置**（两船回到初始位置） | **`F5`** |
| 定位系统窗口全屏 | **`F6`** |
| 航向控制 | `W` 前进 / `S` 后退 / `A` 左转 / `D` 右转 |
| 切换视角 | 面板内按钮（无人船 / 船坞 / 全局） |
| 调节波浪 | 面板内"波浪调节"滑条 |

### 定位系统

- **双击屏幕左下角的小地图**，或点面板里的 **「定位系统」** 按钮打开
- 窗口左侧工具列：**浏览**（拖拽平移、滚轮缩放 ×1.25）/ **打点**（左键落点、右键退点）/ **清除打点**
- 窗口可拖动、缩放、关闭，**位置与大小自动记忆**
- 地图上显示两船实时位置：🔵 蓝 = 无人船天线 A　🟦 青 = 船坞天线 A　🩷 粉 / 🟡 金 = 天线 B
 　🟢 绿 = **A+B 中点**（算法参考位置）　🟠 橙 = 你打的点

### 参数设置窗口（V1 新增）

`F8` → **「参数设置」**。窗口底部：**恢复默认 / 保存 / 导出 / 导入**。
分组一览：

| 分组 | 内容 | 备注 |
|---|---|---|
| **力映射 · PWM ↔ 力** | 曲线系数 `posA/posB/negA/negB/maxForcePos/maxForceNeg` 可改；`pwmMid` 与 `exponent` **只读**；右侧**曲线预览** | ⚠ 顶部常驻红字警告：**改了力映射，孪生就不再代表真船**（见 `JOINT_README.md` R1） |
| 载体动力学 · 小船 / 船坞 | `M / I / Xu / Yv / Nr`、推力与扭矩限幅 | 即时生效 |
| 传感器 · GPS 噪声 | `σ`（默认 **0 = 关闭**）、零偏、随机种子 | 见 `JOINT_README.md` R9 的 4 个副作用与红线 |
| 相机 · 视场角 | 三个屏幕相机 FOV | 推流画面同步跟随 |
| 环境 · 波浪 / 水材质 / 浮力 / 光照 | 波浪幅度、频谱 6 项、水色 8 项、浮力组（按对象 3 组）、太阳方位/强度/颜色/雾 | 改资产类参数时会**自动创建运行时副本**，不动原始资产 |
| GNSS · 锚点 | `lat0/lon0` + 地图四角 + **【应用锚点】复合按钮** | 一次点击内完成"改锚点 → 重算四角 → 刷新"，保证**船图标与底图不错位** |
| 通信端口 / IP | **只读**回显 | 改端口请改 `gcs_target_ip.txt`（IP）或重新构建（端口） |

---

## 参数存档与导出（**行为说明，避免误判"没保存"**）

| 项 | 位置 / 行为 |
|---|---|
| 存档文件 | `<exe 同目录>\dt_params.json`（+ `.bak`）；该目录不可写时回退 `…\LocalLow\SCUT_NOE\USV_Sim2Real_Simulation_Platform\` |
| **只存非默认项** | 文件里**只有你改过的参数**。⇒ **一个都没改过时，不会生成这个文件**（`"values": []` 即"全默认"）——**这是正常行为** |
| 载入规则 | 载入 / 导入时**先把全部参数回出厂值**，再套用文件里的项 ⇒ **文件里缺的项 = 用出厂值** |
| 导出 | 导出到 `<参数目录>\ParamsExport\`；可改名 / 删除（都限定在该目录内，防路径穿越） |
| 导入失败 | 坏文件或 `schema` 不符 ⇒ **拒绝导入且不改动任何当前值** |
| 想回到真船一致 | 「恢复默认」= 回到与真船一致的**权威实测值** |

---

## 已知限制

- **打点数据只保存在内存**，退出程序后不保留
- 船坞 GPS 天线的**虚拟布置方向与实船不一致**（当前前后、实为左右），位置显示约 **0.5 m** 系统偏差
  —— 已与地面站对齐口径（`JOINT_README.md` R3）
- 启动时若提示 `Crest Validation: Foam is not enabled...`，属**已知渲染配置警告**，不影响功能
- 启动日志里若出现"**因目标计算机积极拒绝，无法连接**"：那是保留的 **Python TCP 桥（`127.0.0.1:65410`）**
  在等一个未启动的 Python 端 —— **本机的"合并版本地物理"已接管，属纯提示，不影响运行**
- `bundleVersion` 当前为 **0.1**（发布前由维护者裁定是否改为 V1 正式版本号）
- 定位系统界面样式与最新版仍在收敛中

---

## 第三方组件与许可

> ⚠️ **本节发布前必须由维护者复核。**

| 组件 | 用途 | 许可 | 处理 |
|---|---|---|---|
| Unity Engine | 运行时 | Unity Editor License（分发构建产物受 Unity 条款约束） | 保持 |
| **Crest Ocean System** | 海洋渲染 | **MIT** | 可随包分发（**需保留署名**） |
| IronPython（`IronPython.dll` 等） | 脚本支持 | **Apache-2.0** | 需在 `THIRD_PARTY_NOTICES` 中署名 |
| Unity 官方包（Input System / TextMeshPro / Splines / Recorder / Burst / Mathematics…） | 输入 / UI / 录制 | Unity Package License | 保持 |
| ~~OPC UA .NET Stack~~ | （未使用） | GPL / RCL | ✅ **V1 已剔除** |
| ~~NDI Runtime~~ | （未使用） | 专有，再分发须注册 | ✅ **V1 已剔除** |
| 3D 模型 / 贴图资源（船体、船坞、环境、Crest-Examples） | 场景资源 | 见各资源原始许可 | ⚠ **需逐项核对**（未完成） |

---

## 目录结构

```
Build_GCS_Compatible/
├── USV_Sim2Real_Simulation_Platform.exe        主程序
├── USV_Sim2Real_Simulation_Platform_Data/      资源与托管程序集
├── USV_Sim2Real_Simulation_Platform_BurstDebugInformation_DoNotShip/   Burst 调试信息（**可删**，不影响运行）
├── UnityPlayer.dll                             Unity 运行时
├── UnityCrashHandler64.exe                     崩溃上报（**可删**）
├── MonoBleedingEdge/                           Mono 运行时
├── gcs_target_ip.txt                           目标地面站 IP（可直接编辑）
├── GROUND_STATION_INTERFACE.md                 对接协议说明（权威）
├── JOINT_README.md                             与地面站的联合口径 R1–R10（**必读**）
├── README_V1.md                                本文件
├── README.md                                   V0.5 预览版历史说明（保留）
├── dt_params.json / .bak                       参数存档（改过参数才有）
└── ParamsExport/                               参数导出目录
```

---

## 构建方式（维护者）

Unity 菜单：

```
Tools > Ground Station > Build Windows x64
```

- **默认输出目录**：`Build_GCS_Compatible/`（工程根下）
- **输出文件名**：跟随 `PlayerSettings.productName` ⇒ `USV_Sim2Real_Simulation_Platform.exe`
  （⚠ 改了产品名，**新 exe 会以新名字出现，不会覆盖旧名字的 exe** —— 整理产物时记得清旧的）
- 构建脚本会自动复制 `gcs_target_ip.txt` 与 `GROUND_STATION_INTERFACE.md` 到输出目录

命令行批处理：

```
-batchmode -nographics -quit -projectPath <工程路径> ^
  -executeMethod GroundStationBuild.BuildWindows64 ^
  -gcsBuildPath <输出目录>\USV_Sim2Real_Simulation_Platform.exe
```

---

## 反馈

问题与建议：**（待填）**
