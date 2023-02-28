
# 面临需要登录的网站时候，可以使用HTTPBasicAuthHandler来请求这样的页面
"""
HITPDefaultErrorHandler ：用于处理 HTTP 响应错误，错误都会抛出 HTTP Error 类型的异常 。
HTTPRedirectHandler ：用于处理重定向 。
HTTPCookieProcessor ： 用于处理 Cookies 。
HπPPasswordMgr ：用于管理密码，它维护了用户名和密码的表 。
HTTPBasicAuthHandler ： 用于管理认证，如果一个链接打开时需要认证，那么可以用它来解 决认证问题。
"""
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()  # 实例化HTTPPasswordMgrWithDefaultRealm()的对象

p.add_password(None, url, username, password)   # 使用add_password方法添加进去用户名和密码

auth_Handler = HTTPBasicAuthHandler(p)   # 传入p以后就可以建立这样一个处理验证的Handler
opener = build_opener(auth_Handler)      # 利用这个build_opener()构建一个opener

try:
    result = opener.open(url)     # 利用opener的open()方法打开链接
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)