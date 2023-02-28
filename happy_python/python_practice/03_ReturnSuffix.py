# 设计一个函数返回文件后缀名

"""
name : MILUDeer_go
date : 2021/10/24
"""

def Get_Suffix(filename,has_dot=False):
    """
    获取文件后缀名
    : param filename : 文件名
    : param has_dot : 返回文件是否需要带点
    : return : 文件后缀名
    """
    pos = filename.rfind('.')      # 找出点所在的位置的索引
    print(pos)
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1   # 等于 if has_dot == True: index = pos else: index = pos +1        
        return filename[index:]
    else:
        return ''

if __name__ == '__main__':
    filename = 'test.tex'
    Suffix = Get_Suffix(filename)
    print(f"{filename}的后缀名为：{Suffix}")

