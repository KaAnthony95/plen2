# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:56:42 2017

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage import filters as filters
import skimage.io as io
import scipy.ndimage as ndi
from skimage import feature

w=io.imread('x-ray.jpg',"gray")

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