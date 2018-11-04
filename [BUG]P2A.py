'''
参考文档：https://www.kancloud.cn/aollo/aolloopencv/259610

'''

import cv2,os
from PIL import Image

def read_all_pic(folderName):
	#读取文件夹中的所有图片文件名字
	orginPath=os.getcwd()

	os.chdir(folderName)
	#如果存在该文件夹，进入该文件夹，并读取所有图片，截取后缀
	picList=[p for p in os.listdir() if ".jpg" in p or ".png" in p]
	# print(picList)
	os.chdir(orginPath)
	return picList

def main():

	folderName = os.getcwd()+"/assets/anime/"
	picList=read_all_pic(folderName)
	fps = 4    #保存视频的FPS，可以适当调整
	img=Image.open(folderName+picList[0])
	size=img.size

	#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
	# fourcc = cv2.VideoWriter_fourcc(*'DVIX')
	# fourcc = cv2.VideoWriter_fourcc(*'XVID')
	fourcc=cv2.VideoWriter_fourcc('M', 'P','E','G')
	videoWriter = cv2.VideoWriter('anime.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸


	for pic in picList:
		print(folderName+pic)
		frame = cv2.imread(folderName+pic)
		videoWriter.write(frame)
	videoWriter.release()

if __name__ == '__main__':
    main()