# 设计一个函数返回传入列表中的最大和第二大的元素的值

"""
name : MILUDeer_go
date : 2021/10/24
"""

import random

def get_max2(list1):
    """
    返回传入列表中的最大和第二大的元素的值
    ：param ：列表
    : return : 最大和第二大的元素的值
    """
    
    m1 , m2 = (list1[0] , list1[1])  if list1[0] > list1[1] else (list1[1],list1[0])
    for index in range(2,len(list1)):
        if list1[index] > m1:
            m2 = m1
            m1 = list1[index]
        elif list1[index] > m2:           
            m2 = list1[index]
    return m1,m2

if __name__ == '__main__':
    x = [1,2,3,4,5,6,7,10]

    m1,m2 = get_max2(x)
    print("最大的两个值为：",(m1 , m2))