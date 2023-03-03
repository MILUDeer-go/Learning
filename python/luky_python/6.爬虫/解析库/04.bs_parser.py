from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 读取HTML中的信息
    html = open("chipscoco.html", 'r', encoding='utf-8')
    """
        (1) 构造BeautifulSoup对象, 指定lxml解析器
        (2) 使用lxml解析器需要先在命令行中执行pip install lxml进行安装
    """

    bs = BeautifulSoup(html, 'lxml')
    # 直接通过BeautifulSoup对象来获取HTML title对象的文本内容
    title = bs.title.string
    print('title = ' + title)

    # 通过find方法中的attrs参数来获取属性id为heading的标签对象
    h1 = bs.find(attrs={"id": "heading"})
    h1_text = h1.string if h1 else ""
    print(h1_text)

    # 执行BeautifulSoup对象的find方法来获取HTML中的a标签
    link = bs.find("a")
    # 访问a标签对象的href属性
    href = link["href"] if link else ""
    print("html title:{}\narticle title:{}\nhref:{}".format(title, h1_text, href))





