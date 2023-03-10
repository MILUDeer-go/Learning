# 128位AES分组加密

# 加解密过程中需要使用的矩阵
# 加密代换的S盒
S_FORWORD = [
 [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
 [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
 [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
 [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
 [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
 [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
 [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
 [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
 [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
 [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
 [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
 [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
 [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
 [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
 [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
 [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]

# 解密代换的S盒
S_REVERSE = [
 [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
 [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
 [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
 [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
 [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
 [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
 [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
 [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
 [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
 [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
 [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
 [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
 [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
 [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
 [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
 [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]]

#
RC = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000, 0x20000000,
      0x40000000, 0x80000000, 0x1B000000, 0x36000000]

# 1. 字节代替
# 输入16字节的数据，每个字节的前四位作为行，后4位作为列值，进行查表操作，然后在输出新的16字节
# 加密解密使用不同的矩阵
def IP_Sub(S_Input, flag='0'):
    # S_Input输入16进制的数据
    # 断言判断是否数据输入正确
    assert len(S_Input) == 32
    index = 0
    ret = ""
    while index < 32:
        # 16进制字节第1位为行值row
        row = int(S_Input[index], base=16)
        # 16进制字节第2位为列值col
        col = int(S_Input[index+1], base=16)
        # 输出代换以后的结果result自动会转换为10进制,需要在转换为16进制并移除前面的字符0x,在数组里面是从第0行0列开始的
        if flag == '-1':
            result = hex(S_REVERSE[row][col])[2:].upper()
        else:
            result = hex(S_FORWORD[row][col])[2:].upper()

        while len(result) < 2:
            result = '0' + result
        # 合并输出
        ret += result
        # index加2
        index += 2
    return ret

# 2. 行位移
# 按照顺序从化成4*4的矩阵，第一列为前四个字节，其他的依次排列
# 加密：第一行不变，第二行左移一个字节，第三行左移两个字节，第4行左移3个字节
# 解密：第一行不变，第二行右移一个字节，第三行右移两个字节，第4行左移3个字节
def Row_Sub(R_Input, flag='0'):
    # 先将字符串两两分组转换成列表,进行替换
    assert len(R_Input) == 32
    temp = []
    for i in range(0, 32, 2):
        temp1 = R_Input[i:i+2]
        temp.append(temp1)
    # print(temp)
    # 每一行都移动位置本质上还是一个置换，这里可以使用一个位置数组对应每一个元素的位置
    IP_Site = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]
    IP_site_1 = [0, 13, 10, 7, 4, 1, 14, 11, 8, 5, 2, 15, 12, 9, 6, 3]
    R_Output = []
    if flag == '-1':
        for i in IP_site_1:
            R_Output.append(temp[i])
    else:
        for i in IP_Site:
            R_Output.append(temp[i])
    # print(R_Output)
    return R_Output

# 3. 列混淆
# 这里是将上一步列出的列表先化为4*4的矩阵，因为列混淆本质上是矩阵的乘法
# 加密有加密的矩阵，解密有解密的矩阵，两个矩阵互为逆矩阵，输入矩阵依次左乘两个矩阵就可以还原
# 3.1在GF(2^8)的有限域从乘法
def GF_Cheng(a, b):
    # 输入的a,b是10进制，先转换为二进制
    a_bin = bin(a)[2:]
    while len(a_bin) < 8:
        a_bin = "0" + a_bin
    b_bin = bin(b)[2:]
    while len(b_bin) < 8:
        b_bin = "0" + b_bin
    # print(a_bin, b_bin)
    # 找出左乘矩阵数据的二进制1所在的索引
    a_list = []
    for i in range(len(a_bin)):
        if a_bin[i] == "1":
            a_list.append(i)
    # print(a_list)
    # 对应下标移动不同的位置，如果输入的数据二进制第一位为1，还要在移位之后异或0x1B
    b_list = []  # 用来存储异或之后列表
    for i in a_list:
        res_temp_b = b_bin
        for j in range(0, 8-i-1):
            if res_temp_b[0] == '1':
                # 移位
                temp_b = res_temp_b[1:] + "0"
                # 移位之后异或0x1B
                temp_b = str(bin(int(temp_b, base=2) ^ int('0x1B', base=16))[2:])
                while len(temp_b) < 8:
                    temp_b = "0" + temp_b
                # 更新 res_temp_b的值
                res_temp_b = temp_b
            else:
                temp_b = res_temp_b[1:] + "0"
                while len(temp_b) < 8:
                    temp_b = "0" + temp_b
                # print(temp_b)
                res_temp_b = temp_b
        b_list.append(int(res_temp_b, base=2))

    result = b_list[0]
    # print(b_list)
    for i in range(1, len(b_list)):
        result = result ^ b_list[i]
    # print(bin(result))
    return result

# 4.2 开始列变换算法
def Col_Mix(col_input, flag='0'):
    # 使用行变换的列表转换为矩阵，输入矩阵的转换
    col_Input = [[col_input[0], col_input[4], col_input[8], col_input[12]],
                 [col_input[1], col_input[5], col_input[9], col_input[13]],
                 [col_input[2], col_input[6], col_input[10], col_input[14]],
                 [col_input[3], col_input[7], col_input[11], col_input[15]]]
    # print(col_Input)
    # 加密矩阵
    col_encode = [[0x02, 0x03, 0x01, 0x01],
                  [0x01, 0x02, 0x03, 0x01],
                  [0x01, 0x01, 0x02, 0x03],
                  [0x03, 0x01, 0x01, 0x02]]
    # 解密矩阵
    col_decode = [[0x0E, 0x0B, 0x0D, 0x09],
                  [0x09, 0x0E, 0x0B, 0x0D],
                  [0x0D, 0x09, 0x0E, 0x0B],
                  [0x0B, 0x0D, 0x09, 0x0e]]
    # 存储输出结果
    col_Output = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if flag == '-1':
        abc = col_decode
    else:
        abc = col_encode
    # 进行矩阵的乘法，加密（或解密）矩阵左乘输入矩阵
    for i in range(4):
        for j in range(4):
            temp_list = []
            temp = GF_Cheng(abc[i][j], int(col_Input[j][i], base=16))
            temp_list.append(temp)
            # 对应位置乘积的异或
            result = temp_list[0]
            for x in range(1, len(temp_list)):
                result = result ^ temp_list[x]
            res = str(hex(result)[2:].upper())
            while len(res) < 2:
                res = '0' + res
            col_Output[j][i] = res
    # print(col_Output)
    # 转化为一维数组输出
    col_Output_str = []
    for i in range(4):
        for j in range(4):
            col_Output_str.append(col_Output[j][i])
    return"".join(col_Output_str)

# 4. 轮密钥加密
# 首先输入16字节（128位）的密钥，将4个字节作为一组，按组输出下一列数据
# 如果组数是4的倍数，就w[i-1]进入g函数，输出的数据在与w[i-4]异或，否则直接w[i-1]与w[i-4]异或

# 密钥生成
def Key_Birth(key):
      assert len(key) == 32
      key_list = []
      for i in range(0, len(key), 8):
            key_list.append(key[i:i+8])

      for i in range(0, 40):
            if i % 4 == 0:
                  a = i // 4
                  temp1 = G_Sub(key_list[i+3], a)
                  temp2 = int(str(key_list[i]), base=16) ^ int(temp1, base=16)
                  b = str(hex(int(temp2))[2:].upper())
                  while len(b) < 8:
                        b = "0" + b
                  key_list.append(b)
            else:
                  temp1 = int(key_list[i+3], base=16) ^ int(key_list[i+1], base=16)
                  temp2 = str(hex(temp1)[2:].upper())
                  while len(temp2) < 8:
                        temp2 = '0' + temp2
                  key_list.append(temp2)

      result = []
      for i in range(0, len(key_list), 4):
            temp = ''
            for j in range(i, i+4):
                  temp += key_list[j]
            result.append(temp)
      return result

# g代换输入的数据是4个字节，也就是32位，先做循坏左移1个字节，在做S盒字节置换，之后在于Rcon[i]数组异或
def G_Sub(G_Input, i):
    # 判断输入的16进制字符串数据长度为8
    assert len(G_Input) == 8
    # 左移一个字节
    g_input = G_Input[2:] + G_Input[0:2]
    # print(g_input)
    # s盒置换
    index = 0
    ret = ""
    while index < 8:
        # 16进制字节第1位为行值row
        row = int(g_input[index], base=16)
        # 16进制字节第2位为列值col
        col = int(g_input[index + 1], base=16)
        # 输出代换以后的结果result自动会转换为10进制,需要在转换为16进制并移除前面的字符0x,在数组里面是从第0行0列开始的
        result = str(hex(S_FORWORD[row][col])[2:].upper())
        while len(result) < 2:
            result = '0' + result
        # 合并输出
        ret += result
        # index加2
        index += 2
    # 输出s盒置换以后的数据就用RC异或
    result = int(str(ret), base=16) ^ int(RC[i])
    # print(result)
    # print(hex(result)[2:].upper())
    fina = str(hex(result)[2:].upper())
    while len(fina) < 8:
        fina = '0' + fina
    return fina


if __name__ == '__main__':
    KEY = "F0034A98FABCD423543D4A98FCD42354"
    key_list = Key_Birth(KEY)
    # print("轮密钥：", key_list)
    S_Input = "05ACBD578924F003D4A98FABCD423543"
    # S_Input = '41298A3DF854BFB152EDE230D7B413F'
    print("明文：", S_Input)
    print("初始密钥：", KEY)
    print("="*40)
    # 第一步轮密钥相加
    S_input = hex(int(S_Input, base=16) ^ int(key_list[0], base=16))[2:].upper()
    while len(S_input) < 32:
        S_input = '0' + S_input
    print("初始异或后", S_input)
    # 10轮加密后
    for i in range(10):
        # print(f"第{i+1}轮加密：")
        R_input = IP_Sub(S_input)
        # print("S盒置换后：", R_input)
        while len(R_input) < 32:
            R_input = '0' + R_input
        R_output = Row_Sub(R_input)
        # print("行变换后", "".join(R_output))
        col_mix = Col_Mix(R_output)
        # print("列混淆后：", col_mix)
        S_input = hex(int(S_Input, base=16) ^ int(key_list[i+1], base=16))[2:].upper()
        # print("轮钥加密后：", S_input)
        while len(S_input) < 32:
            S_input = '0' + S_input
    encrp_text = S_input
    print("最终加密结果：", encrp_text)





