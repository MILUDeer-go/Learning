# 简单的爬虫，爬取python官网的页面

import urllib.request
import pprint
# 使用urlopen()爬取指定网址的网页源代码
url = 'https://www.python.org'
response = urllib.request.urlopen(url)

# pprint.pprint(response.read().decode('utf-8'))
print(response.read().decode('utf-8'))   # 爬取网页源码,解码
print(type(response.read()))
print(type(response.read().decode('utf-8')))
# print("="*40)      # 打印分割线
#
# print("响应的类型：", type(response))   # 输出响应的类型
# print("响应的状态：", response.status)
# print("响应的头信息：", response.getheaders())
# print("响应的头中的服务器值：", response.getheader('Server'))

