# 约瑟夫环问题
"""
name : MILUDeer
date : 2021/11/12
"""

def main():
	person = [True] * 20
	counter, index, number = 0, 0, 0 
	while counter < 19:
		if person[index]:
			number += 1
			if number == 9:      # 位置第9的出局
				person[index] = False
				counter += 1
				number = 0 
		index += 1
		index %= 20
		for persons in person:
			print("活" if persons else "死", end="")
		print("\n")

if __name__ == '__main__':
	main()