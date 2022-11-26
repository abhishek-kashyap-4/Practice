
import cv2
import matplotlib.pyplot as plt
import numpy as np



def get_correspondences(img1,img2,num=8,save=False):
    print("Give {} points. Select points alternately from 2 images.".format(num))
    fig = plt.figure()
    figA = fig.add_subplot(1,2,1)
    figB = fig.add_subplot(1,2,2)
    # Display the image
    figA.imshow(img1,origin='upper')
    figB.imshow(img2,origin='upper')
    pts = plt.ginput(num,timeout=0)
    plt.close()
    print("Making Mosaic...")
    pts = [list(t) for t in pts]
    pts1 = pts[0::2]
    pts2 = pts[1::2]
    
    if(save):
        np.save('wdc1.npy',pts1)
        np.save('wdc2.npy',pts2)
    return pts1 , pts2
