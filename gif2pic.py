`from PIL import Image,ImageSequence
import os,time

def divede_gif(filename):
	im=Image.open(filename)
	#创立文件夹
	dirname=os.getcwd()+"/imageFolder"

	try:
		os.mkdir(dirname)
	except Exception as e:
		print("已存在该文件夹")
		os.mkdir(dirname+str(time.localtime()))

	index=1
	for frame in ImageSequence.Iterator(im):
		frame.save("divideImage/"+"%d.png"%index)
		index+=1

if __name__ == '__main__':
	divede_gif('reverse_gif.gif')
	print("finish")
