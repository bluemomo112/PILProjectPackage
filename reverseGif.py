# 导入库
from PIL import Image, ImageSequence


def  reverse_gif(filepath,gifname):
	#打开图片
	im=Image.open(filepath)

	#判断图片是否为动态图
	if im.is_animated:
	 #新建列表
	    frames=[]
	 #读取图像中的每一帧
	    for f in ImageSequence.Iterator(im):
	    #将图像添加到列表中
	          f=f.copy
	          frames.append(f)
	 #将列表反向
	    frames.reverse()
	 #保存图像
	    frames[0].save(gifname, save_all=True, append_images=frames[1:])

def main():
	reverse_gif("","")

if __name__ == '__main__':
	main()