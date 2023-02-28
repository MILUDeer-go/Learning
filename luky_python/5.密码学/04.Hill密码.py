# Hill 密码
"""
Hill 密码是简单的多表代替密码，首先将按照字符串3个一组来分组，将每个字符与
3*3的矩阵相乘，得到新的字符，以此来加密，要注意:字符串如果不是3的倍数，就在
字符串的最后加上x,还有用来做密钥的3*3的行列式的值不能为0；为零不可以作为密钥
"""

# 加密的密钥矩阵
K_LIST = [[17, 17, 5],
          [21, 18, 21],
          [2, 2, 19]]

K_LIST1 = [[4, 9, 15],
           [15, 17, 6],
           [24, 0, 17]]

# 26个字母列表，方便找出下标
ALPHABET = ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]


def get_index(alphabet):
    """
    获取字母在字母表中对应的位置（下标）
    :param alphabet: 明文
    :return: 下标
    """
    alphabet = alphabet.upper()
    return ALPHABET.index(alphabet)


def deal_index(list_index, K_List):
    """
    加密处理
    :param list_index: 每一组明文字母的下标
    :return: 加密后的密文下标
    """
    deal_list = [0, 0, 0]
    for i in range(len(K_List)):
        for j in range(len(K_List[i])):
            deal_list[i] += list_index[j] * K_List[j][i]
        deal_list[i] = (deal_list[i] % 26)
    return deal_list


def get_alphabet(deal_list):
    """
    通过字母下标获取对应的字母
    :param deal_list: 下标列表
    :return:  返回的密文字母列表
    """
    cipher_list = []
    for i in deal_list:
        cipher_list.append(ALPHABET[i])
    return cipher_list


def encrytion(clear_text):
    """
    加密时候调用的函数
    :param clear_text:  输入的明文
    :return: 加密后的密文
    """
    # 转换字符为列表并消除空格
    list_clear_text = list(clear_text.strip().replace(" ", ""))
    # 明文3个一组,不足的补X(大写)
    for i in range(len(list_clear_text)):
        if i % 3 == 0 and i + 2 > len(list_clear_text) - 1:
            if i + 1 > len(list_clear_text) - 1:
                list_clear_text.insert(i + 1, "X")
            list_clear_text.insert(i + 2, "X")


    cipher_list = []  # 用来存入密文
    # 明文3个一组,找出每组在字母表中的位置（用列表保存）
    for i in range(len(list_clear_text)):
        if i % 3 == 0 and i + 2 <= len(list_clear_text) - 1:
            x = get_index(list_clear_text[i])
            y = get_index(list_clear_text[i + 1])
            z = get_index(list_clear_text[i + 2])
            list_index = [x, y, z]

            # 调用deal_index()函数进行3个字母位置加密
            deal_list = deal_index(list_index, K_LIST)

            # 返回一组密文字母列表
            part_cipher_list = get_alphabet(deal_list)

            # 存储返回的每一组列表
            cipher_list.extend(part_cipher_list)

    return "".join(cipher_list)  # 使用join()方法将序列中的字符生成新的字符串


def decryption(cipher_text):
    """
    # 输入密文进行解密
    :param cipher_text: 密文
    :return: 明文
    """
    # 转换密文字符为列表
    list_cipher_text = list(cipher_text.strip())

    clear_list = []     # 用来存入解密后的明文

    # 密文3个一组,找出每组在字母表中的位置（用列表保存）
    for i in range(len(list_cipher_text)):
        if i % 3 == 0 and i + 2 <= len(list_cipher_text) - 1:
            x = get_index(list_cipher_text[i])
            y = get_index(list_cipher_text[i + 1])
            z = get_index(list_cipher_text[i + 2])
            list_index = [x, y, z]

            # 调用deal_index()函数进行3个字母位置解密
            deal_list = deal_index(list_index, K_LIST1)
            # print(deal_list)

            # 返回一组明文字母列表
            part_clear_list = get_alphabet(deal_list)
            # print(part_clear_list)
            # print('='*40)

            # 存储返回的每一组列表
            clear_list.extend(part_clear_list)

    return "".join(clear_list)  # 使用join()方法将序列中的字符生成新的字符串





if __name__ == '__main__':
    while True:
        print('欢迎来到HILL密码')
        choice = input("请输入e加密或者d解密,输入b退出：")
        if choice == "e":
            clear_text = input("请输入明文：")
            print("加密成功！ 密文为：%s" % encrytion(clear_text))
        if choice == "d":
            cipher_text = input("请输入密文")
            print("解密成功！ 明文为：%s" % decryption(cipher_text))
        if choice == "b":
            print("下次再见")
            break


