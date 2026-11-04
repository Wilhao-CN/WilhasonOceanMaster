# 第三方组件声明（THIRD_PARTY NOTICES）

> 本文件随二进制发布包提供，列出发布物中包含的第三方组件及其许可。
> 本包为**纯二进制发布物，不含 Unity 工程源码**（构建方式见 `README_V1.md`）。
> 本文档与随包提供的 `digital_twin/LICENSE`、`digital_twin/NOTICE` 共同构成发布包的许可声明文件集。
> 本文档内嵌 MIT 许可证全文（附录 A）；Apache License 2.0 全文见随包 `digital_twin/LICENSE` 文件。


## 1. 第三方开源组件

### 1.1 Crest Ocean Framework
**涉及文件**：`USV_Sim2Real_Simulation_Platform_Data/Managed/Crest.dll`、`Crest.Examples.dll`

- **许可**：MIT License
- **版权声明**：Copyright (c) 2019-2020 Wave Harmonic Ltd and contributors
- **处理**：✅ 允许再分发。须保留本声明、上述版权行，以及下文 **附录 A** 中的 MIT 许可证全文。

### 1.2 IronPython 及 Microsoft 动态语言运行时
**涉及文件**：`Managed/IronPython.dll`、`Microsoft.Dynamic.dll`、`Microsoft.Scripting.dll` 等

- **许可**：Apache License 2.0
- **版权声明**：Copyright (c) .NET Foundation and Contributors. All Rights Reserved.
- **处理**：✅ 允许再分发。须保留本声明、上述版权声明，以及随包 `digital_twin/LICENSE` 中的 Apache 2.0 全文。经追溯，本发布包所引入的 IronPython/DLR 组件未随附可获得的独立 NOTICE 文件，故本包未转发第三方 NOTICE 声明；本声明本身已满足 Apache 2.0 对版权与许可声明保留的基本要求。

### 1.3 Newtonsoft.Json
**涉及文件**：`USV_Sim2Real_Simulation_Platform_Data/Managed/Newtonsoft.Json.dll`

- **许可**：MIT License
- **版权声明**：Copyright (c) 2007 James Newton-King
- **处理**：✅ 允许再分发。须保留本声明、上述版权行，以及下文 **附录 A** 中的 MIT 许可证全文。


## 2. Unity 引擎与官方包

**涉及文件**：`UnityEngine.*.dll`、`Unity.*.dll`、`UnityPlayer.dll`、`MonoBleedingEdge/` 运行时，以及 Unity 官方包。

- **许可**：Unity Companion License / Unity 官方组件许可
- **处理**：作为 Unity 构建产物的运行时组成部分随包分发，保持原样。
- **声明位置**：经检查，本发布包中未包含 Unity 自动生成的 `Third-Party Notices.txt`。Unity 引擎及各官方包的具体版权与许可声明，参见 Unity 安装目录或官方文档。


## 3. 项目自有代码与资产（Project-Owned Code & Assets）

> **重要提示**：本项目采用**分层许可**。Apache License 2.0 **仅适用于** 3.1 明确列出的软件组件，**不适用于** 3.2 所述数字孪生环境资产或任何未明确声明的项目内容。

### 3.1 以 Apache License 2.0 发布的脚本组件
**涉及文件**：`USV_Sim2Real_Simulation_Platform_Data/Managed/Assembly-CSharp.dll` 等自研逻辑代码（以编译后二进制形式随包分发）。

- **许可**：Apache License 2.0
- **版权声明**：Copyright (c) 2026 New Ocean Force (NOF), School of Marine Science and Engineering, South China University of Technology
- **说明**：上述脚本组件按 Apache License 2.0 发布，许可证全文见 `digital_twin/LICENSE`。接收者可依该许可证使用、修改、分发上述组件，但须遵守其条款。本项目自有代码的 NOTICE 声明见随包的 `NOTICE` 文件（或 `digital_twin/NOTICE`）。

### 3.2 保留所有权利的数字孪生环境资产（Proprietary Digital Twin Assets）
**涉及内容**：场景（Scenes）、预制体（Prefabs）、材质（Materials）、地形/环境数据、UI 布局文件，以及未在 3.1 中明确列出的任何项目创作性资产。

- **权利状态**：**保留所有权利（All Rights Reserved）**
- **说明**：上述资产**未**以 Apache License 2.0 或其他开源许可证授权。未经版权持有人事先书面许可，不得复制、修改、分发或用于商业目的。`digital_twin/LICENSE` **不适用于**本节所述资产。


## 附录 A：MIT License 全文
（适用于 Crest Ocean Framework 与 Newtonsoft.Json）

```text
MIT License

Copyright (c) 2019-2020 Wave Harmonic Ltd and contributors
Copyright (c) 2007 James Newton-King

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.