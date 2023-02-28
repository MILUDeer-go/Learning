# 进一步了解 Request 类的构造方法
# urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

from urllib import request, parse

url = 'http://httpbin.org/post'
# 构造请求头，伪装游览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0)',
    'Host': "python.org"
}
# 添加参数data
dic = {
    'name': 'hello'
}
# 使用bytes()方法构建字节流
data = bytes(parse.urlencode(dic), encoding='utf8')
# 构建请求类
req = request.Request(url, data=data, headers=header, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))


