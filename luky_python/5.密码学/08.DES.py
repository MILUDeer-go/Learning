# IP 初始置换矩阵
import random
import re

IP_MATRIX = [58, 50, 42, 34, 26, 18, 10, 2,
			 60, 52, 44, 36, 28, 20, 12, 4,
			 62, 54, 46, 38, 30, 22, 14, 6,
			 64, 56, 48, 40, 32, 24, 16, 8,
			 57, 49, 41, 33, 25, 17, 9, 1,
			 59, 51, 43, 35, 27, 19, 11, 3,
			 61, 53, 45, 37, 29, 21, 13, 5,
			 63, 55, 47, 39, 31, 23, 15, 7]

# E扩展置换矩阵
E_MATRIX = [32, 1, 2, 3, 4, 5,
			4, 5, 6, 7, 8, 9,
			8, 9, 10, 11, 12, 13,
			12, 13, 14, 15, 16, 17,
			16, 17, 18, 19, 20, 21,
			20, 21, 22, 23, 24, 25,
			24, 25, 26, 27, 28, 29,
			28, 29, 30, 31, 32, 1]

# S盒 的置换矩阵
S_MATRIX = [(14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
			 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
			 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
			 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13),
			(15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
			 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
			 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
			 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9),
			(10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
			 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
			 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
			 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12),
			(7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
			 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
			 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
			 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14),
			(2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
			 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
			 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
			 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3),
			(12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
			 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
			 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
			 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13),
			(4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
			 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
			 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
			 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12),
			(13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
			 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
			 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
			 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11)]

# P置换的置换矩阵
P_MATRIX = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
			2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

# IP逆置换矩阵
IP_INVERSE_MATRIX = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
					 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
					 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
					 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# 压缩置换矩阵  从56位里选48位
COMPRESS_MATRIXS = [14, 17, 11, 24, 1, 5,
					3, 28, 15, 6, 21, 10,
					23, 19, 12, 4, 26, 8,
					16, 7, 27, 20, 13, 2,
					41, 52, 31, 37, 47, 55,
					30, 40, 51, 45, 33, 48,
					44, 49, 39, 56, 34, 53,
					46, 42, 50, 36, 29, 32]


# 1. 明文初始IP置换
def IP_Reverso(MingWen):
	# 使用断言判断条件是否为正
	assert len(MingWen) == 64

	ret = ""
	# 通过for循环进行IP置换
	for i in IP_MATRIX:
		ret = ret + MingWen[i - 1]
	return ret


# 2.E扩展置换：把置换分组以后的右边32为扩展为48位
def E_Expand(Rn):
	retRn = ""
	for i in E_MATRIX:
		retRn += Rn[i - 1]
	assert len(retRn) == 48
	return retRn


# 3. S盒替换函数：
# 压缩后的密钥与扩展分组异或以后得到48位的数据，将这个数据送入S盒，进行替代运算。
# 替代由8个不同的S盒完成，每个S盒有6位输入4位输出。48位输入分为8个6位的分组，一个分组对应一个S盒，对应的S盒对各组进行代替操作。

# S盒替代运算
def S_Sub(S_Input):
	# 从第二位开始的子串去掉0b
	S_Input = bin(S_Input)[2:]

	while len(S_Input) < 48:
		S_Input = "0" + S_Input

	index = 0
	retstr = ""

	# 以元组为单位，依次在进入0-7元组进行压缩
	for Slist in S_MATRIX:
		# 输入的高低两位做为行数row
		row = int(S_Input[index] + S_Input[index + 5], base=2)
		# 中间四位做为列数L
		col = int(S_Input[index + 1:index + 5], base=2)
		# 得到 result的 单个四位输出
		ret_single = bin(Slist[row * 16 + col])[2:]

		while len(ret_single) < 4:
			ret_single = "0" + ret_single

		# 合并单个输出
		retstr += ret_single
		# index + 6 进入下一个六位输入
		index += 6

	assert len(retstr) == 32

	return retstr


# 4. P盒置换

