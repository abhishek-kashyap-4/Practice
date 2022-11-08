import numpy as np
import cv2

def quantizeHSV(origImg, k):
    
  hsv_image = cv2.cvtColor(origImg, cv2.COLOR_RGB2HSV)
  hsv_flat = np.float32(hsv_image.reshape((-1, 3)))
  
  hue  = hsv_flat[:,0].copy()
  
  #kmeans algo
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 500, 0.2)
  _, labels, (meanHues) = cv2.kmeans(hue, k,None ,criteria = criteria , attempts = 10, flags = cv2.KMEANS_RANDOM_CENTERS)
  meanHues = np.uint8(meanHues)
  labels = labels.flatten()
  hsv  = meanHues[labels.flatten()]
  ####################
  
  hsv_flat[:,0] = hsv.flatten()
  hsv_flat = np.uint8(hsv_flat)
  outputImg = hsv_flat.reshape(origImg.shape)
  outputImg = cv2.cvtColor(outputImg, cv2.COLOR_HSV2RGB)
  
  return outputImg , meanHues