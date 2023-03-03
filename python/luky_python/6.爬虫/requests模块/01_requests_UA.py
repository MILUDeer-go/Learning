# 定制HTTP请求头需通过关键字参数headers进行传递。headers
# 接收一个字典类型的参数，键名表示HTTP请求头的字段名，键值为请求字段所对应的字段值。

import requests

# 爬取百度首页的数据
# url = 'http://www.baidu.com/s?wd=python'
# 构建请求头
headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'
}
# # 设置爬虫程序的UA，可在一定程度上防止被服务端反爬
# response = requests.get(url, headers=headers)
#
# with open('baidu.html', 'wb') as f:
#     f.write(response.content)

url = 'http://www.baidu.com/s?'
# 构建参数字典
data = {
    'wd': 'python'
}

response = requests.get(url, headers=headers, params=data)
with open('baidu1.html', 'wb') as f:
    f.write(response.content)