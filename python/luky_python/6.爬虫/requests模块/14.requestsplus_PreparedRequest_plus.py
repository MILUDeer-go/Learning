"""
直接构造PreparedRequest对象，以便在下文代码中对对象进行复用。
其不足在于直接通过Request.prepare方法构造的是一个无状态的PreparedRequest对象，不会在会话中保持cookie。
如需构造带状态的PreparedRequest，应当使用Session对象的prepare_request方法
"""
import requests
from requests import Request

# 设置登录地址
login_url = 'http://chipscoco.com/zb_users/plugin/YtUser/cmd.php?act=verify'
# 构造登录密码表单
form_data = {"username":"test", "edtPassWord":"47ec2dd791e31e2ef2076caf64ed9b3d"}

re = Request('POST', url=login_url, data=form_data)

with requests.Session() as s:

    # 获取一个带有状态的PreparedRequest
    prepped = s.prepare_request(re)
    # 直接使用Session对象的send方法来发起请求
    s2 = s.send(prepped)
    print(s2.headers)




