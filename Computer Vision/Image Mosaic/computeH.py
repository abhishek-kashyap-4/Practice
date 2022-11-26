

import cv2
import matplotlib.pyplot as plt
import numpy as np

def computeH(t1 , t2):
  '''
  t1,t2 = 2xN
  H = 3x3 Homography
  '''
  #The points I am taking are from the plot, which inverses x,y. 
  #So I need to use this.
  t1 = [[x[1],x[0]] for x in t1]
  t2 = [[x[1],x[0]] for x in t2]
   
  Temp = []
  for i in range(0, len(t1)):
    x, y = t1[i][0], t1[i][1]
    u, v = t2[i][0], t2[i][1]
    Temp.append([x, y, 1, 0, 0, 0, -u*x, -u*y, -u])
    Temp.append([0, 0, 0, x, y, 1, -v*x, -v*y, -v])
  Temp = np.asarray(Temp)
  U, S, Vh = np.linalg.svd(Temp)
  L = Vh[-1,:] / Vh[-1,-1]
  H = L.reshape(3, 3)
  return H
