# 在屏幕上显示跑马灯文字

"""
name: MILUDeer_go
dat: 2021/10/24
"""

import os 
import time

def main():
    content = '我在大海游海大'
    count = 0
    while True:
        # 清理屏幕上的输出
        os.system('cls')    # os.system('clear')
        print(content)

        # 休眠200ms
        time.sleep(0.2)
        content = content[1:] + content[0]

        count +=1
        if count > 10:
            break

if __name__ == '__main__':
    main()