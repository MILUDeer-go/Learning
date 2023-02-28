# 抓取python官方文档
"""
如果需要在执行get方法时传递url参数，可以通过params参数。
params参数接收一个字典对象，键名表示请求的参数名，键值表示传递的url参数。
"""
import requests
url = 'https://docs.python.org/3/search.html'
payload = {'q': 'urllib'}
response = requests.get(url, params=payload)
print(response.url)
print(response.text)