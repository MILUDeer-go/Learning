# base64编码经常用于HTTP请求中，对请求参数进行编码。
import base64

password = 'qwdefg'
# encode方法接收的参数类型必须为字节类型
# 所以需要执行字符串的encode方法，将其转换为字节类型
password_b64 = base64.b64encode(password.encode('utf-8'))
print(password_b64)

# 解码端通过b64decode来解码,参数同样为字节类型:
password_d = base64.b64decode(password_b64)
print(password_d)