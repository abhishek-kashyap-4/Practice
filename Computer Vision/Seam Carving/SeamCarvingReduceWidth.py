# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 00:53:39 2022

@author: kashy
"""

'''
load a colored image inputSeamCarvingPrague.jpg
  reducewidth by 100 pixels.
  save as outputReduceWidthPrague.png
Load a colored image  inputSeamCarvingMall.jpg
  reducewidth by 100 pixels
  save as outputReduceWidthMall.png
'''
images = ('inputSeamCarvingPrague.jpg' , 'inputSeamCarvingMall.jpg')
outputnames = ("outputReduceWidthPrague.png" , "outputReduceWidthMall.png")
figures = (1,2)
for im_ind in range(len(images)):
  im = cv2.imread(images[im_ind])
  im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

  plt.figure(1)
  plt.imshow(im)

  for i in range(100):
    energyImage = energy_image(im)
    im , energyImage = reduceWidth(im , energyImage)
  plt.figure(figures[im_ind])
  plt.imshow(im)
  plt.imsave(outputnames[im_ind] , im)