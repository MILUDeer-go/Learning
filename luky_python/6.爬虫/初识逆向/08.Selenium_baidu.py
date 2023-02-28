# 模拟百度搜索
from selenium import webdriver
import time

# 创建火狐游览器对象
browser = webdriver.Firefox()
# 访问百度首页
browser.get("https://www.baidu.com")
# 将id定位到百度首页的输入框
input_key = browser.find_element_by_id('kw')
# 在输入框中输入薯条老师
input_key.send_keys('薯条老师')
# 根据id定位到首页中的搜索按钮
search = browser.find_element_by_id('su')
# 执行click方法，模拟用户的点击事件
search.click()
# 执行time.sleep方法模拟用户在页面停留
time.sleep(3)
# 退出
browser.close()
