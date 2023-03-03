# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字组成
"""
name : MILUDeer_go
date : 2021/10/24
"""

import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码
    ：param code_len:验证码长度（默认4个字符）
    ：return :由大小写字母和数字生成的随机验证码
    """
    all_chars = '0123456789abcdefjhijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    code = generate_code()
    print('随机验证码为：',code)
