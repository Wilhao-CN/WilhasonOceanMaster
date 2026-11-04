# License Scope / 许可证范围

本仓库为多许可证仓库。各目录/发布包相互独立，以对应目录内的 `LICENSE` 为准。具体范围如下：

| 范围 | 许可证 | 说明 |
| --- | --- | --- |
| 根目录 `LICENSE` | MIT | 仅适用于仓库骨架、根目录文档与配置文件（如 `README.md`、`.gitignore`、`CITATION.cff`、`LICENSE-SCOPE.md` 等）。 |
| `digital_twin/` | Apache License 2.0 | 见 `digital_twin/LICENSE`；**注意**：其内部的数字孪生环境资产（如 3D 模型、贴图）为“保留所有权利（All Rights Reserved）”，具体见 `digital_twin/Build_GCS_Compatible/THIRD_PARTY_NOTICES.md` 第 3.2 节。 |
| `LandStation/` | GNU GPL v3 | 见 `LandStation/LICENSE`。 |
| `LandStation-Lite-v1.0.1-src.zip` | GNU GPL v3 | 见压缩包内 `LICENSE`。 |
| `docs/`、`parameters/`、`usv/` | MIT | 随根仓库 MIT，除非文件内另有声明。 |
| `.github/`、`traffic-data/` | MIT | 随根仓库 MIT，除非文件内另有声明。 |

**边界声明**：根目录 MIT 许可证**不覆盖** `digital_twin/` 与 `LandStation/`。使用 `LandStation/` 中任何内容即受 GPL-3.0 约束；使用 `digital_twin/` 中任何内容受 Apache-2.0 约束（其独有资产除外）。各子目录许可证不可混用。