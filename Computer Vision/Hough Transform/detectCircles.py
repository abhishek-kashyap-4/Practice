


import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve
from collections import Counter

def detectCircles(img,radius,useGradient):
    #returns centers
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    plt.figure(1)
    plt.imshow(img,cmap='gray')
    
    #Median Blur is great at removing noise!
    img = cv2.medianBlur(img , 11)
    edge = cv2.Canny(img, 0, 200)
    
    plt.figure(2)
    plt.imshow(edge,cmap='gray')
    
    
    
    #(M,N) = img.shape
    voting_dictionary = {}
    pixels = np.argwhere(edge[:,:])
    if(useGradient):
        G_x = cv2.Sobel(edge,cv2.CV_64F,1,0)
        G_y = cv2.Sobel(edge,cv2.CV_64F,0,1)
        angle = np.arctan2(G_y, G_x)
        for x,y in pixels:
            x1 = x+ int(np.round(radius*np.cos(angle[x][y])))
            y1 = y+ int(np.round(radius*np.sin(angle[x][y])))
            x2 = x - int(np.round(radius*np.sin(angle[x][y])))
            y2 = y - int(np.round(radius*np.cos(angle[x][y])))
            
            if((x1,y1) not in voting_dictionary):
                voting_dictionary[(x1,y1)] =1
            else:
                voting_dictionary[(x1,y1)] += 1
                
            if((x2,y2) not in voting_dictionary):
                voting_dictionary[(x2,y2)] =1
            else:
                voting_dictionary[(x2,y2)] += 1
    else:
        for x,y in pixels:
            for i in range(0,360,10):
                t = i*np.pi/180
                x1 = x + int(np.round(radius*np.cos(t)))
                y1 = y + int(np.round(radius*np.sin(t)))
                if((x1,y1) not in voting_dictionary):
                    voting_dictionary[(x1,y1)] =1
                else:
                    voting_dictionary[(x1,y1)] += 1
            
        
            
    Accum = np.zeros(img.shape) 
    for x,y in voting_dictionary:
        aa,bb = img.shape    
        if(x>=aa or y>=bb):
            continue
        Accum[x][y] =  voting_dictionary[(x,y)]
    
    plt.figure(4)
    plt.imshow(Accum)
    plt.title("Accumulator array, radius = {}".format(radius))
    fig, ax = plt.subplots()
    plt.imshow(img)
    max_n = dict(Counter(voting_dictionary).most_common(1))
    for x,y in max_n:
        ax.add_patch(plt.Circle((y,x),radius,color=(1,0,0),fill=False))
    plt.title('The most Voted Circle')
        
    
    fig, ax = plt.subplots()
    plt.imshow(img)
    max_n = dict(Counter(voting_dictionary).most_common(10))
    for x,y in max_n:
        ax.add_patch(plt.Circle((y,x),radius,color=(1,0,0),fill=False))
    plt.title('10 most voted circles')
    plt.show()
        
    return Accum , max_n


img = cv2.imread('egg.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

Accum , max_n = detectCircles(img ,60, False)

'''
Optional: execute for post processing accumulator array

n , bins, patches = plt.hist(Accum.flatten())
indexes = np.argwhere(Accum>2.8)
fig, ax = plt.subplots()
plt.imshow(img)
for row in indexes:
    x,y = row
    ax.add_patch(plt.Circle((y,x),50,color=(1,0,0),fill=False))
plt.show()
    
'''

    

