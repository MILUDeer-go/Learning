# (2) 遍历父节点
# 通过parent或parents属性遍历当前节点的父节点，
# 前者指向当前节点的父节点，后者为一个生成器，
# 可在循环中递归获取当前节点的所有父节点。

from bs4 import BeautifulSoup

htML = '<body><div><p></p><h1></h1></div></body>'

bs = BeautifulSoup(htML, features='html.parser')
h1 = bs.h1
# 获取h1节点的父节点，h1节点的父节点为div
print(h1.parent.name)

# 在循环中获取h1节点的所有父节点
for parent in h1.parents:
    # 遍历出来的parent为tag对象
    print(parent.name)
