"""
hash.update(arg)
用字符串arg更新哈希对象。重复的调用等同于单次调用所有参数的连接：m.update(a); m.update(b) 相当于m.update(a+b)。

hash.digest()
返回目前为止传递给update()方法的字符串的摘要。它是一个具有digest_size个字节的字符串，其中可能包含非ASCII 字符，包括空字节。

hash.hexdigest()
类似digest()，但是返回的摘要的字符串的长度翻倍，且只包含十六进制数字。这可用于在电子邮件或其它非二进制环境中安全交换数据。
"""

import hashlib

def get_file_md5(f):
    m = hashlib.md5()
    while True:
        #如果不用二进制打开文件，则需要先编码
        #data = f.read(1024).encode('utf-8')
        data = f.read(1024)  #将文件分块读取，避免占用大量内存
        if not data:
            break
        m.update(data)
    return m.hexdigest()

#将file2文件写入改动一个位数的数据
txt1 = '验证文件'
txt2 = '验证文件1'
with open('1.txt', 'w', encoding='utf-8') as f1, open('2.txt', 'w', encoding='utf-8') as f2:
    f1.write(txt1)
    f2.write(txt2)

with open('1.txt', 'rb') as f1, open('2.txt', 'rb') as f2:
    file1_md5 = get_file_md5(f1)
    file2_md5 = get_file_md5(f2)
    print('file1_md5:', file1_md5)
    print('file2_md5:', file2_md5)
    if file1_md5 != file2_md5:
        print('文件变动')
    else:
        print('文件未变动')
