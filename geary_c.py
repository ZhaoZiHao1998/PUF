# coding=utf-8
import numpy as np
import sys
import os

image_number = sys.argv[1]
#打开二进制的文件
def openfile_var(i):
	name = r'D:\\PUF\\data\\2th\\2th' + str(i).zfill(len(image_number)) + '.txt'  
	fp = open(name)
#将字符串导入
	string = fp.read().replace(' ','').replace('\n','')
	
	length = len(string)
	number =[]
	for i in range(0,length):
		number.append(int(string[i]))

	VAR  = np.var(number)
	fp.close()
	return (length,VAR,number)

def Geary_c(length,number):
	sum_w = 0
	sum_wx= 0
	for i in range(0,length):
		for j in range(0,length):
			if abs(i-j) == 1:
				w = 1
			else:
				w = 0
			sum_w = sum_w + w
			sum_wx= sum_wx + w*(number[i]-number[j])*(number[i]-number[j])
	
	c = ( (length - 1) * sum_wx ) / ( 2 * length * VAR * sum_w)
	return c
if(os.path.exists(r'D:/PUF/data/Geary_c') == False):
	os.makedirs(r'D:/PUF/data/Geary_c')
files1 = open(r'D:\\PUF\\data\\Geary_c\\Geary_c.txt','a')
for i in range(1,int(image_number) + 1):
	(length,VAR,number)=openfile_var(i)
	c=Geary_c(length,number)
	files1.write(str(c)+'\n')

files1.close()
print('Geary_c完成! 储存到D:/PUF/data/Geary_c')