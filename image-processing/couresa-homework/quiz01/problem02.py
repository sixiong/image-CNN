#-*- encoding:utf8 -*-
import Image
import numpy as np
import pylab

'''
加载一个图像，然后进行图像的像素的简单
的空间3x3的平均水平。换句话说，通过在其
3×3邻域的平均值的替换每个像素的值
'''

#求n邻域的平均值
def getAverageValue(arr,i,j,k,n):
	sum = 0
	temp = []
	result = 0
	try:
		half = n/2
		for l in range(n):
			for m in range(n):
				temp.append(arr[i-half+l][j-half+m][k])
				
	except Exception, e:
		pass
	else:
		pass
	finally:
		for t in temp:
			sum += t
		return sum * 1.0 /len(temp)

imageTestPath = "C:\\Users\\sxiong\\Pictures\\1.jpg"
im = Image.open(imageTestPath)
arr=np.array(im)

shapes = arr.shape
for i in range(shapes[0]):
	for j in range(shapes[1]):
		for k in range(shapes[2]):
			# arr[i][j][k] = getAverageValue(arr,i,j,k,3)
			# arr[i][j][k] = getAverageValue(arr,i,j,k,10)
			arr[i][j][k] = getAverageValue(arr,i,j,k,20)

pylab.imshow(arr)
pylab.show()


