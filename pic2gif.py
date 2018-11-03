import imageio,os

#定义函数,并设置“开始帧”，“结束帧”，“gif的速率”为参数
def saveGif(start_frame,end_frame,gif_speed,folderName,filename):
	#创建frames列表
	frames=[]
	#当i在开始帧到结束帧之间
	if folderName in os.listdir():
		os.chdir(folderName)
		#如果存在该文件夹，进入该文件夹，并读取所有图片，截取后缀
		picList=[p for p in os.listdir() if ".jpg" in p or ".png" in p]

		#如果输入的结尾帧数多于图片数量，则=图片数量
		if end_frame>len(picList):
			end_frame=len(picList)
		# hz=picList[0].split(".")[1]
		for i in range(start_frame,end_frame):
			# d读取保存下来的静态帧
			# s=os.getcwd()+folderName+"/{}.{}".format(str(frame),hz)
			img=imageio.imread((picList[i]))
			frames.append(img)
			#加入列表
			print("f%d正在加入列表"%i)
		frames.reverse()
		# random.shuffle(frames)
		print("正在生成gif中...")
		imageio.mimsave(filename,frames,fps=gif_speed)	  #利用帧数列表制作gif，设置fps也就是帧速率为参数
	else:
		print("该文件夹不存在")

if __name__=="__main__":
	# print(os.getcwd())
	# saveGif(0,10,5,'2659',"out.gif")