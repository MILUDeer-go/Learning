import requests

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
url = 'http://challenge-06d1a1616e98bff4.sandbox.ctfhub.com:10800/index.php'
response = requests.get(url, headers=headers, allow_redirects=False)
print(response.text)
