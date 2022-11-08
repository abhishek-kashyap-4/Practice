# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:26:48 2022

@author: kashy
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 

def find_optimal_vertical_seam(cumulativeEnergyMap):
  '''
  return verticalSeam column indexes fro each row. list of indexes, 1d array
  '''
  verticalSeam = []
  n = len(cumulativeEnergyMap)
  nj = len(cumulativeEnergyMap[0])
  init = np.argmin(cumulativeEnergyMap[0,:])
  verticalSeam.append(init)
  i = 1
  j = init
  while(len(verticalSeam) < n):
    values = []

    if(j>0 and j<nj-1):
      values = cumulativeEnergyMap[i][j-1:j+2]
      skew = np.argmin(values)
      j = j+ skew - 1
    elif(j<=0):
      values = cumulativeEnergyMap[i][j:j+2]
      skew = np.argmin(values)
      j = j+ skew
    elif(j>=nj-1):
      values = cumulativeEnergyMap[i][j-1:j+1]
      skew = np.argmin(values)
      j = j+ skew - 1
    
    verticalSeam.append(j)
    i +=1
  
  return verticalSeam