import sys
import pygame
from pygame.locals import *

# 创建pygame
pygame.init()

# 建立window窗口
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello World!")


# 赋值背景颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 建立字体
basciFont = pygame.font.SysFont(None, 48)

# 建立文章内容
text = basciFont.render('hello world', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# 背景颜色
windowSurface.fill(WHITE)

# 将绿色的多边形显示在频幕上
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (292, 106), (236, 277), (56, 277), (0, 106)))

# 画一些蓝色的线条在表面
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120), 2)
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# 画一个蓝色的圆圈在窗口里
pygame.draw.circle(windowSurface, BLUE, (300, 50), 40, 0)

# 化一个矩形文本框作为文本的背景
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20,
                                      textRect.width + 40, textRect.height + 40))
# 获取像素阵列在窗口里
pixArrag = pygame.PixelArray(windowSurface)
pixArrag[480][380] = BLACK
del pixArrag

# 将文本传输到表面
windowSurface.blit(text, textRect)

# 画一个红色的椭圆在窗口里
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 0)

# 将窗口信息更新显示到屏幕上
pygame.display.update()

# 一直运行pygame
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
