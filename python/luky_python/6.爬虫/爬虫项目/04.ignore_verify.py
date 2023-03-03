# 使用verify忽略CA证书
import requests
url = 'https://sam.huat.edu.cn:8843/selfservice/'

response = requests.get(url, verify=False)
print(response.content)