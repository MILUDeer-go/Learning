# 获取网站的cookies

import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()   # 声明创建一个对象CookieJar()

handler = urllib .request.HTTPCookieProcessor(cookie)   # 构建一个请求

opener = urllib.request.build_opener(handler)    # 使用build_opener()构建一个Opener

response = opener.open('https://www.baidu.com')

for item in cookie:            # cookie是以字典的形式存在
    print(item.name+" = "+item.value)