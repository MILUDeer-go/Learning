import pygame
import time
import random
import sys
from pygame.locals import *

# 建立游戏
pygame.init()
mainClock = pygame.time.Clock()

# 创建窗口
WINDOWWIDTH = 400
WINDOWHEIGHT = 400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("beautiful sprite")

# 创建颜色
WHITE = (255, 255, 255)

# 创建人物块数据结构
player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('sprite.jpg')  # 导入图片
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))  # 设置图片大小

# 创建食物数据结构
foodimage = pygame.image.load('food.jpg')
foodImage = pygame.transform.scale(foodimage, (20, 20))
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

foodCounter = 0
NEWFOOD = 40

# 设置键盘变量，4个布尔值变量用来记录按下了哪个方向键。例如，当用户按下键盘上向左的方向键时，
# 把moveLeft设置为True。当松开这个键时，把moveLeft设置回False。
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

# 移动速度
MOVESPEED = 6

# 设置音乐
pickUpSound = pygame.mixer.Sound('loveyou.wav')
pygame.mixer.music.load('loveyou.wav')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# 开始游戏循环
while True:
    """检查退出事件"""
    for event in pygame.event.get():
        if pygame.event == QUIT:
            pygame.quit()
            pygame.sys()
        # 键盘响应按下
        if event.type == KEYDOWN:
            """改变关键变量"""
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        # 键盘放开
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            # 控制音乐
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0, 0)
                musicPlaying = not musicPlaying
        # 通过鼠标获得新的食物
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        """自动增加新的食物"""
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20),
                                 random.randint(0, WINDOWHEIGHT - 20), 20, 20))
    # 将白色的背景放在表面上
    windowSurface.fill(WHITE)

    # 移动游戏人物
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # 将块画在表面
    windowSurface.blit(playerStretchedImage, player)

    # 检查人物块是否碰撞到食物
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top,
                                 player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))

            # if musicPlaying:
            #     # 在pickupSound所存储的sound对象上调用play(),只有条件为真才会执行,每次移动都会重头播放音乐
            #     pickUpSound.play()

    # 绘画食物
    for food in foods:
        windowSurface.blit(foodImage, food)

    # 在屏幕上显示窗口
    pygame.display.update()
    mainClock.tick(40)