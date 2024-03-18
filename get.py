from random import random

import requests
import json


def get_(session_hash):
    url = 'https://v2.genshinvoice.top/run/predict'
    data_str = f'{{"data":["今天星期天","流萤_ZH",0.5,0.6,0.9,1,"ZH",true,1,0.2,null,"Happy","",0.7],"event_data":null,"fn_index":0,"session_hash":"{session_hash}"}}'

    data_dict = json.loads(data_str)
    # 检查请求是否成功

    payload = data_dict

    # 发送POST请求
    response = requests.post(url, json=payload)
    r = response.json()
    name = r['data'][1]['name']
    url = f'https://v2.genshinvoice.top/file={name}'

    file_response = requests.get(url)
    if file_response.status_code == 200:
        with open(f'123.wav', 'wb') as file:
            file.write(file_response.content)
        print('文件下载成功')
    else:
        print('文件下载失败')

    # 打印响应内容


if __name__ == '__main__':
    get_('pjzd93ylekc')
