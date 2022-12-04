# coding=utf-8
import os
import sys

path   = sys.argv[1]
number = sys.argv[2]
#path   = "D:\\实验\\实验数据\\CuPc阵列\\same"
filename_list = os.listdir(path)
zfillnumber   = len(number)
#print(filename_list)
temp = 1
for i in filename_list:
	os.rename( path + '\\' + i ,path + '\\' + str(temp).zfill(zfillnumber)+'.tif')
	temp = temp + 1
