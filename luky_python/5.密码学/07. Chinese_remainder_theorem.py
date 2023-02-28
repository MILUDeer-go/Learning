# 中国式剩余定理的求解
# 定义一个函数，参数分别为a,n，返回值为b
def gcd(a, b):
    """
    判断最小公倍数b
    """
    while a != 0:
        a, b = b % a, a
    return b

# 扩展欧几里得算法求模逆
def findModReverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# 判断所有的mi是否两两互质
def Is_Coprime(m_list):
    for i in range(len(m_list)):
        for j in range(i + 1, len(m_list)):
            if 1 != gcd(m_list[i], m_list[j]):
                return 0  # 返回0表示不是两两互质的
    return 1  # 返回1表示是两两互质的


# 获取所有的Mi
def Get_Mi(m_list, M):
    Mi_list = []
    for mi in m_list:
        Mi_list.append(M // mi)
    return Mi_list


# 获取所有的Mi的逆元
def Get_Mi_inverse(Mi_list, m_list):
    Mi_inverse = []
    for i in range(len(Mi_list)):
        Mi_inverse.append(findModReverse(Mi_list[i], m_list[i]))
    return Mi_inverse

# 中国剩余定理,返回值为最终的x
def C_R_T():
    while True:
        # 两个空列表，分别用来保存mi和bi
        m_list = []
        b_list = []

        while True:  # 输入mi
            m_i = input("请输入mi,以'.'结束输入:")
            if m_i == '.':
                break
            elif False == m_i.isnumeric():
                print("输入有误，请输入数字:")
                m_i = input()
                continue
            else:
                m_list.append(int(m_i))

        while True:  # 输入bi
            b_i = input("请输入bi,以'.'结束输入:")
            if b_i == '.':
                break
            elif False == b_i.isnumeric():
                print("输入有误，请输入数字！\n")
                b_i = input()
                continue
            else:
                b_list.append(int(b_i))

        if len(m_list) != len(b_list):
            print("错误！mi的个数和bi的个数不相同，请重新输入\n")
        elif 0 == Is_Coprime(m_list):
            print("错误！输入的mi并不是两两互质的，请重新输入mi\n")
        else:
            break

    M = 1  # M是所有mi的乘积
    for mi in m_list:
        M *= mi

    Mi_list = Get_Mi(m_list, M)
    Mi_inverse = Get_Mi_inverse(Mi_list, m_list)
    x = 0
    for i in range(len(b_list)):  # 开始计算x
        x += Mi_list[i] * Mi_inverse[i] * b_list[i]
        x %= M
    return x


if __name__ == '__main__':
    print("同余式组的解为：x=%d" % C_R_T())
