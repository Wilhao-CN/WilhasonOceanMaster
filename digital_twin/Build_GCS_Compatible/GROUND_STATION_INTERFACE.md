# 地面站兼容接口

本文件定义 `USV_Sim2Real_Simulation_Platform` 数字孪生与 LandStation V3.3 的稳定接口。修改场景、模型或控制算法时，不应改变以下端口和数据格式；如确需改变，必须同步升级地面站。

## 视频接口

Unity 作为 TCP 服务端，地面站作为客户端连接。每帧按小端序发送：

1. `double`：Unix 时间戳（秒），8 字节。
2. `int32`：JPEG 数据长度，4 字节。
3. JPEG 数据。

| 端口 | 画面 | RenderTexture | 显示相机 | 推流相机 |
|---:|---|---|---|---|
| 5001 | 船坞 | `usv_rear`（历史名称） | `Dock` | `Camera_2` |
| 5002 | 全局俯视 | `MinimapRenderTexture` | `Globalmap` | `Main Camera` |
| 5003 | 无人船 | `usv_main` | `Camera_main` | `Camera` |

目标参数：无人船与船坞 1280×720、JPEG 质量 85、30 FPS。推流相机必须在 `LateUpdate` 中与对应显示相机同步位置、旋转和投影参数。

## UDP 接口

| 载体 | 地面站下发控制 | Unity 上报遥测 |
|---|---:|---:|
| 船坞 | UDP 8081 | UDP 8080 |
| 无人船 | UDP 8888 | UDP 8889 |

遥测包为当前 `USVTelemetrySender` / `DockTelemetrySender` 生成的 65 字节二进制协议，发送周期由 `FixedUpdate` 驱动，目标频率 50 Hz。

## IP 配置

`gcs_target_ip.txt` 必须与 EXE 位于同一目录。文件只包含一行目标 IPv4 地址：

- 地面站与数字孪生在同一台电脑：`127.0.0.1`
- 数字孪生在服务器：填写地面站可达的实际 IP

修改 IP 不需要重新构建。

## 标准构建

Unity 菜单：`Tools > Ground Station > Build Windows x64`

批处理入口：

```text
-batchmode -quit -projectPath <USV5> -executeMethod GroundStationBuild.BuildWindows64 -gcsBuildPath <输出目录>\USV_Sim2Real_Simulation_Platform.exe
```

构建脚本会自动复制 `gcs_target_ip.txt` 和本接口说明到输出目录。新构建必须先输出到独立目录并完成三路视频、两路遥测及控制端口验收，禁止直接覆盖当前可用版本。
