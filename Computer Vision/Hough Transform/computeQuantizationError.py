import numpy as np


def computeQuantizationError(origImg , quantizedImg):
  
  origImg = np.float32(origImg)
  quantizedImg = np.float32(quantizedImg)
  
  difference = origImg - quantizedImg  
  difference = difference **2
  return np.sum(difference)
  
  