# 模拟登录github：只是思路
import requests
import re

def login():
    # session
    session = requests.session()
    # headers
    session.headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664.45Safari / 537.36'
    }

    # url1-获取token
    url1 = 'https://github.com/login'
    # 发送请求获取响应
    res_1 = session.get(url1).content.decode()
    # 正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />', res_1)[0]
    # print(token)

    # url2-登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    data = {
        'commit': 'Sign in',
        'utf8': '',            # 这里里面是一个勾
        'authenticity_token': token,
        'login': 'exile-morganna',
        'password': '1QAZ2wSX3edC4rfy',
        'webauthn-support': 'supported'
    }
    session.post(url2, data=data)

    # url3-验证
    url3 = 'https://github.com/exile-morganna'
    response = session.get(url3)
    with open('github1.html', 'w') as f:
        f.write(response.content)

if __name__ == '__main__':
    login()