# 捕获url异常

import urllib.parse
from urllib.error import HTTPError
# 以下url并不存在，读者可使用tornado快速搭建一个本地服务器来进行测试
url = 'http://httpbin.org/'      # 没有使用post方法提交表单
values = {'name': 'chipscoco', 'password': 'forget'}

data = urllib.parse.urlencode(values)
# 必须传递字节流类型
data = data.encode('utf-8')
try:
    response = urllib.request.urlopen(url, data=data)
except HTTPError as e:
    print(e.code, e.reason)

