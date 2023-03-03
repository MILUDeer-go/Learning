# 奥特曼打小怪兽

"""
name: MILUDeer_go
dat: 2021/10/24
"""

from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass = ABCMeta):
	"""战斗者"""

	# 通过__slots__魔法限制对象可以绑定的成员变量
	__slots__ = ('_name', '_hp')

	def __init__(self, name, hp):
		"""初始化方法"""
		self._name = name
		self._hp = hp 

	# @property包装器 --访问器getter方法
	@property
	def name(self):
		return self._name

	@property
	def hp(self):
		return self._hp

	# 修改器 -setter方法
	@hp.setter 
	def hp(self, hp):
		self._hp = hp if hp >= 0 else 0 

	@property
	def alive(self):
		return self._hp > 0

	@abstractmethod
	def attack(self, other): 
		pass






	
	