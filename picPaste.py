from PIL import Image
from PIL import ImageFont,ImageDraw
import mov2pic1 as m2p
import random,os


''' 这里定义‘黏贴表情’函数的区域 '''


def draw_emoi(img,emoiFile,size=(50,50),xy=(0,0),outFile="picPemoi.jpg"):

	emoi = Image.open(emoiFile)
	emoi = emoi.resize(size)

	print(xy)
	if ".png" in emoiFile:
		emoi = emoi.convert("RGBA")

		r, g, b, a = emoi.split()
		img.paste(emoi, xy, mask=a)

	elif ".jpg" in emoiFile:
		img.paste(emoi, xy)

	img.save("outFolder/"+outFile)  # 保存合成图片



def read_all_pic(folderName):
	#读取文件夹中的所有图片文件名字
	orginPath=os.getcwd()
	if folderName in os.listdir():
		os.chdir(folderName)
		#如果存在该文件夹，进入该文件夹，并读取所有图片，截取后缀
		picList=[p for p in os.listdir() if ".jpg" in p or ".png" in p]
	os.chdir(orginPath)
	return picList



''' 这里定义‘黏贴文字’函数的区域 '''

def drawText(folderName,text,color=(0,0,0),fontSize=50,outFileName="picPasteText.jpg"):
	font_set = ImageFont.truetype('assets/msyhbd.ttc', textSize, encoding='unic')
	picList=read_all_pic(folderName)
	img = Image.open(folderName + "/" + picList[i])

	if ".jpg" in picList[i]:
		draw = ImageDraw.Draw(img, mode="RGB")
	elif ".png" in picList[i]:
		draw = ImageDraw.Draw(img, mode="RGBA")
	draw.text(xy, text, fill=color, font=font_set)



def draw_moving_thing(folderName,start,end,contentName,emoiSize=(50,50),textSize=50,xy=(0,0)):
	if folderName in os.listdir():
		# print(type(contentName)==list)
		picList=read_all_pic(folderName)
		x, y = xy

		if  type(contentName) == list:
			font_set = ImageFont.truetype('assets/msyhbd.ttc', textSize, encoding='unic')
			random_Num = random.randint(0, len(contentName) - 1)
			random_Text = contentName[random_Num]
			text_width, text_height = font_set.getsize(random_Text)


		#读取所有底层图片
		for i in range(start, end):
			print(i)
			img = Image.open(folderName+"/"+picList[i])
			picSize = img.size


			if ".png" in contentName or ".jpg" in contentName:
				print("1")

				if x >= picSize[0]:
					x = 0
					y = random.randint(0, picSize[1] - emoiSize[1])
				else:
					x += 30

				draw_emoi(img,contentName,(100,100),(x,y),str(i)+".jpg")


			elif type(contentName) == list:

				if ".jpg" in picList[i]:
					draw = ImageDraw.Draw(img, mode="RGB")
				elif ".png" in picList[i]:
					draw = ImageDraw.Draw(img, mode="RGBA")


				# y = 1/2*picSize[1] - text_height

				if x - text_width >= picSize[0]:
					x = 0
					y = random.randint(0, picSize[1] - text_height)
					random_Num = random.randint(0, len(contentName))
					random_Text = contentName[random_Num]
				else:
					x += 40

				draw.text((x,y), random_Text, fill=(255,255,255), font=font_set)
				# 保存合成图片
				img.save("outFolder/" + str(i) + ".jpg")




	else:
		print("该文件夹不存在")


def main():
	# img = Image.open("imageFolder/0.jpg")
	# draw_emoi(img, "assets/01.jpg",(100,200))
	# m2p.main()
	textList = ['疯狂为博士打call', "哈哈哈哈哈哈", "博士好棒棒", "6666666666666", '为大佬献上膝盖！', '前方高能', "我们爱夏博士"]
	# draw_moving_thing("imageFolder",0,10,"assets/01.jpg")
	draw_moving_thing("imageFolder", 0, 9, textList)

if __name__=="__main__":
	main()
