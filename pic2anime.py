import imageio
import os
from PIL import Image

# 安装ffmpeg，可以另起程序安装，32mb 估计需要5分钟左右
# imageio.plugins.ffmpeg.download()
# 选择视频帧地址

def resizePic(path):
	# 定义空列表
	fileList = []
	# os.listdir()函数用来返回指定文件夹中的文件名字列表
	for file in os.listdir(path):
		im = Image.open(path + file)
		im = im.resize((768, 432), Image.ANTIALIAS)
		im.save(path + file)
		print(file)
		fileList.append(path + file)
	return fileList

path = os.getcwd()+"/assets/anime/"
fileList=resizePic(path)

# 利用字符串加法避免显示过长的字符串
writer = imageio.get_writer('animation001.mp4', fps=4)
print(writer)

for im in fileList:
	writer.append_data(imageio.imread(im))

writer.close()