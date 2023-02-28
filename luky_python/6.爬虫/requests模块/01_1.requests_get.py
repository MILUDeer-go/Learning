# 抓取python官网首页
import requests
url = 'https://www.python.org/'
r = requests.get(url)
print(r.text)