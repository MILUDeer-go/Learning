import hashlib
# 定义变量password表示用户密码
password = "simple"

# SHA方法接收的数据类型为字节类型，需执行字符串对象的encode方法进行转换
sha_obj = hashlib.sha1(password.encode())
# 获取密码的十六进制散列
password_hash = sha_obj.hexdigest()
print(password_hash)