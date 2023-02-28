# 绘制一个折线图
# 导入matplotbli.pyplot模块
import matplotlib.pyplot as plt
# 使用内置模块
plt.style.use('seaborn')
# 使用整个图表作为照片输出
fig, ax = plt.subplots()

# 画出第一个点,s表示散点的尺寸
# ax.scatter(2, 4, s=200)

'''给一组x,y的数值
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
ax.scatter(x_values, y_values, s=100)
'''
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# 使用渐变色
# ax.scatter(x_values, y_values, c='red', s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# 用来正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']

# 设置图表的标题和给坐标加上标签
plt.title("平方数", fontsize=14)
plt.xlabel("值", fontsize=14)
plt.ylabel("值的平方", fontsize=14)
# 设置每个坐标轴的范围
ax.axis([0, 1100, 0, 1100000])
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 输出图表
plt.show()