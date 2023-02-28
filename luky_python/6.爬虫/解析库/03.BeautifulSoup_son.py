# (1) 遍历子节点
# 通过tag对象的contents属性，可将当前节点的所有子节点以列表的形式输出。读者需注意的是，contents列表中的元素为tag对象。
# 通过tag对象的children属性遍历当前节点的所有子节点，children为迭代器对象，可在循环中进行遍历。

from bs4 import BeautifulSoup
HTML = "<div><p></p><h1></h1></div>"

# 在以上HTML中，p节点以及h1节点均为div节点的子节点
bs = BeautifulSoup(HTML, features='html.parser')

div = bs.div
print(div)

print("="*30)
# 通过children遍历div节点的所有子节点
for children in div.children:
    print(children.name)