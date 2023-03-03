# 所谓tag对象，对应的是HTML或XML文档中的标签，比如h1标签，img标签，a标签等。构造好BeautifulSoup对象以后，
# 直接通过成员操作符来访问tag对象。对于tag对象，可通过name属性来获取标签名，通过attrs属性来获取文档标签中的属性

from bs4 import BeautifulSoup

HTML = '<h1 id="heading">www.chipscoco.com</h1>'
bs = BeautifulSoup(HTML, features="html.parser")

# 访问文档中的h1标签对象
tag = bs.h1
# 输出标签名
print(tag.name)
# 输出h1标签的id属性
print(tag.parserClass)
print(tag.attrs["id"])
print(tag.string)
print("=="*20)

# 访问标签对象中的string属性
navigable_string = bs.h1.string
print(type(navigable_string))
print(navigable_string)
