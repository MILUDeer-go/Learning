# 求解模的逆
# 使用欧几里得算法

# 求一个数的逆
# 要定义这个运算，需要三个整数。a的模逆元素（对n取模）为b，意味着a*b mod m=1，则称a关于m的模逆为b
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

if __name__ == '__main__':

    a = int(input('请输入求模逆的数：'))
    m = int(input("请输入模的值："))

    b = findModReverse(a, m)
    if None == b:
        print("%d模%d的逆不存在" % (a, m))
    else:
        print("%d模%d的逆为：%d" % (a, m, b))




