# 跨请求保持登录cookie

"""
保持cookie:通过requests中的Session对象，可以在同一个会话的所有请求间保持cookie。
构造Session对象时，通常使用with来进行上下文管理，并通过Session对象的get或post方法来发起请求。
requests中的会话无法保持请求级别的参数，即后面的请求方法不能保持前面请求方法中的参数.
"""

import requests

# 以下为薯条老师博客的登录url
login_url = 'http://chipscoco.com/zb_users/plugin/YtUser/cmd.php?act=verify'
page_url = 'http://chipscoco.com/?id=9'

# 构造一个form data， username为登录的用户名，edtPassWord为加密后的登录密码
form_data = {"username": "test", "edtPassWord": "47ec2dd791e31e2ef2076caf64ed9b3d"}

# 构造一个Session对象， 同一个会话的所有请求保持相同的cookie
with requests.session() as s:
    # 直接使用Session对象的post方法来发起请
    s.post(login_url, data=form_data)
    # get请求使用的是 发起post请求后服务端响应的cookie信息
    s.get(page_url)
    print(s.headers)
