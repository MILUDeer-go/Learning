"""
打印自己的第一个程序“Hello World”
"""
# print("Hello World")
def chengfabiao(b):
    for i in range(b):
        for j in range(i+1):
            print("%d * %d = %d  " % (j + 1, i + 1, (i + 1) * (j + 1)), end='')
        print("\t")

print("九九乘法表：")
chengfabiao(9)
