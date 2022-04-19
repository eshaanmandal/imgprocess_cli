# made by Eshaan Mandal
# driver function for running the image processing cli tool
# 
#
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import helpers
import pOps
import filters
import os

menu_1 = '''
    ------------------------------------
    |   MAIN MENU                      |
    |----------------------------------|
    |    1. Enter image path (n/N)     |
    |    2. Use sample images (d/D)    |
    |    3. Exit(b/B)                  | 
    ------------------------------------
    '''
menu_2 = '''
    ------------------------------------
    |   IMAGE OPTIONS                  |
    |----------------------------------|
    |    1. Point Filters (p/P)        |
    |    2. Filters (f/F)              |
    |    3. View Image (v/V)           |
    |    4. Previous Menu (b/B)        | 
    ------------------------------------
    '''
menu_3 = '''
    ------------------------------------
    |   POINT OPERATIONS               |
    |----------------------------------|
    |    1. Invert image(i/I)          |
    |    2. Auto-contrast(a/A)         | 
    |    3. Thresholding(t/T)          | 
    |    4. Clipping(c/C)              |
    |    5. Equalize(e/E)              |
    |    6. Go to previous menu(b/B)   | 
    ------------------------------------
    '''
menu_4 = '''
    ------------------------------------
    |   FILTERS                        |
    |----------------------------------|
    |    1. Gaussian Filter (g/G)      |
    |    2. Sobel Filter (s/S)         | 
    |    3. Prewitt Filter (p/P)       | 
    |    4. Laplacian Filter (l/L)     |             
    |    5. Go to previous menu(b/B)   | 
    ------------------------------------
    '''

menu_5 = '''
    ------------------------------------
    |   OPTIONS                        |
    |----------------------------------|
    |    1. Save Image(s/S)            |
    |    2. Display Image(d/D)         |            
    |    3. Go to previous menu(b/B)   | 
    ------------------------------------
    '''
def image_options(img):
    while True:
        print(menu_5)
        choice = input("Choice(s/d/b)?").lower()
        if choice == "s":
            save_as = input("Save as : ")
            plt.imsave(save_as,img, cmap='gray')
            print("Image saved")
        elif choice == "d":
            plt.imshow(img, cmap='gray')
            plt.show()
        elif choice == "b":
            return
        else:
            print("Invaid choice")
def options(img) -> None:
    while True:
        print(menu_2)
        choice = input("Choice(p/f/v/b)?").lower()
        if choice == "p":
            while True:
                print(menu_3)
                choice = input("Choice(i/a/t/c/e/b)?").lower()
                if choice=="i":
                    new_img = pOps.invert(img)
                    image_options(new_img)
                elif choice=="a":
                    new_img = pOps.auto_contrast(img)
                    image_options(new_img)
                elif choice=="t":
                    new_img = pOps.threshold(img)
                    image_options(new_img)
                elif choice=="c":
                    new_img = pOps.clipping(img)
                    image_options(new_img)
                elif choice=="e":
                    new_img = pOps.equalize(img)
                    image_options(new_img)
                elif choice=="b":
                    break
                else:
                    print("invalid choice")
        elif choice == "f":
            while True:
                print(menu_4)
                choice = input("Choice(g/s/p/l/b)").lower()
                if choice == "g":
                    pass
                elif choice == "s":
                    print("auto-contrast")
                elif choice == "p":
                    print("threshold")
                elif choice == "l":
                    print("clip")
                elif choice=="b":
                    break
                else:
                    print("invalid choice")
        elif choice == "v":
            plt.imshow(img, cmap='gray')
            plt.show()
        else:
            return
def main():
    while True:
        print(menu_1)
        choice = input("Choice(n/d/b)? ").lower()
        if choice == "n":
            path = input("Image Path :")
            exists,img = helpers.load_image(path)
            if not exists:
                print("Image not found!")
                continue
            print("*****Image loaded successfully!*****")
            options(img)

        elif choice == "d":
            path = "./sample_images/"
            print(os.listdir(path))
            choice = input("Choose an image from the following : ")
            exists,img = helpers.load_image(os.path.join(path,choice))
            if not exists:
                print("Image does not exist")
                continue
            print("*****Image loaded successfully!*****")
            options(img)

        else:
            break


if __name__=="__main__":
    main()


