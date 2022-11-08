

import cv2
import numpy as np
import matplotlib.pyplot as plt



from quantizeHSV import quantizeHSV
from quantizeRGB import quantizeRGB
from computeQuantizationError import computeQuantizationError
from getHueHists import getHueHists



origImg = cv2.imread('fish.jpg')
origImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2RGB)
plt.imshow(origImg)
plt.show()

k=3

plt.figure(1)
kmeans_rgb , _ = quantizeRGB(origImg , k)
plt.imshow(kmeans_rgb)
plt.title("RGB K means clustering with k=3 ")

plt.figure(2)
kmeans_hsv , means = quantizeHSV(origImg , k)
plt.imshow(kmeans_hsv)
plt.title("HSV K means clustering with k =3")
plt.show()

print("RGB K means error with k=3")
print(computeQuantizationError(origImg , kmeans_rgb))

print("HSV K means error with k=3")
print(computeQuantizationError(origImg , kmeans_hsv))

#print(means)

plt.figure(3)


############Get Histograms
normal , clustered = getHueHists(origImg , k)

plt.hist(normal)
plt.title("Uniform bins for k=3")


plt.figure(6)
plt.hist(normal,bins = k)
plt.title("Uniform bins for k=3")

plt.figure(4)
plt.hist(clustered)
plt.title("Clustered bins for k=3")

plt.show()


    
    
    
  