# 双色球选号
"""
name : MILUDeer
date : 2021/10/24
"""

from random import randrange,randint,sample

def display(balls):
	"""
    输出列表中双色球的号码
	"""
	# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
	# 同时列出数据和数据下标，一般用在 for 循环当中。
	for index , ball in enumerate(balls):
		if index == len(balls) - 1:
			print('|', end = '')
		print('%02d' % ball, end ='')

	print()


def random_select():
	"""
	随机选择一组号码
	"""
	red_balls = [x for x in range(1,34)]
	selected_balls = []
	selected_balls = sample(red_balls, 6)
	selected_balls.sort()     # 排序（默认升序）
	selected_balls.append(randint(1,16))
	return selected_balls

def main():
	n = int(input('机选几注：'))
	for _ in range(n):
	 	display(random_select())

if __name__ == '__main__':
	main()


