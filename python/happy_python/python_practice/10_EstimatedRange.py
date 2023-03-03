# 定义一个类描述数字时钟

"""
name : MILUDeer
date : 2021/11/12
"""

from math import sqrt      # math模块引入sqrt函数计算平方根

class Point(object):

	def __init__(self, x=0, y=0):
		# 初始化
		self.x = x
		self.y = y

	def move_to(self, x, y):
		"""
		x,y新的横纵坐标
		"""
		self.x = x 
		self.y = y 

	def move_by(self, dx, dy):
		"""dx,dy表示移动的增量
		"""
		self.x += dx 
		self.y += dy

	def distance_to(self, other):
		"""计算距离，other表示另一个点的位置"""
		dx = self.x - other.x 
		dy = self.y - other.y
		return sqrt(dx**2 + dy**2)


	def __str__(self):
		return '(%s, %s)' % (str(self.x), str(self.y))


def main():
	p1 = Point(1, 5)
	p2 = Point()
	print(p1)
	print(p2)
	print("="*30)
	p2.move_by(-1, 2)
	print(p2)
	print(p1.distance_to(p2))

if __name__ == "__main__":
	main()