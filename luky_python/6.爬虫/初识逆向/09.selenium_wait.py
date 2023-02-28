# 模拟百度搜索
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# 访问百度页面
url = 'https://www.baidu.com'
browser.get(url)

try:
    # 等待页面中出现id为kw的元素，等待时间为5秒
    input1 = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'kw')))
    # 页面中出现id为kw的元素后才模拟用户的输入
    input1.send_keys('薯条老师')
    # 根据id定位到首页中的搜索按钮
    search = browser.find_element_by_id('su')
    # 执行click方法，模拟用户的点击事件
    search.click()
finally:
    time.sleep(3)
    browser.quit()
