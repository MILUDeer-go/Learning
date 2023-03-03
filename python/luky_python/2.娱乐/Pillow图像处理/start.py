
from PIL import Image

im = Image.open('夕阳.jpg')
print(im.format, im.size, im.mode)

# 该format属性标识图像的来源。如果图像不是从文件中读取的，则将其设置为无。
# size 属性是一个包含宽度和高度（以像素为单位）的 2 元组。
# mode属性定义了图像中波段的数量和名称，以及像素类型和深度。常见的模式是“L”（亮度）用于灰度图像，“RGB”用于真彩色图像，“CMYK”用于印前图像。

# 显示刚刚加载的图像
im.show()