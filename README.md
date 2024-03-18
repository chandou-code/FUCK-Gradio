# FUCK-Gradio
本项目利用Selenium和Browsermob-Proxy技术来绕过Gradio框架网站的反爬机制。该反爬机制的核心在于通过随机生成的在线码作为参数，在WebSocket两端保持连接，确保在线码有效性。传统的请求方式无法模拟这种动态交互过程，因此需要借助浏览器自动化工具来实现。

通过Selenium控制浏览器打开网站，并利用Browsermob-Proxy进行抓包操作，实现自动获取到携带在线码的session_hash。有了这个session_hash，就可以在后续的数据请求中模拟用户的有效身份，成功获取所需数据。

这个项目的关键在于模拟浏览器行为，确保与网站保持持续连接并且正确处理在线码，从而绕过了简单的请求方式无法解决的动态交互问题。同时，该方案还可以实现跨平台部署，适用于Linux和Windows系统，为爬取特定网站数据提供了一种有效的解决方案。
