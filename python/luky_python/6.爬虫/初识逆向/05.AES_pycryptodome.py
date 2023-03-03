# AES常用的加密模式有ECB和CBC。密钥长度必须为16字节，24字节，或者32字节，且加密的数据长度必须是16的倍数。
# 在Python中使用AES加密需安装pycryptodome模块

from Crypto.Cipher import AES
import hashlib, base64

# 以md5的散列值作为密钥
AES_KEY = hashlib.md5("qwert".encode()).hexdigest().encode()

# 待加密明文的长度需为16的倍数
text = ("1" * 16).encode()

# 执行AES模块的new方法构造一个AES cipher对象
# 再执行AES cipher对象的encrypt方法对数据进行加密
en_text = base64.b64encode(AES.new(AES_KEY, AES.MODE_ECB).encrypt(text))
print(en_text)
"""
之所以在AES加密以后再对密文进行base64编码，是为了消除某些特殊字符的影响
"""