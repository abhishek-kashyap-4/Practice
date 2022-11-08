
import numpy as np
import cv2

from quantizeHSV import quantizeHSV

def getHueHists(origImg,k):
  
  hsv_image =  cv2.cvtColor(origImg , cv2.COLOR_RGB2HSV)  
  hsv_array = np.float32(hsv_image.reshape((-1, 3)))
  hue  = hsv_array[:,0]
  
  outputImg , _ = quantizeHSV(origImg,k)
  outputImg =  cv2.cvtColor(outputImg , cv2.COLOR_RGB2HSV)  
  
  return hue , outputImg.reshape(-1,3)[:,0]
  
