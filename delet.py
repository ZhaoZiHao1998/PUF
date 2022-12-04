# coding=utf-8
import shutil
import os

if(os.path.exists(r"D:\PUF\data") == True):
    shutil.rmtree(r"D:\PUF\data")
if(os.path.exists(r"D:\PUF\gabor") == True):
    shutil.rmtree(r"D:\PUF\gabor")
if(os.path.exists(r"D:\PUF\gabor_square") == True):
    shutil.rmtree(r"D:\PUF\gabor_square")
