markdown
# Gradio框架反爬机制绕过项目

## 项目简介

本项目利用了 Selenium 和 Browsermob-Proxy 技术，通过模拟浏览器行为来绕过 Gradio 框架网站的反爬机制。该网站的反爬机制基于随机生成的在线码，并通过 WebSocket 保持连接以确保在线码的有效性。传统的请求方式难以模拟这种动态交互过程，因此采用了 Browsermob 获取在线码，并且用 Selenium 保持连接来实现这一目标。

Windows 版本适用于 Edge 浏览器及其驱动，而 Linux 版本适用于 Chrome 浏览器及其驱动。尽管提供了一个可行的思路，但由于配置环境和路径调整可能会耗费大量时间，因此需要小白谨慎考虑是否选择此项目。

## 使用说明

1. 配置环境并安装所需驱动（Windows 版本使用 Edge 浏览器驱动，Linux 版本使用 Chrome 浏览器驱动）。
2. 安装项目依赖包：

```
pip install -r requirements.txt
```
运行项目。

#注意事项
本项目需要配置浏览器驱动，并根据操作系统选择合适的驱动版本。
需要耐心配置环境和路径，否则可能会出现错误。
建议有一定编程和调试经验的用户尝试，小白用户可能会遇到困难。
欢迎使用并提出改进建议！


我将项目简介、使用说明和注意事项进行了整理和修订，使其更清晰易懂。如有需要进一步修改或添加的内容，请告诉我。
