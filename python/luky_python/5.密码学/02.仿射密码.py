# 仿射密码
"""
仿射密码是凯撒密码另一种变式，将每个字符按照
C=E([a,b],p) = (ap+b)mod 26的形式进行加密
字母的ASCII码为：a-z:97-122,A-Z:65-90
p的值为26以内与26互素的数
p'为a的逆，解密形式为a=E([C,b],p')=(cp'-(p‘b)mod 26)mod 26
"""
# 加密
def encrypt_Caesar():
    print("欢迎来到仿射密码")
    print("请输入要加密的信息:", end='')
    message = input()
    print('请从以下数字选取第一个密钥（1，3，5，7，9，11，13，15，17，19，21，23，25）：')
    key1 = int(input())
    print('请从0-26选取第二个密钥：')
    key2 = int(input())

    encrypt = ''
    for symbol in message.lower():

        if symbol.isalpha():
            num = ((ord(symbol)-97)*key1 + key2) % 26
            num1 = 97 + num

            encrypt += chr(num1)
        else:
            encrypt += symbol
    print(f"密钥 {key1} 和 {key2} 加密后为：")
    print(encrypt.upper())
    
# 解密
def decrypt_Caesar():
    print("欢迎来到仿射密码")
    print("请输入要解密的信息:", end='')
    message = input()
    print('请从以下数字选取第一个密钥（1，3，5，7，9，11，13，15，17，19，21，23，25）：')
    key1 = int(input())
    print('请从选取第二个密钥：')
    key2 = int(input())
    # 用字典表示仿射密码对应第一个密钥的逆
    a1 = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}

    decrypt = ''
    for symbol in message.lower():

        if symbol.isalpha():
            num = ((ord(symbol) - 97) * a1[key1] - (a1[key1]*key2) % 26) % 26
            num1 = 97 + num

            decrypt += chr(num1)
        else:
            decrypt += symbol
    print(f"密钥 {key1} 和 {key2} 解密后为：")
    print(decrypt.upper())


# 调用实例
if __name__ == "__main__":
    encrypt_Caesar()
    decrypt_Caesar()
