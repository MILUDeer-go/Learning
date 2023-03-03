import requests

"""
(1) 字典类型变量headers，用来定义HTTP请求头。我们可以在headers变量中定义User-Agent，cookie等字段

"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    # 在HTTP请求中发送Cookie
    'cookie': 'BAIDUID=03C9A27F2A09F8261BD17E34C2D19C38:FG=1; BIDUPSID=80BC549FAA32FC2DE5CFA86F61635D2E; PSTM=1583838768; BDUSS=HJzVHZKVGw1Y1NLMEZLNlNvajBybDRiQWxrNGNYS1FFZ3p5a1ByS0wzR2F2cHRlRVFBQUFBJCQAAAAAAQAAAAEAAABschQSWkRMwLLAssCyc2t5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJoxdF6aMXReZ; MCITY=-125%3A; __yjs_duid=1_5d0577d7ad5101b2ce95e64eb8eb62701619508173117; BD_UPN=13314752; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[Fc9oatPmwxn]=srT4swvGNE6uzdhUL68mv3; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_PSSID=34945_34442_34918_35105_31254_34967_35049_34584_34518_34532_34916_34813_26350_35072_34865_35114_35127; H_PS_645EC=ff0dEbkE3aSp64sIPU648QFBoIKx5j%2BXe5LEjy99CH9cjR0GDtwcV2Zs000p8Lop0xQ9; BA_HECTOR=2g0004208g24a40kgp1gp6umn0q; sugstore=1'

}

"""
(1) 字典类型变量proxies，用来配置HTTP代理。
(2) 键名表示代理所使用的协议，常用的有http与https。https协议是HTTP加上 TLS/SSL 协议所构建的加密传输协议。
(3) 键值表示http代理的地址。
"""
proxies = {
    # 以下代理并不存在，为虚构的代理地址，读者可自行找寻可用的HTTP代理
    "http": "http://127.0.0.1:9000"
}

# 以下url并不存在，同学们在实际练习时，可将之替换为待抓取的网页的url
url = "https://www.baidu.com"

# 通过关键字参数proxies来传递http代理的配置信息
response = requests.get(url, headers=headers, proxies=proxies)

# 返会响应体的头部
print(response.headers)