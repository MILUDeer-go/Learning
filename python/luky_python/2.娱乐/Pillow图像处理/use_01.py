import sys
from PIL import Image
# 在命令行调用参数时候使用sys.argv[]返回一个.py文件和后面所带的参数
for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass