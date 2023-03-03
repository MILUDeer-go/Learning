# 使用方法 post(url, data=None, json=None, **kwargs) Sends a POST request.
"""
post方法主要定义了三个参数，分别是url，data, json。
url参数用来传递字符串类型的URL。data是一个可选参数，用来传递字典，参数列表，字节流，
以及文件类型的对象。json也是一个可选参数，会自动将字典类型的对象转换为json格式。
"""

# __desc__ = 通过requests模块的post方法发起HTTP POST请求

import requests
import urllib.error

""" 
(1) 站点的登录通常发起的是HTTP的POST请求
在本节的代码实例中，以京东商城的登录作为例子
"""

URL = "https://passport.jd.com/new/login.aspx"

"""
(1) 定义一个全局的data对象，用来传递登录请求所需传递的参数
(2) 京东商城PC页面的登录远不止这些参数，而且涉及到参数的加密，在本节的代码中，仅演示如何发起POST请求，
     在后续的教程中会详细讲解如何模拟站点登录
"""

data = {
    "uuid": "7c52477f-66af-4902-8429-51d51f6b38c4",
    "loginname": "18819353206",
    "nloginpwd": "Thvm9iAfZ/MhW8VbEDSscBJtwxLLXCKki4g="
}

# 发起POST请求，参数data用来传递请求参数
try:
    response = requests.post(URL, data)
    print(response.text)
except urllib.error as e:
    print(e.code, e.reason)

# 登录失败，代码实例仅演示如何发起POST请求