#-*- encoding:utf8 -*-
import Image
import numpy as np
import pylab
'''
写能够降低强度级的数目的图像在从256至2，
在2强度水平的期望数量的需要是一个变量输入
到程序的整数幂的一个计算机程序。
'''
imageTestPath = "C:\\Users\\sxiong\\Pictures\\1.jpg"
im = Image.open(imageTestPath)
print im.size
arr=np.array(im)
# print arr
i = 0
print arr[0][0][0]
shapes = arr.shape
for i in range(shapes[0]):
	for j in range(shapes[1]):
		for k in range(shapes[2]):
			arr[i][j][k] = int(arr[i][j][k]/128)*128

pylab.imshow(arr)
pylab.show()


