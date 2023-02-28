# 解析ul节点下的li子节点的a

from lxml import etree

HTML = """
<html>
<head>  
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">  
    <title>薯条老师的官方教程:www.chipscoco.com</title>
</head>
<body> 
<ul>
    <li> <a href="www.chipscoco.com">薯条老师的官方教程</a></li>
    <li> <a href="www.chipscoco.cn">橙子在线编程</a></li>
<li> <a href="www.shadows.com">侠影七三</a></li>
<li> <img src="/media/images/cover.png" /></li>
</ul>
</body>
</html>
"""

etree1 = etree.HTML(HTML)
li_container = etree1.xpath("//ul//li")

for li in li_container:
    # 列表中的每一个元素均为Element对象
    # xpath中的.表示当前节点
    # 模糊匹配contains
    o = li.xpath("./a[contains(@href, 'chipscoco')]/@href")
    print(o) if o else 0