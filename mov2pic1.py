import cv2,imageio,os,time

''' 这里是定义‘捕捉图像’函数的区域 '''


# 定义函数,并设置“视频名称”，“开始帧”，“结束帧”为参数
def capture_image(video,start_frame,end_frame):

	# 创立文件夹
	dirname = os.getcwd() + "/imageFolder"
	try:
		os.mkdir(dirname)
	except Exception as e:
		print("已存在该文件夹")
		dirname=dirname + str(time.localtime())
		os.mkdir(dirname)

	# 打开视频
	cap=cv2.VideoCapture(video)
	index= 0
	# 如果视频正在播放，且帧数小于“结束帧”时
	while cap.isOpened() and index<=end_frame:
		frame=cap.read()[1]   #读取每一帧
		# print(cap.read())

		if index>=start_frame:
			# 把每一帧保存到一个名为image的文件夹中
			cv2.imwrite("{}/{}.jpg".format(dirname,index),frame)
			print(u"已经保存%d帧"%index)  #输出提示

		index+=1    #每循环一次，帧数+1

def main():
	capture_image('assets/wn.mp4', 0, 10)


if __name__=="__main__":
	# print(os.getcwd())
	main()
