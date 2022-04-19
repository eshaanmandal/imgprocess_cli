import imp
import numpy as np
import cv2 as cv
from helpers import convolve

def average_filter(img: np.array, k_size = 3):
    return cv.blur(img, (k_size, k_size))

def gaussian(img: np.array, k_size = 3):
    return cv.GaussianBlur(img, (k_size, k_size), 0)

def median_blur(img: np.array, k_size = 3):
    return cv.medianBlur(img,k_size)

def sobel(img: np.array, channel, k_size=3):
    if channel == 3:
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    sobx = cv.Sobel(img, cv.CV_64F, 1, 0, k_size)
    soby = cv.Sobel(img, cv.CV_64F, 0, 1, k_size)
    sob = np.sqrt(np.power(sobx, 2) + np.power(soby, 2))
    print(sob.shape)
    return (sob / np.max(sob)) * 255

def prewitt(img: np.array, channel: int):
    if channel == 3:
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    prewittx = cv.filter2D(img, -1, kernelx)
    prewitty = cv.filter2D(img, -1, kernely)
    prewitt = np.sqrt(np.power(prewittx, 2) + np.power(prewitty, 2))
    # print(prewitt.shape)
    prewitt = (prewitt /  np.max(prewitt)) * 255
    return prewitt.astype(int)

def laplacian(img: np.array, channel: int):
    L = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]])
    img_d = np.copy(img) 
    if channel == 3:
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        lap = cv.filter2D(img, -1, L)
        img_d[:,:,0] = img_d[:,:,0] - lap
        img_d[:,:,1] = img_d[:,:,1] - lap
        img_d[:,:,2] = img_d[:,:,2] - lap
    else:
        lap = cv.filter2D(img, -1, L)
        img_d = img_d - lap
    

    return img_d

    

    


