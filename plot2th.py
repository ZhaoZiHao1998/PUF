# coding=utf-8
import numpy as np
import seaborn
import matplotlib.pyplot as plt
from PIL import Image 
import sys
import os

image_number = sys.argv[1]

def file2array(path, delimiter=' '):     # delimiter是数据分隔符
    fp = open(path, 'r', encoding='utf-8')
    string = fp.read()              # string是一行字符串，该字符串包含文件所有内容
    fp.close()
    row_list = string.splitlines()  # splitlines默认参数是‘\n’
    data_list = [[float(i) for i in row.strip().split(delimiter)] for row in row_list]
    return np.array(data_list)

def image_border(src, dst, loc='a', width=2, color=(0, 0, 0)):
    '''
    src: (str) 需要加边框的图片路径
    dst: (str) 加边框的图片保存路径
    loc: (str) 边框添加的位置, 默认是'a'(
        四周: 'a' or 'all'
        上: 't' or 'top'
        右: 'r' or 'rigth'
        下: 'b' or 'bottom'
        左: 'l' or 'left'
    )
    width: (int) 边框宽度 (默认是3)
    color: (int or 3-tuple) 边框颜色 (默认是0, 表示黑色; 也可以设置为三元组表示RGB颜色)
    '''
    # 读取图片
    img_ori = Image.open(src)
    w = img_ori.size[0]
    h = img_ori.size[1]

    # 添加边框
    if loc in ['a', 'all']:
        w += 2*width
        h += 2*width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (width, width))
    elif loc in ['t', 'top']:
        h += width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (0, width, w, h))
    elif loc in ['r', 'right']:
        w += width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (0, 0, w-width, h))
    elif loc in ['b', 'bottom']:data = file2array(name1)
       # h += width
        #img_new = Image.new('RGB', (w, h), color)
       # img_new.paste(img_ori, (0, 0, w, h-width))
    elif loc in ['l', 'left']:
        w += width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (width, 0, w, h))
    else:
        pass

    # 保存图片
    img_new.save(dst)

if(os.path.exists(r'D:/PUF/data/picture') == False):
    os.makedirs(r'D:/PUF/data/picture')
for i in range(1,int(image_number) + 1):
	name1 = r"D:\\PUF\\data\\2th\\"+'2th'+str(i).zfill(len(image_number))+'.txt'
	name2 = r"D:\\PUF\\data\\picture\\"
	data = file2array(name1)

	seaborn.heatmap(data,xticklabels=0,yticklabels=0,cmap='Greys',cbar=False,square=True)
	plt.savefig(name2+str(i).zfill(len(image_number))+'.jpg',dpi=300,bbox_inches='tight')
	image_border(name2+str(i).zfill(len(image_number))+'.jpg',name2+str(i).zfill(len(image_number))+'.jpg', 'a', 10, color=(0, 0, 0))

print('图片绘制完成! 储存到D:/PUF/data/picture')