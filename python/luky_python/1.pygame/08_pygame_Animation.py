# 输出一个会移动的积木
import pygame
import time
import sys
from pygame.locals import *

# 初始化pygame
pygame.init()

# 建立窗口
WINDOWWIDTH = 400
WINDOWHEIGHT = 400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Animation")

# 定义方向变量
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 10

# 创建颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 创建盒子的数据结构
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UPRIGHT}
b2 = {'rect': pygame.Rect(200, 200, 20, 20), 'color': GREEN, 'dir': UPLEFT}
b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir':  DOWNLEFT}
box = [b1, b2, b3]

# 开始游戏循环
while True:
    """检查退出事件"""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    """将背景颜色设置为白色"""
    windowSurface.fill(WHITE)

    for b in box:
        """移动盒子的数据结构"""
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED

        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED

        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        """检查盒子是否移动到了窗口"""
        if b['rect'].top < 0:
            """盒子移动出了屏幕顶端"""
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT

        if b['rect'].bottom > WINDOWHEIGHT:
            """盒子经过底部"""
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT

            if b['rect'].left < 0:
                """盒子移动到左边部分"""
                if b['dir'] == DOWNLEFT:
                    b['dir'] = DOWNRIGHT
                if b['dir'] == UPLEFT:
                    b['dir'] = UPRIGHT

            if b['rect'].right > WINDOWWIDTH:
                """盒子移动到右边部分"""
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPRIGHT:
                    b['dir'] = UPLEFT

        """将盒子画在表面"""
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    """屏幕刷新"""
    pygame.display.update()
    time.sleep(0.02)




