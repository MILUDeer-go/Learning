# 测试如果一个网页长时间没有响应，就跳过抓取

import urllib.request
import socket
import urllib.error

try:
    url = "https://www.baidu.com/"
    response = urllib.request.urlopen(url, timeout=0.00001)
except urllib.error.URLError as e:
    # isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
    if isinstance(e.reason, socket.timeout):
        print("time out")
