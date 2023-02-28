# post方法用来提交数据给服务器，直接将字典类型的实参通过data进行传递，或者将json格式的数据通过json参数来进行传递。
# 代码实例-模拟登录chipscoco

import requests

# 以下为薯条老师博客的登录url
login_url = 'http://chipscoco.com/zb_users/plugin/YtUser/cmd.php?act=verify'
# 构造一个form data， username为登录的用户名，edtPassWord为加密后的登录密码
form_data = {"username": "test", "edtPassWord": "47ec2dd791e31e2ef2076caf64ed9b3d"}
r = requests.post(login_url, data=form_data)

# cookies是一个RequestsCookieJar对象
for item in r.cookies:
    print(item.name + '=' + item.value)