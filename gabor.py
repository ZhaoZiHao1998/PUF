# coding=utf-8
import matplotlib.pyplot as plt
from skimage import filters,io,color
import numpy as np
import os
import cv2
import sys

image_path   = sys.argv[1]
image_number = sys.argv[2]
number_len   = len(image_number)
def gobor (nums):
    filename= image_path + '/' + str(nums).zfill(number_len) +'.tif'
    img = io.imread(filename)#读取图像
    img_gray = color.rgb2gray(img)#RGB转灰度
    sum = 0
    for i in range(0,90,30):
        real,imag = filters.gabor(img_gray, frequency = 0.6, theta=i, bandwidth=1, sigma_x=None,sigma_y=None, n_stds=3, offset=0, cval=0)
        img_mod=np.sqrt(real.astype(float)**2+imag.astype(float)**2)
        sum = sum + img_mod/5
#print(img_mod)
    plt.imsave('D:/PUF/gabor/'+ str(nums).zfill(number_len) +'.png',sum)

def square (nums):    
    #调整尺寸为正方形
    imge = cv2.imread('D:/PUF/gabor/'+ str(nums).zfill(number_len) +'.png')
    size = (1080,1080)
    imge = cv2.resize(imge, size)
    #print(imge)
    cv2.imwrite("D:/PUF/gabor_square/"+ str(nums).zfill(number_len) +".png",imge)

if(os.path.exists(r'D:/PUF/gabor') == False):
    os.makedirs(r'D:/PUF/gabor')
for nums in range(1,int(image_number) + 1):
    gobor(nums)

if(os.path.exists(r'D:/PUF/gabor_square') == False):
    os.makedirs(r'D:/PUF/gabor_square')
for nums in range(1,int(image_number) + 1):
    square(nums)
print('gabor处理完成!!图片存储到D:/PUF/gabor和gabor_square')