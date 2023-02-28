# 使用本地代理来做爬虫
# ProxyHandler ：用于设置代理 ， 默认代理为空 。参数是个字典
# URLError 捕捉错误
# build_opener 构造请求

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = "127.0.0.1:9000"


# 构造一个代理
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
})

# 使用build_opener()构造一个打开者
opener = build_opener(proxy_handler)

try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))

except URLError as e:
    print(e.reason)

