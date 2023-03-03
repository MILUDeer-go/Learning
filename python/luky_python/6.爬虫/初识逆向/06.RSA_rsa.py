
import rsa
import hashlib
import json

# 执行rsa模块的newkeys方法来生成公钥和私钥
public_key, private_key = rsa.newkeys(1024)

# 构造字典对象cert,表示cert证书
cert = {
    "Version": "v3",
    "Serial Number": 126822703,
    "Signature Algorithm": "sha256",

    # (1) 通过PublicKey的save_pcks1方法将公钥转换为字节类型
    # (2) 通过PublicKey的load_pcks1方法将字节类型转换为PublicKey对象
    "PublicKey": public_key.save_pkcs1().decode("utf-8")
}

# json.dumps	将 Python 对象编码成 JSON 字符串
info = json.dumps(cert, ensure_ascii=False).encode("utf-8")

# 执行rsa模块的sign方法+RSA私钥+sha256散列算法生成一个加密签名
cert["Signature"] = rsa.sign(info, private_key, "SHA-256")

# 通过rsa模块的verify方法以及RSA公钥来对加密签名进行验证
# 如果验证失败会抛出异常
rsa.verify(info, cert["Signature"], rsa.PublicKey.load_pkcs1(cert["PublicKey"].encode("utf - 8")))