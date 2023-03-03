# 制作一个简单的play fair密码

"""
playfair密码是将密钥去重以后填到一个5*5的矩阵中
再将剩余的字母表里面的字母依次填到矩阵剩余的位置里面，
对明文进行加密的时候遇到连续两个相同的字母，则在他们之间插入一个X(大写),
其次明文数组的因该为整数，否则末尾加X以达到两两配对
"""
# 约定I,J占同一个位置
# 在补充和添加的字符均为X

import numpy as np

# 字母表中把I,J视为同一个字母
ALPHABET = ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z"]


# 获取密钥字母列表
def get_key():
    """
    获取密钥
    :return: 返回密钥数组
    """
    key = input('请输入密钥').upper()
    # 密钥去空格获得字母列表
    list_key = list(key.strip().replace(' ', ''))
    # 去除列表中重复的字母
    list_key1 = []
    for item in list_key:
        if item not in list_key1:
            # 将密钥中的I,J视为同一个字母
            if item != 'J':
                list_key1.append(item)
    # print(list_key1)    # 密钥原来的字符
    # 将字母表中剩余的字符全部插入字符数组中
    for item in ALPHABET:
        if item not in list_key1:
            list_key1.append(item)

    fin_list_key = np.array(list_key1).reshape(5, 5)
    # print(fin_list_key)  # 用于测试作用
    return fin_list_key


# 获取并转换为列表明文
def clear_text():
    """
    :return:
    """
    text = input('请输入要加密的明文').upper()
    # 将明文字符串转换为列表
    list_text = list(text.strip().replace(' ', ''))  # 去除空格以后的列表
    # 将明文列表进行一系列的处理
    # 先将列表中为'J'的字符转化为'I'
    for j in range(len(list_text)):
        if list_text[j] == 'J':
            list_text[j] = 'I'
    # 如果有两个连续的字符相同，就在其中插入一个'X'
    for i in range(len(list_text) - 1):
        if list_text[i] == list_text[i + 1]:
            list_text.insert(i + 1, 'X')
    # 如果列表为奇数个,则在列表的后面加上'X'
    if len(list_text) % 2 != 0:
        list_text.append('X')
    # print('要加密的明文为：', list_text)
    return list_text


# 进行两个一组的位置变换
def exchange_alp(list_math, list_key):
    # 将分组后的字符下标存储在列表中两个列表中，加密专用
    list_path_x = []
    list_path_y = []
    for first in range(5):
        for second in range(5):
            if list_key[first][second] == list_math[0]:
                list_path_x.append(first)
                list_path_y.append(second)
    for first in range(5):
        for second in range(5):
            if list_key[first][second] == list_math[1]:
                list_path_x.append(first)
                list_path_y.append(second)
    # 同行就就向后移动一位
    if list_path_x[0] == list_path_x[1]:
        list_path_y[0] = (list_path_y[0] + 1) % 5
        list_path_y[1] = (list_path_y[1] + 1) % 5
    # 如果同列就向下移动一位
    elif list_path_y[0] == list_path_y[1]:
        list_path_x[0] = (list_path_x[0] + 1) % 5
        list_path_x[1] = (list_path_x[1] + 1) % 5
    # 不同行不同列就用同行和不同列组成新的位置
    else:
        a = list_path_y[1]
        list_path_y[1] = list_path_y[0]
        list_path_y[0] = a
    cipher = [list_key[list_path_x[0]][list_path_y[0]],
              list_key[list_path_x[1]][list_path_y[1]]]
    return cipher


def exchange_alp1(list_math, list_key):
    """
    解密专用
    :param list_math: 传入是数组
    :param list_key:  密钥
    :return: 明文
    """
    list_path_x = []
    list_path_y = []
    for first in range(5):
        for second in range(5):
            if list_key[first][second] == list_math[0]:
                list_path_x.append(first)
                list_path_y.append(second)
    for first in range(5):
        for second in range(5):
            if list_key[first][second] == list_math[1]:
                list_path_x.append(first)
                list_path_y.append(second)

    # 同行就就向前移动一位
    if list_path_x[0] == list_path_x[1]:
        list_path_y[0] = (list_path_y[0] - 1) % 5
        list_path_y[1] = (list_path_y[1] - 1) % 5

    # 如果同列就向上移动一位
    elif list_path_y[0] == list_path_y[1]:
        list_path_x[0] = (list_path_x[0] - 1) % 5
        list_path_x[1] = (list_path_x[1] - 1) % 5
    # 不同行不同列就用同行和不同列组成新的位置
    else:
        a = list_path_y[1]
        list_path_y[1] = list_path_y[0]
        list_path_y[0] = a

    cipher = [list_key[list_path_x[0]][list_path_y[0]],
              list_key[list_path_x[1]][list_path_y[1]]]

    return cipher


# 进行加密算法(密钥，明文)
def encry_playfair(list_key, list_text):
    """
    将明文进行加密
    :param list_key:密钥
    :param list_text:明文
    :return:密文
    """
    # 对明文进行分组
    cipher_list = []
    for i in range(len(list_text)):
        if i % 2 == 0 and i + 1 <= len(list_text) - 1:
            cut_list_text = [list_text[i], list_text[i+1]]
            # 用来存储分组密文,加密
            cip_list = exchange_alp(cut_list_text, list_key)
            # 将所有密文合在一起
            cipher_list.extend(cip_list)

    return "".join(cipher_list)


# playfair密码解密
def decry_playfair(list_key):
    """
    输入密文解密
    :return: 明文
    """
    print('请输入密文：')
    cle_text = input().upper()
    list_text = list(cle_text.strip().replace(' ', ''))  # 去除空格以后的列表
    # 两两一个分组
    cipher_list = []
    for i in range(len(list_text)):
        if i % 2 == 0 and i + 1 <= len(list_text) - 1:
            cut_list_text = [list_text[i], list_text[i + 1]]
            # 用来存储分组密文,解密
            cip_list = exchange_alp1(cut_list_text, list_key)
            # 将所有密文合在一起
            cipher_list.extend(cip_list)
    return "".join(cipher_list)


# 调用实例
if __name__ == "__main__":
    while True:
        print("加密e,解密d,退出b")
        a = str(input())
        if a == 'e':
            key = get_key()
            text = clear_text()
            cip = encry_playfair(key, text)
            print("加密成功,密文为：", cip)
        elif a == 'd':
            key = get_key()
            cip = decry_playfair(key)
            print("解密成功，明文为：", cip)
        elif a == 'b':
            break
        else:
            print('输入不符合规则，请重新输入！')










