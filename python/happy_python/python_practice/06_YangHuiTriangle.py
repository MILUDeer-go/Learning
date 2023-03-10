# 打印杨辉三角
"""
name : MILUDeer
date : 2021/10/24
"""
def main():
    num = int(input("Number of row:"))
    yh = [[]]*num 
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row: 
                yh[row][col] = 1
            else: 
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end="")
        print()

if __name__ == "__main__":
    main()
