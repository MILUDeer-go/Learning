# (3) 遍历兄弟节点
# 通过next_sibling或previous_sibling遍历当前节点的兄弟节点，前者表示后继，后者表示前驱。如需遍历所有前驱或所有后继，
# 则通过next_siblings或previous_siblings进行遍历。

from bs4 import BeautifulSoup

HTML = "<div><ul></ul><p></p><a></a><h1></h1><img /></div>"

bs = BeautifulSoup(HTML, features='html.parser')

# 定位a节点
a = bs.a

# 在循环中获取a节点的所有前向兄弟节点
# 在以上HTML中，a节点的所有前向兄弟节点为p以及ul
for previous_sibling in a.previous_siblings:
    # 遍历出来的parent为tag对象
    print(previous_sibling.name)

print("="*30)
# 找出HTML所以的后继兄弟节点
for next_sibling in a.next_siblings:
    print(next_sibling.name)

