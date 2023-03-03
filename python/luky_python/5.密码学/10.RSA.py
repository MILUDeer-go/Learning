# 编写RSA
# RSA是非对称加密算法，分为公钥和私钥
# 明文用只能有公私钥加解密
import random

# 求最大公因数
def gcd(a, b):
    """
    最大公因数
    """
    while a != 0:
        a, b = b % a, a
    return b

# 判断两个数是否互质
def Is_HuZhi(a, b):
    # 如果互质，那么最大公因数为1
    if a == 1 or b == 1:
        return 1
    else:
        c = gcd(a, b)
        return c

# 判断一个数是否为质数
def Is_Prime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    # 质数一定是奇数，因此只需要遍历3到质数的平方根没有公因子即可
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

# 生成大质数算法n位二进制，一般为1024或着2048位
def SC_ZhiShu(n):
    # 最后一位设置成1能加快生成速度
    res = random.randint(2**(n-1), 2**n-2)
    while res < 2**n - 1:
        res += 1
        if Is_Prime(res):
            break
    # print(res)
    return res

# 选择1到（p-1）*（q-1）中选择一个与（p-1）*（q-1）互质的数做私钥
def Select_Pvk(n):
    # 私钥从3开始找出互质的一个数，一般选择65537
    while True:
        if n > 65537:
            c = 65537
        else:
            c = random.randint(3, int(n ** 0.5) + 1)
        for e in range(c, n):
            if gcd(e, n) == 1:
                return e
        break

# 使用拓展欧几里得方法求公钥e关于（p-1）*（q-1）的逆
# 该逆元即为私钥
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

# 快速模运算
def quick_algorithm(a, b, c):
    a = a % c
    ans = 1
    # 这里我们不需要考虑b<0，因为分数没有取模运算
    while b != 0:
        #  &运算通常用于二进制取位操作，例如一个数 & 1 的结果就是取二进制的最末位。
        if b & 1:
            ans = (ans * a) % c
        # >>运算比较单纯,二进制去掉最后一位，移位操作，不断遍历b的二进制位
        b >>= 1
        a = (a * a) % c
    return ans
# 加密解密算法
def RSA_E(key, m, n):
    # 输入密钥（公私钥都可）和明文
    m_en = quick_algorithm(m, key, n)
    return m_en

if __name__ == "__main__":
    # 输入二进制大质数的位数
    m = int(input("请输入密钥的位数:"))
    # 生成两个不相等的质数p和 q
    p = SC_ZhiShu(m)
    q = SC_ZhiShu(m)
    # p,q不相同且互质
    while p == q or gcd(p, q) != 1:
        q = SC_ZhiShu(m)
    print(f"p:{p},q:{q}")
    # p*q
    n = p * q
    # 求数(p-1)*(q-1)
    a = (p-1)*(q-1)
    # 生成公钥e
    e = Select_Pvk(a)
    # 求出私钥d
    d = findModReverse(e, a)
    print(f'公钥为{e, n}')
    print(f'私钥为{d, n}')
    # 请输入要加密的信息
    while True:
        m = int(input(f"请输入要加密的信息:(小于{n})\n"))
        if m < n:
            break
        else:
            print("输入数据过大，请重新输入")
    m_en = RSA_E(e, m, n)
    print("加密后：", m_en)
    # 解密查看数据是否正确
    m_de = RSA_E(d, m_en, n)
    print("解密后：", m_de)





