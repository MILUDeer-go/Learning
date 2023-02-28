# Comment对象是一种特殊的NavigableString对象，当注释内容被包含于tag中时，通过string属性得到的即为Comment对象

from bs4 import BeautifulSoup

HTML = '<b><!--it is a comment!--></b>'

bs = BeautifulSoup(HTML, features="html.parser")
# 访问b标签中的string，此时的string是一个Comment对象
comment = bs.b.string
print(type(comment))
print(comment)