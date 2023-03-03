# 解析所有div标签下的所有img标签的src属性

from lxml import etree

HTML = """
<html>
<head>  
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">  
    <title>薯条老师的官方教程:www.chipscoco.com</title>
</head>
<body> 
    <div> 
        <img src="/media/images/logo.png" />
        <ul>
           <li><img  src="http://justtest.com/one.jpg"/></li>
        </ul>
</div>
<ul>
    <li> <a href="www.chipscoco.com">薯条老师的官方教程</a></li>
    <li> <a href="www.chipscoco.cn">橙子在线编程</a></li>
</ul>
</body>
</html>
"""

etree1 = etree.HTML(HTML)

#  通过Element对象的xpath方法来解析HTML
t = etree1.xpath("//div//img/@src")  # 匹配从div节点的img节点下所有的属性为src的文本

print(t)

# 径表达式为//div/img,那么只能匹配到div节点下的img子节点。
# 读者可以将代码中的路径表达式改为//div/img/@src，那么输出的只是['/media/images/logo.png']。
