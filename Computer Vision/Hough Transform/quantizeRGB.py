
import numpy as np
import cv2



def quantizeRGB(origImg , k):
    shape = origImg.shape
    origImg = np.float32(origImg.reshape((-1, 3)))
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 500, 0.2)
    __, labels, (meanColors) = cv2.kmeans(origImg, k,None ,criteria = criteria , attempts = 10, flags = cv2.KMEANS_RANDOM_CENTERS)
    meanColors = np.uint8(meanColors)
    labels = labels.flatten()
    outputImg = meanColors[labels.flatten()]
    outputImg = outputImg.reshape(shape)
    
    return outputImg , meanColors
    