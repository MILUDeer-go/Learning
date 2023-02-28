# Caesar Cipher
"""
凯撒密码实现是字符移动n位后组成的新字符，在每个字符的基础上
ord()+n % 26 来实现字符的代替
"""

MAX_KEY = 26


# 获取关键词

def getMode():
    while True:
        print('请选择加密，解密，或者暴力破解')
        print('加密：encrypt(e)')
        print('解密：decrypt(d)')
        print('暴力破解：brute(b)')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('请再输入上面的字母或单词')


# 获取明文
def getMessage():
    print("请输入信息：")
    return input()

# 获取移动的个数
def getKey():
    key = 0
    while True:
        print('请输入密钥数字（1-%s）' % (MAX_KEY))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY):
            return key

# 获取明文或者密文
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


if __name__ == "__main__":
    mode = getMode()
    message = getMessage()
    if mode[0] != 'b':
        key = getKey()

    print('你要加密或解密的信息是：')
    if mode[0] != 'b':
        print(getTranslatedMessage(mode, message, key))
    else:
        for key in range(1, MAX_KEY + 1):
            print(key, getTranslatedMessage('decrypt', message, key))
