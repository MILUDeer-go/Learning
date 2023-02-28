# 使用plotly掷骰子
import random

import plotly
from plotly.graph_objs import Bar, Layout


class Die:
    """创建一个骰子类"""
    def __init__(self, num_sides=6):
        """默认是6个面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return random.randint(1, self.num_sides)


#  创建一个实例6面的骰子
die = Die()

# 投掷几次骰子并把结果记录在以下的列表中
results = []
# 重复投掷一百次，记录结果

for roll_num in range(1000):
    result = die.roll()       # 执行函数
    results.append(result)    # 通过append模块将数据加入列表尾部

# 分析结果
frequencies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)   # 统计result列表中的相同数据个数
    frequencies.append(frequency)      # 将统计结果放到新的列表中
# # 打印结果
# print(frequencies)

# 对结果进行可视化
x_value = list(range(1, die.num_sides + 1))  # 打印横坐标列表print(x_value)
data = [Bar(x=x_value, y=frequencies)]      # 使用Bar来绘制条形图的数据集，这个类必须放在[]中

# 设置横纵坐标的名称（字典）
x_axis_config = {'title': '结果'}
y_axis_config = {'title': '频率'}

# 使用Layout类返回指定图表的布局和配置对象
my_layout = Layout(title='投掷1000次6面骰子的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)

# 调用offline.plot()制作图表，传入数据是字典格式
plotly.offline.plot({'data': data, 'layout': my_layout}, filename='D6.html')







