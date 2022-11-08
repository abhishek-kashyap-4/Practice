# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 00:55:57 2022

@author: kashy
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 


from energy_image import energy_image
from reduceHeight import reduceHeight


'''
repeat above and do height.

'''
images = ('inputSeamCarvingPrague.jpg' , 'inputSeamCarvingMall.jpg')
outputnames = ("outputReduceHeightPrague.png" , "outputReduceHeightMall.png")
figures = (1,2)
for im_ind in range(len(images)):
  im = cv2.imread(images[im_ind])
  im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

  plt.figure(1)
  plt.imshow(im)

  for i in range(100):
    energyImage = energy_image(im)
    im , energyImage = reduceHeight(im , energyImage)
  plt.figure(figures[im_ind])
  plt.imshow(im)
  plt.imsave(outputnames[im_ind] , im)

