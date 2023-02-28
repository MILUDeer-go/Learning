# __desc__ = 通过requests模块的get方法发起HTTP GET请求

# 使用函数 get(url, params=None, **kwargs) Sends a GET request.

# 使用requests模块，必须先执行import进行导出
import requests

# www.chipscoco.com为薯条老师的个人博客，可授权进行合法抓取
URL = "http://www.chipscoco.com/?id=9"
response = requests.get(URL)

# http状态码为200，说明请求成功
if response.status_code == 200:
    # 输出http服务器的响应头
    print(response.headers)
    # 输出字符串类型的响应体,也就是的这里网页的HTML代码
    # print(response.text)