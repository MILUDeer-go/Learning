
# 引入matplotbli.pyplot模块
import matplotlib.pyplot as plt

# 定义一个输入列表
input_values = [1, 2, 3, 4, 5]
# 定义输出一个列表
s = [1, 4, 9, 16, 25]

# 使用内置样式
plt.style.use('seaborn')

# fig表示整张图片，ax表示图片中的图表
fig, ax = plt.subplots()

# 整合输入输出数据
ax.plot(input_values, s, linewidth=3)

# 改变plot()绘制的线条粗细
# ax.plot(s, linewidth=3)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 设置图表标题并给坐标轴加上标签
plt.title("平方数", fontsize=14)
plt.xlabel("值", fontsize=14)
plt.ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

# plot有意义的绘制图表
# ax.plot(s)

# show()函数展示图表
plt.show()
