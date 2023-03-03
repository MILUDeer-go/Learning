# 为爬虫设置UA
import urllib.request

url = "https://www.baidu.com/"
# Chrome游览器的UA
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'

# 设置爬虫程序的UA，可在一定程度上防止被服务端反爬
headers = {'User_Agent': user_agent}

response = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(response) as resp:
    the_page = resp.read()
    print(the_page)
