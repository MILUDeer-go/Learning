# SM4数据加密encrypt_ecb、 decrypt_ecb、 encrypt_cbc、 decrypt_cbc等函数用于加密解密
import random
from gmssl import func
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

# generate 128 bit random key
# type of key is bytes
def key_gen():
    # complete this function
    key = []
    while len(key) < 128:
        key.append(random.randint(0,1))
    return key

# generate 128 bit random iv
# type of iv is bytes
def iv_gen():
    # complete this function
    iv = []
    while len(iv) < 128:
        iv.append(random.randint(0,1))
    return iv

# SM4 ecb mode encryption
# types of plaintext, key and ciphertext are bytes
def SM4_ecb_enc(plaintext,key):
    # complete this function
    # 初始化
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key,SM4_ENCRYPT)
    ciphertext = crypt_sm4.crypt_ecb(plaintext)

    return ciphertext

# SM4 ecb mode decryption
# types of plaintext, key and ciphertext are bytes
def SM4_ecb_dec(ciphertext,key):
    # 初始化
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key, SM4_DECRYPT)
    plaintext = crypt_sm4.crypt_ecb(ciphertext)
    # byte转字符串类型
    plaintext = str(plaintext,encoding='utf8')
    return plaintext

# SM4 cbc mode encryption
# types of plaintext, iv, key and ciphertext are bytes
def SM4_cbc_enc(plaintext,iv,key):
    # complete this function
    # 初始化
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key,SM4_ENCRYPT)
    ciphertext = crypt_sm4.crypt_cbc(iv, plaintext)

    return ciphertext

# SM4 cbc mode decryption
# types of plaintext, iv, key and ciphertext are bytes
def SM4_cbc_dec(ciphertext,iv,key):
    # complete this function
    # 初始化
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key, SM4_DECRYPT)
    plaintext = crypt_sm4.crypt_cbc(iv, ciphertext)
    # byte转字符串类型
    plaintext = str(plaintext,encoding='utf8')

    return plaintext

# SM4 experiment with string
# type of plaintext is str
def exp_SM4_str(plaintext):
    # complete this function
    key = key_gen()
    key_str = hex(int(''.join(str(i) for i in key_gen()), 2))[2:]
    iv = iv_gen()
    iv_str = hex(int(''.join(str(i) for i in iv_gen()), 2))[2:]

    # 将密钥列表转换为byte类型
    key_byte = func.list_to_bytes(key)
    # 将字符串转换为byte类型
    plaintext_byte = bytes(plaintext, encoding="utf8")
    # 将iv列表转化为byte类型
    iv_byte = func.list_to_bytes(iv)

    print("==============SM4-ecb-mode==============")
    print(f"key:{key_str}")
    ciphertext1 = SM4_ecb_enc(plaintext_byte, key_byte)
    plaintext1 = SM4_ecb_dec(ciphertext1, key_byte)
    print(f"encrypt values:{ciphertext1.hex()}") # 打印bytes的16进制数据
    print(f"decrypt values:{plaintext1}")

    print("==============SM4-cbc-mode==============")
    print(f"key:{key_str}")
    print(f"iv:{iv_str}")
    ciphertext2 = SM4_cbc_enc(plaintext_byte, iv_byte, key_byte)
    plaintext2 = SM4_cbc_dec(ciphertext2, iv_byte, key_byte)
    print(f"encrypt values:{ciphertext2.hex()}")
    print(f"decrypt values:{plaintext2}")

# SM4 experiment with file
# type of file_path is str
def exp_SM4_file(file_path):
    # complete this function
    # 以字节流读取数据
    with open(file_path, 'rb') as f:
        plaintext_bytes = f.read()
    f.close()
    key = key_gen()
    key_str = hex(int(''.join(str(i) for i in key_gen()), 2))[2:]
    iv = iv_gen()
    iv_str = hex(int(''.join(str(i) for i in iv_gen()), 2))[2:]

    # 将密钥列表转换为byte类型
    key_byte = func.list_to_bytes(key)
    # 将iv列表转化为byte类型
    iv_byte = func.list_to_bytes(iv)

    print("==============SM4-ecb-mode==============")
    print(f"key:{key_str}")
    ciphertext1 = SM4_ecb_enc(plaintext_bytes, key_byte)
    plaintext1 = SM4_ecb_dec(ciphertext1, key_byte)
    file1 = 'file_enc_ecb.txt'
    with open(file1, 'w') as f:
        f.write(ciphertext1.hex()[2:])
    f.close()
    print(f"encrypt file save as:{file1}")
    file2 = 'file_dec_ecb.txt'
    with open(file2,'w') as f:
        f.write(plaintext1)
    f.close()
    print(f"encrypt file save as:{file2}")

    print("==============SM4-cbc-mode==============")
    print(f"key:{key_str}")
    print(f"iv:{iv_str}")
    ciphertext2 = SM4_cbc_enc(plaintext_bytes, iv_byte, key_byte)
    plaintext2 = SM4_cbc_dec(ciphertext2, iv_byte, key_byte)
    file3 = 'file_enc_cbc.txt'
    with open(file3, 'w') as f:
        f.write(ciphertext2.hex()[2:])
    f.close()
    print(f"encrypt file save as:{file3}")
    file4 = 'file_dec_cbc.txt'
    with open(file4 , 'w') as f:
        f.write(plaintext2)
    f.close()
    print(f"encrypt file save as:{file4}")

if __name__ == '__main__':
    # complete this function
    print("请输入加密的数据或文件（file）")
    plain = str(input())
    if plain == 'file':
        print("请输入文件路径")
        file_path = input()
        exp_SM4_file(file_path)
    else:
        exp_SM4_str(plain)
    
    
