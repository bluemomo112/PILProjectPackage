from PIL import Image,ImageFont,ImageFilter,ImageDraw
import random,os

char_list=[chr(i) for i in range(65,65+26) ]
def getRandomChar():

	text=""
	for i in range(4):
		text=text+random.choice(char_list)
	return text

def getRandomColor():
	return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))

# 获得验证码图片
def getCodePiture():
	width = 240
	height = 60
	# 创建画布(模式，size，颜色)，
	image = Image.new('RGB', (width, height), (180,180,180))
	# print(os.listdir(os.getcwd()+"/assets/"))
	#找到ttc文件
	fontPath=[f for f in os.listdir(os.getcwd()+"/assets/") if ".ttc" in f]
	font = ImageFont.truetype(os.getcwd()+"/assets/"+fontPath[0], 40)
	draw = ImageDraw.Draw(image)
	# 创建验证码对象
	code = getRandomChar()
	print(code)
	# 把验证码放到画布上，位置，内容，font
	for t in range(4):
		draw.text((60 * t + 10, random.randint(10,20)), code[t], font=font, fill=getRandomColor())
	# 填充噪点
	for _ in range(random.randint(1500,3000)):
		draw.point((random.randint(0,width), random.randint(0,height)), fill=getRandomColor())
	# 模糊处理
	image = image.filter(ImageFilter.BLUR)
	# 保存名字为验证码的图片
	image.save("".join(code) + '.jpg', 'jpeg');
	image.show()

if __name__ == '__main__':
	getCodePiture()
