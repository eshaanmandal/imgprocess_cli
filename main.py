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
    |    3. About this program (a/A)   |
    |    4. Help (h/H)                 |
    |    5. Exit(b/B)                  | 
    ------------------------------------
    '''
menu_2 = '''
    ------------------------------------
    |   IMAGE OPTIONS                  |
    |----------------------------------|
    |    1. Point Filters (p/P)        |
    |    2. Filters (f/F)              |
    |    3. View Image (v/V)           |
    |    4. Convert to GrayScale(g/G)  |
    |    5. Previous Menu (b/B)        |
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
    |    6. Undo All Changes(u/U)      |
    |    7. Go to previous menu(b/B)   | 
    ------------------------------------
    '''
menu_4 = '''
    ------------------------------------
    |   FILTERS                        |
    |----------------------------------|
    |    1. Gaussian Blur (g/G)        |
    |    2. Average Filter (a/A)       | 
    |    3. Median Filter (m/M)        | 
    |    4. Sobel Filter (s/S)         | 
    |    5. Prewitt Filter (p/P)       | 
    |    6. Laplacian Filter (l/L)     | 
    |    7. Undo All Changes(u/U)      |            
    |    8. Go to previous menu(b/B)   | 
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
def image_options(img, channel):
    while True:
        print(menu_5)
        choice = input("Choice(s/d/b)?").lower()
        if choice == "s":
            save_as = input("Save as (e.g. sample.jpg) : ")
            save_path = "./saved_results"
            if channel == 3:
                cv.imwrite(os.path.join(save_path,save_as), cv.cvtColor(img, cv.COLOR_RGB2BGR)) 
            else:
                cv.imwrite(os.path.join(save_path,save_as))
            print("Image saved")
        elif choice == "d":
            plt.imshow(img, cmap='gray')
            plt.show()
        elif choice == "b":
            return
        else:
            print("Invaid choice")

def options(img, channel) -> None:
    copy_of_image = np.copy(img)
    while True:
        print(menu_2)
        choice = input("Choice(p/f/v/g/b)?").lower()
        if choice == "p":
            while True:
                print(menu_3)
                choice = input("Choice(i/a/t/c/e/b)?").lower()
                if choice=="i":
                    new_img = pOps.invert(img, channel)
                    image_options(new_img, channel)
                elif choice=="a":
                    new_img = pOps.auto_contrast(img, channel)
                    image_options(new_img,channel)
                elif choice=="t":
                    t_point = int(input("Threshold point: "))
                    new_img = pOps.threshold(img, t_point)
                    image_options(new_img, channel)
                elif choice=="c":
                    r1 = int(input("lower limit(r1): "))
                    r2 = int(input("upper limit(r2): "))
                    new_img = pOps.clipping(img, r1, r2)
                    image_options(new_img, channel)
                elif choice=="e":
                    new_img = pOps.equalize(img, channel)
                    image_options(new_img, channel)
                elif choice=="b":
                    break
                elif choice == "u":
                    img = np.copy(copy_of_image)
                    image_options(img, channel)
                else:
                    print("invalid choice")

        elif choice == "f":
            while True:
                print(menu_4)
                choice = input("Choice(g/a/m/s/p/l/u/b)").lower()
                if choice == "g":
                    kerel_size = int(input("Kernel size :"))
                    new_img = filters.gaussian(img, kerel_size)
                    image_options(new_img, channel)
                
                elif choice == "a":
                    kerel_size = int(input("Kernel size :"))
                    new_img = filters.average_filter(img, kerel_size)
                    image_options(new_img, channel)

                elif choice == "m":
                    kerel_size = int(input("Kernel size :"))
                    new_img = filters.median_blur(img, kerel_size)
                    image_options(new_img, channel)

                elif choice == "s":
                    kerel_size = int(input("Kernel size :"))
                    new_img = filters.sobel(img, channel, kerel_size)
                    image_options(new_img, channel)
                elif choice == "p":
                    new_img = filters.prewitt(img, channel)
                    image_options(new_img, channel)
                elif choice == "l":
                    new_img = filters.laplacian(img, channel)
                    image_options(new_img, channel)
                elif choice == "u":
                    img = np.copy(copy_of_image)
                    image_options(img, channel)
                elif choice=="b":
                    break
                else:
                    print("invalid choice")

        elif choice == "v":
            plt.imshow(img, cmap='gray')
            plt.show()

        elif choice == "g":
            img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            channel = 1

        else:
            return
def main():
    while True:
        print(menu_1)
        choice = input("Choice(n/d/a/h/b)? ").lower()
        if choice == "n":
            path = input("Image Path :")
            channel,exists,img = helpers.load_image(path)
            if not exists:
                print("Image not found!")
                continue
            print("*****Image loaded successfully!*****")
            options(img, channel)

        elif choice == "d":
            path = "./sample_images/"
            print(os.listdir(path))
            choice = input("Choose an image from the following : ")
            channel,exists,img = helpers.load_image(os.path.join(path,choice))
            if not exists:
                print("Image does not exist")
            else:    
                print("*****Image loaded successfully!*****")
                options(img, channel)
        
        elif choice == "a":
            print(helpers.about())
        
        elif choice == "h":
            helpers.help_menu()

        elif choice == "b":
            break

        else:
            print("Invalid choice")


if __name__=="__main__":
    main()


