# 使用爬虫来使用百度翻译（出错了，因为随机数的原因）
import requests
import json

class BaiDu_trs(object):

    def __init__(self):
        # 初始化翻译所在的url
        self.url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

        self.headers = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664.45Safari / 537.36'
        }
        self.data = {
        'from': 'zh',
        'to': 'en',
        'query': '字典',
        'simple_means_flag': '3',
        'sign': '763934.1002287',
        'token': '1d18bb34d58578b046fd51eb4b9f12b5',
        'domain': 'common'
        }


    def response(self):
        res = requests.post(self.url, headers=self.headers, data=self.data)
        return res.content

    def parse_data(self, data):
        # json.loads()将json数据转化为python字典
        parse_data = json.loads(data)
        return parse_data


    def run(self):
        response = self.response()
        print(self.parse_data(response))


if __name__ == '__main__':
    translation = BaiDu_trs()
    translation.run()

