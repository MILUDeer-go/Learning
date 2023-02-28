
import requests

url = 'https://www.baidu.com/'

proxies = {
    'http': 'http://106.14.5.129:80',
    # 'https': 'https://106.14.5.129:80'

}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
response = requests.get(url, proxies=proxies, headers=headers)
print(response.text)