# 第三方组件声明（THIRD_PARTY_NOTICES）

本程序使用了以下第三方组件，特此致谢并声明其许可归属。

## 1. 核心框架（GPL v3）

| 组件 | 版本 | 许可 | 说明 |
|---|---|---|---|
| PyQt5 | 5.15.11 | GPL v3 | 界面框架 |
| PyQtWebEngine | 5.15.7 | GPL v3 | 内嵌浏览器（地图） |
| PyQt5-Qt5 | 5.15.2 | LGPL v3 | Qt 运行库 |
| PyQtWebEngine-Qt5 | 5.15.2 | LGPL v3 | Qt 运行库 |

> 因依赖 GPL v3 授权的 PyQt5，本工程整体以 GNU GPL v3 发布，完整条款见同目录 `LICENSE` 文件。

## 2. 其他必需依赖

| 组件 | 版本 | 许可 | 说明 |
|---|---|---|---|
| pyqtgraph | 0.13.7 | MIT | 实时遥测曲线 |
| NumPy | 2.2.6 | BSD-3-Clause | 数值计算 |
| opencv-python | 4.11.0.86 | Apache-2.0 | 图像处理、视频解码 |
| pyserial | 3.5 | BSD-3-Clause | 串口通信 |
| pygame | 2.6.1 | LGPL-2.1 | USB 手柄读取 |

## 3. 前端 / 资源

| 组件 | 版本 | 许可 | 位置 |
|---|---|---|---|
| Leaflet | 1.9.4 | BSD-2-Clause | `ui/map/leaflet/`（已本地化，离线可用） |
| qwebchannel.js | 随 Qt | LGPL v3 | `ui/map/qwebchannel.js` |
| Level1_Pool 正交底图 | — | 项目方自有 | `ui/map/twin_maps/` |

---

## 致谢

- **Qt / PyQt** —— 界面与内嵌浏览器
- **Leaflet** —— 轻量地图渲染
- **pyqtgraph** —— 高性能实时绘图
- **OpenCV** —— 图像处理与视频解码
- 以及所有参与本工程前期研究工作的同学与老师

---