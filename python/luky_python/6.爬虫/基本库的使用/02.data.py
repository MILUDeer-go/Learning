# 使用post方式提交数据请求站点httpbin.org，提供HTTP请求POST测试

import urllib.parse
import urllib.request
import time

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# timeout 设置超时时间（s）
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url, data=data, timeout=1)
# read()方法是用来读取网页源码
print(response.read())
