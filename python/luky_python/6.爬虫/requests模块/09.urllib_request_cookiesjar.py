# 通过http.cookiejar来保存登录成功后的cookie信息，通过HTTPCookieProcessor来处理HTTP Cookie请求

import urllib.request
import urllib.parse
import http.cookiejar

# 找到网页的登录url
login_url = 'http://chipscoco.com/zb_users/plugin/YtUser/cmd.php?act=verify'

# 模拟游览器登录
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

# 构建一个请求头
headers = {"User-Agent": user_agent}

# 构造一个form data， username为登录的用户名，edtPassWord为加密后的登录密码
form_data = {"username": "test123456", "edtPassWord": "10a25ef3bc5238dbcadcaf6e5ccedb5a"}

# 对字典对象进行url编码，由于Request中的data需要转换为bytes类型，因此还需要执行encode方法
login_form_data = urllib.parse.urlencode(form_data).encode('utf-8')
res = urllib.request.Request(login_url, headers=headers, data=login_form_data)

# 构造一个cookiejar对象来保存cookie信息
cookiejar = http.cookiejar.CookieJar()  # 对象
cookie_processor = urllib.request.HTTPCookieProcessor(cookiejar)
opener = urllib.request.build_opener(cookie_processor)

opener.open(res)
for item in cookiejar:
    print(item.name + "=" + item.value)
