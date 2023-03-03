# 构造BeautifulSoup对象

from bs4 import BeautifulSoup
HTML = '<html><body><div><h1>www.chipscoco.com</h1></div></body></html>'

bs = BeautifulSoup(HTML, features='html.parser')

# 访问文档中的h1标签对象
tag = bs.h1
# 输出标签名
print(tag.name)
# 输出h1文本
print(tag.text)
# 也可以通过文件流对象来构造BeautifulSoup
# bs = BeautifulSoup(open("index.html"),features="html.parser")
