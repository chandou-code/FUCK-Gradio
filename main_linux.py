import re
import threading

from browsermobproxy import Server

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import platform
import subprocess
import get


def open_cmd():
    # 判断是否已经打开过cmd窗口
    cmd_window_open = False

    # 检查是否存在cmd窗口
    try:
        subprocess.check_output(['tasklist', '/FI', 'WINDOWTITLE eq cmd'], shell=True)
        cmd_window_open = True
    except subprocess.CalledProcessError:
        pass

    # 打开cmd窗口并执行命令
    if not cmd_window_open:
        cmd = 'cmd /K java --add-opens java.base/java.lang=ALL-UNNAMED -jar browsermob-dist-2.1.4.jar --use-littleproxy false'
        process = subprocess.Popen(cmd, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE,
                                   cwd='./browsermob-proxy-2.1.4./lib')


hash = ''
is_hash_updated = False  # 新增布尔变量，表示hash值是否已更新


def sel_run():
    os_type = platform.system()

    if os_type == 'Windows':
        open_cmd()
    else:
        print("当前操作系统不是 Windows，无法执行 open_cmd() 函数")

    global hash, is_hash_updated
    capabilities = DesiredCapabilities.CHROME
    capabilities['acceptInsecureCerts'] = True

    server = Server(
        r"./browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    proxy = server.create_proxy()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    options.add_argument('--incognito')
    options.add_argument(
        "user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'")  # UA
    options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
    options.add_argument('--ignore-ssl-errors')  # 忽略SSL错误
    s = Service('./chromedriver')
    Chrome = webdriver.Chrome(service=s, options=options)

    Chrome.get("https://v2.genshinvoice.top/")
    wait = WebDriverWait(Chrome, 600)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="component-3"]/label/textarea')))

    element.clear()  # 清空文本框内原有内容
    element.send_keys(f"{int(time.time())}")

    element1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="component-30"]')))
    proxy.new_har("douyin", options={'captureHeaders': True, 'captureContent': True})
    element1.click()

    # 等待直到第二个元素出现

    element2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="component-33"]/div[2]/a/button')))

    # 点击第二个元素
    element2.click()

    result = proxy.har
    for entry in result['log']['entries']:
        request = entry['request']
        response = entry['response']

        if request['url'] == 'https://v2.genshinvoice.top/run/predict':
            print('Request URL:', request['url'])
            if 'queryString' in request:
                pass

            if 'postData' in request:
                post_data = request['postData']
                post_data = str(post_data)

                match = re.search(r'"session_hash":"(\w+)"', post_data)
                if match:
                    session_hash = match.group(1)
                    print(session_hash)
                    hash = session_hash
                    is_hash_updated = True  # 设置布尔变量为True，表示hash值已更新
                    time.sleep(1234567)


def run_get():
    global hash, is_hash_updated
    while not is_hash_updated:  # 等待hash值更新
        continue
    with open('../server/hash.txt', 'w', encoding='utf-8') as f:
        f.write(hash)


if __name__ == '__main__':
    thread1 = threading.Thread(target=sel_run)
    thread1.start()

    thread2 = threading.Thread(target=run_get)
    thread2.start()
