# FUCK-Gradio
本项目利用了Selenium和Browsermob-Proxy技术，通过模拟浏览器行为来绕过Gradio框架网站的反爬机制。该网站的反爬机制基于随机生成的在线码，并通过WebSocket保持连接以确保在线码的有效性。传统的请求方式难以模拟这种动态交互过程，因此我采用了Browsermob获取在线码并且用Selenium保持连接来实现这一目标。

Windows版本适用于Edge浏览器及其驱动，而Linux版本适用于Chrome浏览器及其驱动。虽然这个项目提供了一个可行的思路，但由于配置环境和路径调整可能会耗费大量时间，因此需要小白谨慎考虑是否选择此项目。
