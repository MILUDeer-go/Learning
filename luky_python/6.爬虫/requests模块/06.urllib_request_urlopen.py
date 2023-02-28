# 打开统一资源定位器函数：urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, context=None)
"""
url      http url,可为字符串或request对象(urllib.request.Request)

data     发送额外的数据给http服务器，须为bytes类型，默认为None。

timeout    可选的请求超时参数，没有传递时会使用一个默认的超时时间，仅用于http,https,ftp连接

context     ssl.SSLContext实例，用来定义SSL的传输选项，默认为None

cafile,capath    cafile指向一个PEM格式的CA证书文件，capath则指向一个包含一系列PEM格式的CA证书文件的目录
"""

# 简单爬取python官方首页
import urllib.request

url = 'http://python.org/'

with urllib.request.urlopen(url) as response:
    # urlopen返回的数据是一个字节流对象，需要通过decode方法转换为字符串
    html = response.read().decode('utf-8')
    print(html)