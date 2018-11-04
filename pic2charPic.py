from PIL import Image
import argparse,os


'''
gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  
人眼对rgb的感知能力不同
公式的意思是人眼感知的明暗
是三种颜色的光线感知强度的和
系数是科学家通过大量实验得出的。 
'''


'''
# 命令行输入参数处理
parser = argparse.ArgumentParser()  # 创建一个解析器对象parser

# 添加参数
parser.add_argument("file")  # 输入文件参数字符串变量file

args = parser.parse_args()  # 解析命令行
im = args.file  # 参数file付给IMG
# OUTPUT = args.output
'''



gray = 256
im=os.getcwd()+"/assets/01.jpg"

# 字符画中所出现的字符集,长度70
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(gray, alpha=256):  # 用来将像素转化为字符串的函数
	if alpha == 0:  # 如没有像素，那么输出空格
		return " "
	length = len(ascii_char)
	# 将像素彩色值转化为灰度值，getpixel是image的一个函数
	gray = im.getpixel((j, i))

	return ascii_char[int(gray / 256 * length)]  # 确定每个色素用哪个字符


im = Image.open(im)
im = im.resize((270, 270), )# 调整图像大小至和输出字符画长宽一致
im = im.convert("L")  #

txt = ""  # 建立个字符串变量

for i in range(270):  # 扫描每行
	for j in range(270):  # 扫描每列
		txt += get_char(gray)
		txt += get_char(gray)  # 一行的像素都转化成字符串
	txt += "\n"  # 换行处理

print("转换成功")  # 转化成功

f = open("output.txt", "w")  # 输出至output.txt
f.write(txt)
f.close()
