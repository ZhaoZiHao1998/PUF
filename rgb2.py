# coding=utf-8
from PIL import Image
#from cv2 import sqrt
import numpy as np
import sys
import os
import math

bit_width   = sys.argv[1]
image_number= sys.argv[2]

kuan        = int(math.sqrt(int(bit_width)))
chang       = int(math.sqrt(int(bit_width))) #把图片分成多少份

path1       = r"D:/PUF/gabor_square"
data_path   = r"D:/PUF/data"
sumrgb_path = r"D:/PUF/data/sumrgb"
avg_path    = r"D:/PUF/data/avg"
twoth_path  = r"D:/PUF/data/2th"
maxmin_path = r"D:/PUF/data/maxmin"
if(os.path.exists(r'D:/PUF/data') == False):
	os.makedirs(data_path)
	os.makedirs(sumrgb_path)
	os.makedirs(avg_path)
	os.makedirs(twoth_path)
	os.makedirs(maxmin_path)
#path1 = "D:\\实验\\实验数据\\CuPc阵列\\new_gobor_square\\"   # 图片路径
files5=open(data_path + '/' +'num01.txt','a')

#导入图片并计算像素和长宽的函数
def InputImage(i):
	name = path1 + "/" + str(i).zfill(len(image_number)) + '.png'
	im 	 = Image.open(name)#打开图片
	pix  = im.load()#导入像素

	width= im.size[0]#获取宽度
	w    = list(range(0,width+1,int(width/kuan))) #将宽度分为kuan份
#print(w)

	height= im.size[1]#获取长度
	h     = list(range(0,height+1,int(height/chang))) #将长度分为kuan份
	return (pix,width,w,height,h)
#print(h)
#计算中位数

def Newfiles(i):
	files1=open(sumrgb_path + '/' + 's'      + str(i).zfill(len(image_number)) + '.txt' , 'a')#打开存rgb值的文件，如果不存在就创建
	files2=open(avg_path    + '/' + 'avg'    + str(i).zfill(len(image_number)) + '.txt' , 'a')
	files3=open(twoth_path  + '/' + '2th'    + str(i).zfill(len(image_number)) + '.txt' , 'a')
	files4=open(maxmin_path + '/' + 'maxmin' + str(i).zfill(len(image_number)) + '.txt' , 'a')
	return (files1,files2,files3,files4)


# 分单元存储数据
for i in range(1,int(image_number) + 1):
	(pix,width,w,height,h)=InputImage(i)
	(files1,files2,files3,files4)=Newfiles(i)
	middletemp = []
	for n1 in range(kuan):
		for n2 in range(chang):	
			S = 0 #初始化sum
			for x in range(w[n1],w[n1+1]):   
				for y in range(h[n2],h[n2+1]):     
					r, g, b = pix[x, y]#pix获取rgb值	
					s = b + g
					#rgb=(r,g,b)
					#files1.write(str(rgb)+"\n")#把rgb值写入文件demo.close()
					files1.write(str(s)+"\n")   #把rgb中总值写入文件
					S = s + S #计算sum
			S = S/(width*height/(kuan*chang))   #计算平均值
			middletemp.append(S)
			files2.write(str(S)+'\n')           #将kuan*kuan个单元的平均g值写入文件
	files1.close()
	files2.close()

	one  = 0  #初始化0，1计数
	zero = 0

	median = round(np.median(middletemp))  #寻找平均值中的中位数
#将平均值导入并转化为二进制
	temp = 0
	for line in open(avg_path + '/' + 'avg' + str(i).zfill(len(image_number)) + '.txt'):
	#判断与中位数的对比，并写入0 1
		if float(line.strip('\n')) >= int(median) :
			files3.write(str(1)+' ')
			one  = one + 1
		else:
			files3.write(str(0)+' ')
			zero = zero + 1	
		#将文件写成矩阵形式
		if temp == (kuan-1):
			files3.write('\n')
			temp = 0
		else:
			temp = temp + 1
	files3.close()
	files4.write('\n'+'num_1: '+str(one)+'; '+'num_0: '+str(zero))
	files5.write(str(one/(one+zero))+'\n')
	files4.close()


files5.close()
print('处理完成! \n')
print('二进制矩阵储存到D:/PUF/data/2th \n')
print('像素平均值储存到D:/PUF/data/avg \n')
print('像素总和储存到D:/PUF/data/sumrgb \n')
print('0和1的分布个数储存到D:/PUF/data/maxmin \n')
print('1个数/0个数储存到D:/PUF/data/num01.txt \n')