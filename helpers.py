import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def load_image(path_to_image: str):
    try:
        return (True, cv.cvtColor(cv.imread(path_to_image), cv.COLOR_BGR2GRAY))
    except cv.error as error:
        return (False, np.zeros(2))
    
    