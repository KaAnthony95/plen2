# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 08:09:28 2017

@author: eric
"""
import matplotlib.pyplot as plt
import numpy as np
from skimage import filters as filters
import skimage.io as io
import scipy.ndimage as ndi
from skimage import feature

w=io.imread('ic.tif')

b=np.array([[1,0,-1],\
            [1,0,-1],\
            [1,0,-1]])
y=ndi.convolve(w,b,mode='constant') 
fig = plt.figure(figsize= (15,8))
ax1 = fig.add_subplot(1,2,1);io.imshow(w)
ax1 = fig.add_subplot(1,2,2);io.imshow(np.abs(y/255))
y1=ndi.uniform_filter(w,[3,3],mode='constant')
y1=ndi.convolve(y1,b,mode='constant') 
fig = plt.figure(figsize= (15,8))
ax1 = fig.add_subplot(1,2,1);io.imshow(w)
ax1 = fig.add_subplot(1,2,2);io.imshow(y1>200)

wh = filters.hsobel(w)
wv = filters.vsobel(w)
wall = filters.sobel(w)
fig = plt.figure(figsize= (15,8))
ax1 = fig.add_subplot(2,2,1);io.imshow(w)
plt.title('original', fontsize=10)
ax1 = fig.add_subplot(2,2,2);plt.imshow(wh*10,'gray')
plt.title('Sobel (x direction)', fontsize=10)
ax1 = fig.add_subplot(2,2,3);plt.imshow(wv*10,'gray')
plt.title('Sobel (y direction)', fontsize=10)
ax1 = fig.add_subplot(2,2,4);plt.imshow(wall*10,'gray')
plt.title('Sobel filter', fontsize=10)

wlap = filters.laplace(w)
fig = plt.figure(figsize= (15,8))
ax1 = fig.add_subplot(1,2,1);io.imshow(w)
plt.title('original', fontsize=20)
ax1 = fig.add_subplot(1,2,2);plt.imshow(wall*10,'gray')
plt.title('laplace', fontsize=20)

edges1 = feature.canny(w)
edges2 = feature.canny(w, sigma=3)
fig = plt.figure(figsize= (15,8))
ax1 = fig.add_subplot(1,3,1);io.imshow(w)
ax1 = fig.add_subplot(1,3,2);io.imshow(edges1)
ax1 = fig.add_subplot(1,3,3);io.imshow(edges2)



