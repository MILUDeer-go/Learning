# 建一个随机漫步的图表
# 导入matpoltbli.pyplot模块
# 导入random模块的choice函数
import sys
import matplotlib.pyplot as plt
from random import choice


# 创建一个生成随机漫步数据的类
class RandomWalk:

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有的随机漫步都开始与（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定长度
        while len(self.x_values) < self.num_points:

            # 决定前进的方向以及沿这个方向前进的方向
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标x,y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# 绘制随机漫步图
"""
# 只要程序处于活动状态就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()

    # 将所有点绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots()

    # 给点着色
    num_point = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=num_point,
               cmap=plt.cm.Blues, edgecolor='none', s=15)

    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolor='none', s=100)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 展示图表
    plt.show()

    keep_running = input("要继续吗？(y/n):")
    if keep_running == 'n':
        break

"""
while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 将所有点绘制出来
    plt.style.use('classic')
    # 创建图表可以用figsize指定生成图片的尺寸,dpi可以传递分辨率
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)

    # 给点着色
    num_point = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=num_point,
               cmap=plt.cm.Greens, edgecolor='none', s=10)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 展示图表
    plt.show()

    keep_running = input("要继续吗？(y/n):")
    if keep_running == 'n':
        break



