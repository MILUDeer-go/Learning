# 使用Request类来构建简单的请求
import urllib.request

url = "https://www.baidu.com/"
# 构建一个请求类request
request = urllib.request.Request(url)
# 使用urlopen()来请求源码
response = urllib.request.urlopen(request)
# read()方法读取页面源码
print(response.read().decode('utf-8'))
