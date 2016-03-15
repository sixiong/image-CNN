#-*- encoding:utf8 -*-
import Image
import numpy as np
import pylab

'''
旋转图像
'''

imageTestPath = "C:\\Users\\sxiong\\Pictures\\1.jpg"
im = Image.open(imageTestPath)
# out = im.rotate(45)
# out = im.rotate(90)
# out = im.rotate(270)
out = im.transpose(Image.ROTATE_90)

arr = np.array(out)

pylab.imshow(arr)
pylab.show()


