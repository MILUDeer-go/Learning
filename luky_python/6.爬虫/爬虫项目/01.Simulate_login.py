"""
现在我们尝试使用selenium来模拟登录
不带有验证码的网站
name：MILUDeer_go
data:2021/11/22
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()

browser.get('http://www.chipscoco.com')

# 等待页面中出现class为sinup的元素，等待时间为5秒
login = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sinup')))



actions = ActionChains(browser)
# 将鼠标移动至登录按钮并点击
actions.move_to_element(login).click(login).perform()
# 找到id为edtUserName的页面元素，该html元素用来输入用户名
username_input = browser.find_element_by_id('edtUserName')
username_input.send_keys("TEST123456")

# 找到id为edtPassWord的页面元素，该html元素用来输入登录密码
password_input = browser.find_element_by_id('edtPassWord')
password_input.send_keys("TEST123456")

# 找到id为loginbtnPost的页面元素，该html元素用来提交登录请求
submit_button = browser.find_element_by_id('loginbtnPost')
# 点击登录按钮
submit_button.click()
