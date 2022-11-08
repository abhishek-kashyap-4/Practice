# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:36:48 2022

@author: kashy
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 

from find_optimal_horizontal_seam import find_optimal_horizontal_seam
from cumulative_minimum_energy_map import cumulative_minimum_energy_map


def reduceHeight(im , energyImage):
  '''
   return  reducedColorImage, reducedEnergyImage
  '''
  seam = find_optimal_horizontal_seam(cumulative_minimum_energy_map(energyImage , "HORIZONTAL"))
  for ind in range(len(seam)):
    val = seam[ind]
    newrow = np.concatenate((energyImage[:val , ind] , energyImage[val+1:,ind] , np.array([0])))
    energyImage[:,ind]= newrow
    newrow = np.concatenate( (im[:val, ind] , im[val+1 :,ind] , np.array([[0,0,0]]) ))
    im[:,ind] = newrow
  return im[:-1,:,:] , energyImage[:-1,:]
  