# S盒代替运算的32位输出按照P盒进行置换
# 最后，P盒置换的结果与最初的64位分组左半部分L0异或，然后左、右半部分交换，接着开始另一轮。

def P_Sub(Ln, S_sub_str, oldRn):
	# P 盒置换
	tmp = ""
	for i in P_MATRIX:
		tmp += S_sub_str[i - 1]
	# P盒置换的结果与最初的64位分组左半部分L0异或
	LnNew = int(tmp, base=2) ^ int(Ln, base=2)
	LnNew = bin(LnNew)[2:]
	while len(LnNew) < 32:
		LnNew = "0" + LnNew
	assert len(LnNew) == 32
	# 左、右半部分交换，接着开始另一轮
	(Ln, Rn) = (oldRn, LnNew)

	return (Ln, Rn)


# 5. IP逆置换

# 末置换是初始置换的逆过程，DES最后一轮后，左、右两半部分并未进行交换，而是两部分合并形成一个分组做为末置换的输入
# 置换后得到密文或者解密的明文

def IP_Inverse(L16, R16):
	tmp = L16 + R16
	retstr = ""
	for i in IP_INVERSE_MATRIX:
		retstr += tmp[i - 1]
	assert len(retstr) == 64
	return retstr


# 密钥生成

# 6. 循环左移位数函数
# 对输入的str 按照shift_count的大小 左移shift_count位 这个函数主要用于子密钥生成
def Shift(str, shift_count):
	try:
		if len(str) > 28:
			raise NameError
	except TypeError:
		pass

	str = str[shift_count:] + str[0:shift_count]
	return str


# 7. 生成子密钥函数
# 初始密钥的生成
def Start_Key():
	res = ''
	while len(res) < 64:
		res += str(random.randint(0, 1))
	return res

# 此函数用来生成子密钥生成16组子密钥用于和扩展分组异或
def Create_Subkey(key):
	# 如果key长度不是64 就退出
	assert len(key) == 64

	# DES的密钥由64位减至56位，每个字节的第8位作为奇偶校验位
	# 把56位 变成 2个28位

	Llist = [57, 49, 41, 33, 25, 17, 9,
			 1, 58, 50, 42, 34, 26, 18,
			 10, 2, 59, 51, 43, 35, 27,
			 19, 11, 3, 60, 52, 44, 36]
	Rlist = [63, 55, 47, 39, 31, 23, 15,
			 7, 62, 54, 46, 38, 30, 22,
			 14, 6, 61, 53, 45, 37, 29,
			 21, 13, 5, 28, 20, 12, 4]

	# 初试生成 左右两组28位密钥
	L0 = ""
	R0 = ""

	for i in Llist:
		L0 += key[i - 1]
	for i in Rlist:
		R0 += key[i - 1]

	assert len(L0) == 28
	assert len(R0) == 28

	# 轮函数生成 48位密钥

	# 定义轮数
	Movetimes = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
	# 定义返回的subKey
	retkey = []
	# 开始轮置换
	for i in range(0, 16):
		# 获取左半边 和 右半边  shift函数用来左移生成轮数
		L0 = Shift(L0, Movetimes[i])
		R0 = Shift(R0, Movetimes[i])
		# 合并左右部分
		mergedKey = L0 + R0

		tempkey = ""
		# 压缩置换矩阵  从56位里选48位
		# 选出48位子密钥
		for i in COMPRESS_MATRIXS:
			tempkey += mergedKey[i - 1]
		assert len(tempkey) == 48
		# 加入生成子密钥
		retkey.append(tempkey)

	return retkey


