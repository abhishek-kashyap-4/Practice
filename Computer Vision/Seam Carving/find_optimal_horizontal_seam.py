# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:29:08 2022

@author: kashy
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 



def find_optimal_horizontal_seam(cumulativeEnergyMap):
  '''
  return horizontalSeam row indexes for each column. list of indexes, 1darray
  '''
  horizontalSeam = []
  ni = len(cumulativeEnergyMap)
  n = len(cumulativeEnergyMap[0])
  init = np.argmin(cumulativeEnergyMap[:,0])
  horizontalSeam.append(init)
  j = 1
  i = init
  while(len(horizontalSeam) < n):
    values = []

    if(i>0 and i<ni-1):
      values = cumulativeEnergyMap[:,j][i-1:i+2]
      skew = np.argmin(values)
      i = i+ skew - 1
    elif(i<=0):
      values = cumulativeEnergyMap[:,j][i:i+2]
      skew = np.argmin(values)
      i = i+ skew
    elif(i>=ni-1):
      values = cumulativeEnergyMap[:,j][i-1:i+1]
      skew = np.argmin(values)
      i = i+ skew - 1
    
    horizontalSeam.append(i)
    j +=1
  
  return horizontalSeam