import requests

url = 'https://github.com/'
# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Cookie': '_octo=GH1.1.306886830.1635676496; _device_id=5765c09639e026cf27823690aeb399d6; tz=Asia%2FShanghai; '
              'has_recent_activity=1; user_session=ssGGIp_shZuD6caxnZL10udCHlbkAyuzcyl7JJzZ8T_8PdW2;'
              ' tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name'
              '%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark'
              '%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=MILUDeer-go; _gh_sess='
              'cxHNouZwrVPGutqDd32W3JzXxiI0Uac2E6CECc0k0zEbZYFOoo98OvcFEG0UZk1PKcydQwqSjY1Ra4kZaUY0tFHAqA2Uzr'
              'aW0CWQ26%2Fgbh9cjExZa%2Biyy6J6fxUS7BtnSG03WvGFuo8Fvaq01dSk4DYArLlM7s0kHWvYa0ScD3fA3yvcpDc7%2B0nvS6YV'
              'qPAfWFP6rVRxZlokXmDeu6SH5lcLgaZVLpQhTBp1UPtvP5%2BfzKvPwXLZ4SaUjLMCQM7s9Y3wj4ggGHYKSIno9al%2FT7RebRKKWX%'
              '2BSbn7QsJnQapFrrunT21DqjRcPqb2q1x8fPEq6GxX0DLmKKRI26czSP8%2BzMnev7I3fPRUNZR%2Bs8kSWups2Lfu5UOUWe4fpS9widp'
              '53ZmVbUx1Sj%2FqGXrM9gVO8lJq%2BVEtdNrhT0goUR2xc4t%2BrXdEFQz8zz0O2E1EOqNx9aULGHwytj8ix2viEDIZKA5STJV63CxwaD'
              '4N1zB8OHx3Dfkivz3ZZCohXEN5c9SQadlIIf3wC8t90Pe9o5z0EAvEuVVa1zNgOcF6nkxi4jE4JKaemUiH2vnWiij5ThAiZ%2Fp5ZjTZW'
              'gVupkTA%2BBY8H%2BYY5mRtwxEJWW3Rjh7Om%2Bb4OiJzYPapZTOBTBHtE0yY%2Bb8cmUbhwfgiBwoeZKTdILKfkEI9ybnZXMPfEEucXh'
              'BCytmo9A8bc3xk97bPxBCRLjf2836%2Bo3nF%2BlAceRVuhVCRDcGvn2kwb0AleGhY94sM5jA4tptT6hqr2QPFSywRgZjWZIYZtD6NAq7'
              '9HdHEl3dX%2FImL5XR%2F9QX9eF%2FhmxDkzFs9cHhJX5ymAjYhZiL3ZSZVNtRFV8UioohyIocDqt%2F3ufhmnq6l2%2FBYVt4hfPGa1Av'
              'WOxI4PaK%2FZLtIwAQSgMZYaD9qh0KGe86jboezmTdJLzVhJSSlZMo0aNeY%3D--qLpI56k36gqL%2FOqv--O4u4nL9G2s52AJGM82H0%2FQ%3D%3D'
}
response = requests.get(url, headers=headers)

with open('github.html', 'wb') as f:
    f.write(response.content)

