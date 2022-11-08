# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:13:06 2022

@author: kashy
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 

def cumulative_minimum_energy_map(energyImage,seamDirection):
  '''
  return cumulativeEnergyMap in vertical or horizontal directions.
  '''
  assert seamDirection == "HORIZONTAL" or seamDirection == "VERTICAL"
  ni = len(energyImage)
  nj = len(energyImage[0])
  if(seamDirection == "HORIZONTAL"):
    energyImage = energyImage.T
    ni, nj = nj,ni
  
  for i in range(ni-2,-1,-1):
    
    for j in range(0,nj):
      values = []
      values.append(energyImage[i+1][j])
      if(j>0):
        values.append(energyImage[i+1][j-1])
      if(j<nj-1):
        values.append(energyImage[i+1][j+1])
      energyImage[i][j] += min(values)
  if(seamDirection == "HORIZONTAL"):
    return energyImage.T
  return energyImage