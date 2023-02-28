# Vigenere密码
"""
Vigenere密码是最简单的多表代替密码，代替规则与凯撒密码的代替表相同。
密钥不是相同的，而是一个字符串位置的不断重复来和来使明文移动密钥对应的
字符的位数来实现加密。
加密的一般方程为：Ci = (Pi + Ki mod m) mod 26,pi为要加密的字符，
ki为对应的密钥,m为密钥的长度。
解密一般方程为：Pi = (Ci - Ki mod m) mod 26
"""
def encrypt_Vigenere():
    print("欢迎来到维吉尼亚密码加密：")
    print('请输入你要加密的信息')
    message = input().lower()
    print('请输入密钥字符串：')
    key1 = input().lower()

    List_key1 = []
    List_message = []

    # 将密钥转换为0-26的数字存储在列表中
    for i in range(len(key1)):
        List_key1.append(ord(key1[i]) - 97)
    # print(List_key1)
    # 将明文也转换为数字存储在列表中
    for j in range(len(message)):
        List_message.append(ord(message[j]) - 97)
    # print(List_message)

    # 实现维基密码的逻辑上的相加
    num1 = []

    for num in range(len(message)):
        num1.append(97 + (List_message[num] + List_key1[num % (len(key1))]) % 26)

    res = ""
    # 在将字符转换为字母
    for k in range(len(num1)):
        res += chr(int(num1[k]))
    print("解密结果为", res.upper())

def decrypt_Vigenere():
    print("欢迎来到维吉尼亚密码解密：")
    print('请输入你要解密密的信息')
    message = input().lower()
    print('请输入密钥字符串：')
    key1 = input().lower()

    List_key = []
    List_message1 = []

    # 将密钥转换为0-26的数字存储在列表中
    for i in range(len(key1)):
        List_key.append(ord(key1[i]) - 97)

    # 将明文也转换为数字存储在列表中
    for j in range(len(message)):
        List_message1.append(ord(message[j]) - 97)
        # 实现维基密码的逻辑上的相加

    num1 = []
    for num in range(len(message)):
        num1.append((List_message1[num] - List_key[num % len(key1)]) % 26 + 97)
    res = ""
    # 在将字符转换为字母
    for k in range(len(num1)):
        res += chr(int(num1[k]))
    print("解密结果为", res.upper())

# 调用实例
if __name__ == "__main__":
    encrypt_Vigenere()
    print("")
    decrypt_Vigenere()