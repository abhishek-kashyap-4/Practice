# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:31:01 2022

@author: kashy
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 

from find_optimal_vertical_seam import find_optimal_vertical_seam
from cumulative_minimum_energy_map import cumulative_minimum_energy_map

def reduceWidth(im,energyImage):
  '''
  DOUBLE, UNIT8
   return  reducedColorImage, reducedEnergyImage - not correlated?
  '''
  
  seam = find_optimal_vertical_seam(cumulative_minimum_energy_map(energyImage , "VERTICAL"))
  for ind in range(len(seam)):
    val = seam[ind]
    newrow = np.concatenate((energyImage[ind , :val] , energyImage[ind,val+1:] , np.array([0])))
    energyImage[ind]= newrow
    newrow = np.concatenate( (im[ind,:val] , im[ind,val+1 :] , np.array([[0,0,0]]) ))
    im[ind] = newrow
  return im[:,:-1,:] , energyImage[:,:-1]
