# coding=utf-8
import sys
import os

image_number = sys.argv[1]
#打开二进制的文件
def openfile(i):
	name = r'D:\\PUF\\data\\2th\\2th' + str(i).zfill(len(image_number)) + '.txt'  
	fp1 = open(name)
#将字符串导入
	string1 = fp1.read().replace(' ','').replace('\n','')
	fp1.close()
	return string1
#string2 = fp2.read().replace(' ','').replace('\n','')

#
def xor(string1,string2):
	temp   = 0
	length = len(string1)
	for i in range(0,length):
		if string1[i] != string2[i]:
			temp = temp + 1
		else:
			temp = temp		
	return (temp,temp/length)

if(os.path.exists(r'D:/PUF/data/HD') == False):
	os.makedirs(r'D:/PUF/data/HD')
files1 = open(r'D:\\PUF\\data\\HD\\HD.txt','a')
files2 = open(r'D:\\PUF\\data\\HD\\nomal_HD.txt','a')
for i in range(1,int(image_number) + 1):
	for j in range(i+1,int(image_number) + 1):
		string1 = openfile(i)
		string2 = openfile(j)
		(HD,nomal_HD) = xor(string1,string2)
		files1.write(str(HD)+'\n')
		files2.write(str(nomal_HD)+'\n')

files1.close()
files2.close()
print('汉明距离计算完成! 储存到D:/PUF/data/HD')