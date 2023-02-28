from selenium import webdriver
firefox = webdriver.Chrome()
# 访问百度首页
firefox.get('https://www.baidu.com')
# 通过page_source属性获取网页源码
print(firefox.page_source)