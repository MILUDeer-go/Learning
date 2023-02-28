#  将请求到的cookies保存在文件中


import http.cookiejar, urllib.request

filename = 'cookies.txt'
# 生成文件时候使用的MozillaCookieJar()来构建cookies
# 这时 CookieJar 就需要换成问MozillaCookieJar ，它在生成文件时会用到，是 CookieJar 的子类，可
# 以用来处理 Cookies 和文件相关的事件，比如读取和保存 Cookies ，可以将 Cookies 保存成 Mozilla
# 浏览器的 cookies 格式
cookie = http.cookiejar.MozillaCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)