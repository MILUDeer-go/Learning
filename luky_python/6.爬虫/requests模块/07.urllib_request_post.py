# 调用urlopen方法时，默认发起的是GET请求，如需提交数据给服务端，需通过data参数进行传递，此时发起的是POST请求。
# 通过Python中的字典类型，可快速地构建提交的数据，然后再调用urllib.parse的urlencode方法，将其转换为字符串。

import urllib.parse, urllib.request

url = 'http://httpbin.org/post'

values = {'name': 'MILUDeer', 'age': '20'}
data = urllib.parse.urlencode(values)   # 将要提交的数据转换为url编码

# 使用encode（）方法转换为字节流
# 传递字节流类型
data = data.encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    # 将字节流转换为字符串
    the_response = response.read().decode('utf-8')
    print(the_response)