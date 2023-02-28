# 直接构造PreparedRequest

"""
在调用requests的get方法或post等方法时，requests在内部实现中会先构造一个Request对象，
然后再通过Request的prepare方法构造一个PreparedRequest对象。
"""
import requests
from requests import Request

login_in = "http://chipscoco.com/zb_users/plugin/YtUser/cmd.php?act=verify"
# 构造一个form data， username为登录的用户名，edtPassWord为加密后的登录密码
form_data = {"username": "test", "edtPassWord": "47ec2dd791e31e2ef2076caf64ed9b3d"}

re = Request('POST', url=login_in, data=form_data)

# 构造一个PreparedRequest对象
prepped = re.prepare()
with requests.Session() as s:
    # 直接使用Session对象的send方法来发起请求
    s.send(prepped)
    print(s.headers)
