# 第三方组件声明（THIRD_PARTY NOTICES）

> 本文件随开源发布包提供，列出二进制发布物中包含的第三方组件及其许可。
> 依据：维护者此前文件清单审查（`FILE_MANIFEST.md`）§2.1 / §4「许可合规三件事」（该清单为本地工作文件，未入库）。
> 本包为**纯二进制发布物，不含 Unity 工程源码**（见 README_V1.md「构建方式」）。

## 1. 可分发的第三方开源组件

### Crest Ocean Framework（`USV_Sim2Real_Simulation_Platform_Data/Managed/Crest.dll`、`Crest.Examples.dll`）
- **许可**：MIT License
- **版权**： Crest Ocean Framework 作者
- **处理**：✅ 允许再分发，须保留本声明与版权声明。

### IronPython 及 Microsoft 动态语言运行时（`Managed/IronPython.dll`、`Microsoft.Dynamic.dll`、`Microsoft.Scripting.dll` 等）
- **许可**：Apache License 2.0
- **处理**：✅ 允许再分发，须保留本声明与 LICENSE 文本（全文见 <https://www.apache.org/licenses/LICENSE-2.0>）。

### Unity 引擎与官方包（`USV_Sim2Real_Simulation_Platform_Data/Managed/UnityEngine.*.dll`、`Unity.*.dll`、`UnityPlayer.dll`、`MonoBleedingEdge/` 运行时）
- **许可**：Unity Companion License / Unity 官方组件许可
- **处理**：作为 Unity 构建产物的运行时组成部分随包分发，保持原样。

### Newtonsoft.Json（`USV_Sim2Real_Simulation_Platform_Data/Managed/Newtonsoft.Json.dll`）
- **许可**：MIT License
- **版权**： James Newton-King
- **来源**：Unity `com.unity.nuget.newtonsoft-json` 包随构建引入（本版新增，供"关于系统"页面 JSON 序列化使用）
- **处理**：✅ 允许再分发，须保留本声明与版权声明（全文见 <https://github.com/JamesNK/Newtonsoft.Json/blob/main/LICENSE.md>）。

## 2. 项目自有代码

- `Assembly-CSharp.dll` 等自研逻辑代码：**项目自有**。
- 开源协议：仓库根 `LICENSE` / README 中标注为准（当前状态见 README_V1.md「许可」章节；维护者落字前为"待定"）。

## 3. 未完成项（沿用 README_V1.md ⚠ 声明）

- **3D 模型 / 贴图资源的原始许可逐项复核**：尚未完成，由维护者复核后更新本文件。
- OPC UA（`Opc.Ua.*`）、NDI（`Processing.NDI.Lib.x64.dll`）相关许可风险文件：经清点为 **0 个**，已剔除，不随本包分发。
