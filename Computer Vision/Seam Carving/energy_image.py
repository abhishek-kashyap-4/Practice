# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:08:39 2022

@author: kashy
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2 
def energy_image(im):

  '''
  returns energyImage
  '''
  nx , ny , z = im.shape
  im = np.sum(im,axis=2)

  #kernel = np.array([-1,1])

  im_padded = np.zeros( (nx+1 , ny+1) )
  im_padded = im_padded.astype('double')
  im_padded[0:nx , 0:ny] = im
  im = im_padded.copy()
  pad1 = 0
  pad2 = 1
  energyImage = np.zeros( (nx, ny ) )
  
  for i in range(0,nx):
    for j in range(0,ny):

      wrty = im[i,j+1] - im[i,j]
      wrty /= 3

      wrtx  = im[i+1,j] - im[i,j]
      wrtx /= 3
      
      energyImage[i,j] = abs(wrtx) + abs(wrty)
  #energyImage = energyImage[pad1:-pad2,pad1:-pad2 ]
  assert energyImage.shape == (nx , ny)
  
  return energyImage


