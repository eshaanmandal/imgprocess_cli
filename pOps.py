from hashlib import new
import numpy as np
import cv2 as cv
# all the point operations that can be performed on an image are defined here

def invert(img: np.array, channel: int):
    if channel == 3:
        img[:,:,0] = 255 - img[:,:,0]
        img[:,:,1] = 255 - img[:,:,1]
        img[:,:,2] = 255 - img[:,:,2]
    else:
        img = 255 - img
    
    return img


def auto_contrast(img: np.array, channel: int):
    if channel == 3: 
       img[:,:,0] = img[:,:,0] - np.min(img[:,:,0]) * (255)/(np.max(img[:,:,0]) - np.min(img[:,:,0]))
       img[:,:,1] = img[:,:,1] - np.min(img[:,:,1]) * (255)/(np.max(img[:,:,1]) - np.min(img[:,:,1]))
       img[:,:,2] = img[:,:,2] - np.min(img[:,:,2]) * (255)/(np.max(img[:,:,2]) - np.min(img[:,:,2]))
    else:
         img = img - np.min(img) * (255)/(np.max(img) - np.min(img))
    return img

def threshold(img: np.array, t_point: int):
    img[img >= t_point] = 255
    img[img < t_point] = 0
    return img

def equalize(img: np.array, channel: int):
    if channel == 3:
        img[:,:,0] = cv.equalizeHist(img[:,:,0])
        img[:,:,1] = cv.equalizeHist(img[:,:,1])
        img[:,:,2] = cv.equalizeHist(img[:,:,2])
    else:
        img = cv.equalizeHist(img)
    return img

def clipping(img: np.array, r1: int, r2: int):
    img[(img >= r1) & (img <= r2)] = 255
    img[(img < r1) & (img > r2)] = 0
    return img
