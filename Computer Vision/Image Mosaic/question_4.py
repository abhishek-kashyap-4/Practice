# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:03:59 2022

@author: kashy
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from computeH import computeH
from get_correspondences import get_correspondences
from warpImage import warpImage




'''
PAIR 2
'''
img1 = cv2.cvtColor(cv2.imread('wdc1.jpg') , cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread('wdc2.jpg') , cv2.COLOR_BGR2RGB)

pts = np.load('points.npy')
pts1 , pts2 = pts[0] , pts[1]

H = computeH(pts1,pts2)

"Please note, I have calculated H with img2 as Input for this pair."
warpIm ,mergeIm= warpImage(img2, img1, H,True)
plt.figure(12)
plt.imshow(mergeIm)

1/0


'''
PAIR 1
'''
img1 = cv2.cvtColor(cv2.imread('crop1.jpg') , cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread('crop2.jpg') , cv2.COLOR_BGR2RGB)

pts1 = np.load('cc1.npy')
pts2 = np.load('cc2.npy')


H = computeH(pts1,pts2)

"USE average_seam=True to average out seam difference at borders. Use false to retain unwarpped image resolution"
warpIm ,mergeIm= warpImage(img1, img2, H,average_seam=True)
fig = plt.figure(11)
figA = fig.add_subplot(1,2,1)
figB = fig.add_subplot(1,2,2)
figA.imshow(warpIm)
figB.imshow(mergeIm)

1/0
'''
PAIR 3
'''
img1 = cv2.cvtColor(cv2.imread('m1.jpg') , cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread('m2.jpg') , cv2.COLOR_BGR2RGB)


pts1,pts2 = get_correspondences(img1 , img2 , 10)



H = computeH(pts1,pts2)
'''
H = np.array([[ 1.14898977e+00,  9.75701684e-02,  5.09333559e+02],
       [-7.21627985e-02,  1.04797034e+00, -1.00891839e+03],
       [ 1.12508202e-04,  1.08364392e-05,  1.00000000e+00]])
'''
"Please note, I have calculated H with img2 as Input for this pair."
warpIm ,mergeIm= warpImage(img1, img2, H,True)
fig = plt.figure(10)
figA = fig.add_subplot(1,2,1)
figB = fig.add_subplot(1,2,2)
figA.imshow(warpIm)
figB.imshow(mergeIm)



1/0 




'''
PAIR 1
'''
img1 = cv2.cvtColor(cv2.imread('crop2.jpg') , cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread('crop1.jpg') , cv2.COLOR_BGR2RGB)

pts1 = np.load('cc1.npy')
pts2 = np.load('cc2.npy')

pts1 , pts2 = pts2,pts1 
img1 , img2 = img2 , img1
H = computeH(pts1,pts2)

"USE average_seam=True to average out seam difference at borders. Use false to retain unwarpped image resolution"
warpIm ,mergeIm= warpImage(img2, img1, H,average_seam=True)
fig = plt.figure(11)
figA = fig.add_subplot(1,2,1)
figB = fig.add_subplot(1,2,2)
figA.imshow(warpIm)
figB.imshow(mergeIm)



