# SM2数据加密
# SM2密钥生成是指生成SM2算法的密钥对的过程，该密钥对包括私钥与之对应的公钥。 其中，私钥长度为256位，公钥长度为512位。
from gmssl import sm2, func
from gmssl.utils import PrivateKey

'''
密钥生成方法二：
# 生成公私钥
class Generator_SM2_Key(sm2.CryptSM2):
    def __init__(self, private_key=None, public_key=None, ecc_table=sm2.default_ecc_table):
        super().__init__(private_key, public_key, ecc_table)

    def get_private_key(self):
        if self.private_key is None:
            self.private_key = func.random_hex(self.para_len)  # d∈[1, n-2]
        return self.private_key

    def get_public_key(self):
        if self.public_key is None:
            self.public_key = self._kg(int(self.get_private_key(), 16), self.ecc_table['g'])  # P=[d]G
        return self.public_key
def key_gen():
    key = Generator_SM2_Key()
    pk = key.get_public_key()
    sk = key.get_private_key()
    return pk, sk
'''

# key generation
def key_gen():
    sk = PrivateKey()
    pk = sk.publicKey()
    return pk.toString(compressed=False), sk.toString()

# SM2 encryption
def SM2_enc(plaintext,pk,sk):
    # complete this function
    #初始化
    sm2_crypt = sm2.CryptSM2(public_key=pk,private_key=sk)
    ciphertext = sm2_crypt.encrypt(plaintext)
    return ciphertext

# SM2 decryption
def SM2_dec(ciphertext,pk,sk):
    # complete this function
    sm2_crypt = sm2.CryptSM2(public_key=pk,private_key=sk)
    plaintext = sm2_crypt.decrypt(ciphertext)
    return plaintext

# SM2 experiment with string
def exp_SM2_str(plaintext):
    # complete this function
    # 获取公钥私钥
    pk_str, sk_str = key_gen()
    print('====================加密开始====================')
    print('公钥：', pk_str)
    print('私钥：', sk_str)
    # 加密
    print('====================SM2_enc====================')
    ciphertext = SM2_enc(plaintext,pk_str,sk_str)
    # print(type(ciphertext))
    print('SM2加密结果为：\n', ciphertext.hex()[2:])
    print('====================SM2_dec====================')
    plaintext_end = SM2_dec(ciphertext,pk_str,sk_str)
    plaintext_end = str(plaintext_end,encoding="utf8")
    print('SM2解密结果为：', plaintext_end)
    print('================加解密过程结束！=================')

if __name__ == '__main__':
    # complete this function
    data = str(input('请输入要加密的数据：'))
    data = bytes(data,encoding="utf8")
    exp_SM2_str(data)