# DES 算法实现 flag是标志位 当为-1时， 是DES解密， flag默认为0
def DES(text, key, flag="0"):
	# 初始字段
	# IP置换
	InitKeyCode = IP_Reverso(text)
	# 产生子密钥集合
	subkeylist = Create_Subkey(key)
	# 明文分组获得Ln 和 Rn
	Ln = InitKeyCode[0:32]
	Rn = InitKeyCode[32:]

	# 如果是解密的过程 把子密钥数字逆过来 就变成解密过程了
	if flag == "-1":
		subkeylist = subkeylist[::-1]

	for subkey in subkeylist:
		while len(Rn) < 32:
			Rn = "0" + Rn
		while len(Ln) < 32:
			Ln = "0" + Ln

		# 对右边进行E-扩展
		Rn_Expand = E_Expand(Rn)
		# 压缩后的密钥与扩展分组异或后得到48位的数据，将这个数据送入S盒
		S_Input = int(Rn_Expand, base=2) ^ int(subkey, base=2)

		# 进行S盒替代
		S_sub_str = S_Sub(S_Input)

		# P盒置换并且
		# 左、右半部分交换，接着开始另一轮
		(Ln, Rn) = P_Sub(Ln, S_sub_str, Rn)

		# 进行下一轮轮置换

	# 最后一轮之后  左、右两半部分并未进行交换
	# 而是两部分合并形成一个分组做为末置换的输入。
	# 所以要重新置换 一次

	(Ln, Rn) = (Rn, Ln)
	# 末置换得到密文
	re_text = IP_Inverse(Ln, Rn)

	return re_text

# 输入明文转换位字符串
def MW_Exchange(text):
    # 先将明文去掉空格
    text = str(text)
    text = text.upper().replace(' ', '').strip()
    # 去除标点符号
    text = re.sub(r'[^\w\s]', '', text)
    # print(text)
    count = 0
    res = ""
    while count < len(text):
        temp = hex(int(ord(text[count])))[2:]
        while len(temp) < 2:
            temp = '0' + 'temp'
        res += temp
        count += 1
    while len(res) % 8 != 0:
        res += '0'
    return res

# 将解密的数据转化为字符串
def RE_MW(text):
    text = str(text)
    text1 = ''
    for i in range(0, len(text), 2):
        if text[i] != '0' or text[i+1] != '0':
            text1 += text[i]
            text1 += text[i+1]
    res = []
    for i in range(0, len(text1), 2):
        temp1 = text1[i] + text1[i+1]
        temp = chr(int(str(temp1), base=16))
        res.append(temp)
    return ''.join(res).upper()

if __name__ == '__main__':
	print("DES算法")
	# 选择加密还是解密
	select_ = str(input("加密输入：e;解密输入：d")).upper()
	# 加密
	if select_ == "E":
		Mingwen = input("请输入明文")
		print("密钥自动生成！")
		key = Start_Key()
		# print(key)
		print("密钥为：", hex(int(key, base=2))[2:].upper())
		# 明文分组
		Mw_exchange = MW_Exchange(Mingwen)
		result = ""
		for i in range(0, len(Mw_exchange), 16):
			temp = str(Mw_exchange[i:i+16])
			mingwen = str(bin(int(temp, base=16))[2:])
			while len(mingwen) < 64:
				mingwen = "0" + mingwen
			ciphertext = DES(mingwen, key)
			temp1 = str(hex(int(ciphertext, base=2))[2:]).upper()
			while len(temp1) < 16:
				temp1 = '0' + temp1
			result += temp1
		print("加密结果为：", result)
	# 解密
	elif select_ == "D":
		ciphertext = str(input("请输入密文："))
		key1 = str(input("请输入密钥:"))
		key = str(bin(int(key1, base=16))[2:])
		while len(key) < 64:
			key = '0' + key

		result = ""
		res = []
		for i in range(0, len(ciphertext), 16):
			temp = str(ciphertext[i:i+16])
			res.append(temp)
		for i in range(0, len(res)):
			text = str(bin(int(res[i], base=16))[2:])
			while len(text) < 64:
				text = "0" + text
			decode_ciphertext = DES(text, key, "-1")
			temp1 = str(hex(int(decode_ciphertext, base=2))[2:])
			while len(temp1) < 16:
				temp1 = '0' + temp1
			result += RE_MW(temp1)
		print("解密结果为：", result)
	else:
		print("输入错误！")
