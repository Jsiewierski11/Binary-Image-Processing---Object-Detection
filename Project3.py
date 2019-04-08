# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:56:11 2018

@author: Jarid
"""
import numpy as np
import cv2
import matplotlib as mp
import matplotlib.pyplot as plt
import skimage
from skimage import img_as_ubyte
from displayImage import displayImage

#Importing image as grayscale and convert to unit8 or cv2.threshold won't work
img1 = cv2.imread("neuron.jpg", 0);
img1 = img1.astype(np.uint8);

img2 = cv2.imread("Blood-cells_12.Red-blood-ce.jpg", 0);
img2 = img2.astype(np.uint8);

#Displaying Binary images
displayImage(img1, 'brg', 'Before Binary Conversion')
displayImage(img2, 'brg', 'Before Binary Conversion')


#Converting to binary images
ret1,BW_img1 = cv2.threshold(img1,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU);
#ret2,BW_img2 = cv2.threshold(img2,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU);
BW_img2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2);

#Displaying Binary images
displayImage(BW_img1, 'gray', 'After converting to Binary')
displayImage(BW_img2, 'gray', 'After converting to Binary')


##Noise reduction
#BW_img1 = cv2.fastNlMeansDenoising(BW_img1, BW_img1, 7, 21, 30);
#plt.figure();
#plt.imshow(BW_img1, cmap='gray');
#plt.show();

#Perform closing on both images
kernelClose1 = np.ones((9, 9), np.uint8);
kernelClose2 = np.ones((3, 3), np.uint8);
closing1 = cv2.morphologyEx(BW_img1, cv2.MORPH_CLOSE, kernelClose1);
closing2 = cv2.morphologyEx(BW_img2, cv2.MORPH_CLOSE, kernelClose2);

#Display after closing
displayImage(closing1, 'gray', 'After Closing')
displayImage(closing2, 'gray', 'After Closing')

#Opening Image2 and Display
kernelOpen2 = np.ones((3, 3), np.uint8)
opening2 = cv2.morphologyEx(closing2, cv2.MORPH_OPEN, kernelOpen2);
displayImage(opening2, 'gray', 'After Closing')

#Drawing Contours for image2
contours2, hierarchy2 = cv2.findContours(closing2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE);
img2_contours = cv2.drawContours(opening2, contours2, -1, (0, 255, 0), 1);
#img2_contours = cv2.bitwise_not(img2_contours);
displayImage(img2_contours, 'gray', 'drawing contours')

#Opening Image2 and Display
kernelOpen2 = np.ones((3, 3), np.uint8)
opening2 = cv2.morphologyEx(img2_contours, cv2.MORPH_OPEN, kernelOpen2);
opening2 = cv2.bitwise_not(opening2);
displayImage(opening2, 'gray', 'After Opening')

kernelOpen2 = np.ones((5, 5), np.uint8)
opening2 = cv2.morphologyEx(opening2, cv2.MORPH_OPEN, kernelOpen2)
displayImage(opening2, 'gray', 'After Opening')

#Drawing more contours
contours2, hierarchy2 = cv2.findContours(opening2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE);
img2_contours = cv2.drawContours(opening2, contours2, -1, (0, 255, 0), 1);
displayImage(img2_contours, 'gray', 'drawing contours')

#Counting connected components
nlabels1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(closing1);
nlabels2, labels2, stats2, centroids2 = cv2.connectedComponentsWithStats(opening2);

#Printing results
print ("Number of objects for neurons.jpg: " + str(nlabels1));
for x in range(len(centroids1)):
    #print ("Center of component" + str(x) + ": " + str(centroids1[x]));
    a = 1

print ("Number of objects for Red-bloodcells.jpg: " + str(nlabels2));
for x in range(len(centroids2)):
    #print ("Center of component" + str(x) + ": " + str(centroids2[x]));
    a = 1
