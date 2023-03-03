# 8. 获取与发送cookies
# 服务端的响应中如果包含cookie信息，可通过Response对象的cookies进行访问。
# 在爬虫程序的开发场景中，很多情况下需要发送cookie给服务端，以维持状态信息，
# 此时可以通过RequestsCookieJar对象的set方法构造一个cookie:
# set(self, name, value, **kwargs)
# name表示字段名，value表示字段值，可以在关键字参数中使用domain来传递请求的域名，
# 用path参数来指定请求的路径。

import requests
# 以下为薯条老师博客的登录url
url = 'http://chipscoco.com/zb_users/plugin/YtUser/cmd.php?act=verify'

# 构造一个form data， username为登录的用户名，edtPassWord为加密后的登录密码
form_date = {"username": "test", "edtPassWord": "47ec2dd791e31e2ef2076caf64ed9b3d"}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'}
r = requests.post(url, headers=headers, data=form_date)

jar = requests.cookies.RequestsCookieJar()
# 主要是演示set方法的使用
for item in r.cookies:
    jar.set(item.name, item.value)


# 待抓取的在线教程地址
page_url = 'http://www.chipscoco.com'
payload = {'id': 9}
# 通过关键字参数cookies来传递cookie
r = requests.get(page_url, params=payload, cookies=jar)
print(r.text)
