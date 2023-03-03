# 解析所有title标签的文本

"""
①  从lxml中导入etree模块

②  执行etree模块的HTML方法构建etree的Element对象

HTML方法的常用参数：HTML(text)，text表示HTML文本。

③ 通过Element对象的xpath方法来解析HTML
"""

from lxml import etree

HTML = """
<html>
<head>  
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">  
    <title>薯条老师的官方教程:www.chipscoco.com</title>
</head>
<body>  
</body>
</html>
"""
etreeA = etree.HTML(HTML)   # 创建对象
o = etreeA.xpath("//title/text()")    # 寻找title标签下单text()文本
print(o)



