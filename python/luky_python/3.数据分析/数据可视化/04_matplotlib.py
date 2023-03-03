# 创建一个折线图
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)  # 输出0-9的数字
y = np.sin(x)


plt.plot(x, y, lw=2, label='plot figure')
plt.legend()  # 给图表加上图例，就是加上label标签中的内容
plt.show()
