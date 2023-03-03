# LWPCookieJar 同样可以读取和保存 Cookies ，但是保存的格式和 MozillaCookieJar 样，
# 它会保存成 libwww-perl(LWP）格式的 Cookies 文件

import http.cookiejar, urllib.request

filename = 'LWPC_cookies.txt'
cookie = http.cookiejar.LWPCookieJar(filename)    # 使用LWPCookieJar()函数构建新的cookies格式

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 下面读取文件并处理
# 这里调用 load （）方法来读取本地的 Cookies 文件，获取到了 Cookies 的内容 不过前
# 提是我们首先生成了 LWPCookiesJar 格式的 Cookies ，并保存成文件，然后读取 Cookies 之后使用同样
# 的方法构建 Handler Opener 即可完成操作
# 运行结果正常的话，会输出百度网页的源代码

cookies = http.cookiejar.LWPCookieJar()
cookies.load("LWPC_cookies.txt", ignore_discard=True, ignore_expires=True)  # 对cookies对象使用load（）函数打开文件
# 使用文件里面的cookies来构建请求对象
handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
# 输出结果,百度页面的源码
print(response.read().decode('utf-8'))
