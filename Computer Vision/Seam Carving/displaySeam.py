# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:30:42 2022

@author: kashy
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 



def displaySeam(im,seam,type1):
  '''
  HORIZONTAL or VERTICAL

  '''
  im_imposed = im.copy()
  for ind in range(len(seam)):
    val = seam[ind]
    if(type1 == "VERTICAL"):
      im_imposed[ind][val] = (0,0,0) #make this r,g,b
    elif(type1 == 'HORIZONTAL'):
      im_imposed[val][ind] = (0,0,0)
    else:
      raise Exception("type is bad")


  plt.figure(0)
  plt.imshow(im_imposed)
  plt.tight_layout()