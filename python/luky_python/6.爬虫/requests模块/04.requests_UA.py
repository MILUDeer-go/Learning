# 使用requests模块设置爬虫的UA信息

import requests

"""
(1) 字典类型变量headers，用来定义HTTP请求头，在请求头部添加UA信息
(2) headers中的键User-Agent，用来定义HTTP的User-Agent请求头

"""
header = {
    # 设置爬虫的UA为谷歌游览器的UA
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
url = "https://www.baidu.com"
response = requests.get(url, headers=header)

print(response.cookies)