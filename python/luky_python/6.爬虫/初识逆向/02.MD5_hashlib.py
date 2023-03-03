import hashlib

# 定义变量password表示用户密码
password = "simple"

# md5方法接收的数据类型为字节类型，需执行字符串对象的encode方法进行转换
md5_obj = hashlib.md5(password.encode())
print(md5_obj)
# 获取密码的十六进制散列
password_hash = md5_obj.hexdigest()
print(password_hash)