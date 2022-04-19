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
    |    1. Enter image path           |
    |    2. Use sample images          |
    |    3. About this program         |
    |    4. Help                       |
    |    5. Exit                       | 
    ------------------------------------
    '''
menu_2 = '''
    ------------------------------------
    |   IMAGE OPTIONS                  |
    |----------------------------------|
    |    1. Convert to Grayscale       |
    |    2. View Original Image        |
    |    3. View Modified Image        |
    |    4. Save As                    |
    ------------------------------------
    |   POINT OPERATIONS               |
    |----------------------------------|
    |    5. Invert image               |
    |    6. Auto-contrast              | 
    |    7. Thresholding               | 
    |    8. Clipping                   |
    |    9. Equalize                   |
    ------------------------------------
    |   FILTERS                        |
    |----------------------------------|
    |    10. Gaussian Blur             |
    |    11. Average Filter            | 
    |    12. Median Filter             | 
    |    13. Sobel Filter              | 
    |    14. Prewitt Filter            | 
    |    15. Laplacian Filter          | 
    |    16. Undo All Changes          |            
    |    17. Go to previous menu       |  
    ------------------------------------
    '''

def options(img, channel):
    copy_of_image = np.copy(img)
    while True:
        print(menu_2)
        choice = input("Choice(1/2/3....)?")
        if choice == "1":
            img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            channel = 1

        elif choice == "2":
            plt.imshow(copy_of_image, cmap='gray')
            plt.show()
        
        elif choice == "3":
            plt.imshow(img, cmap='gray')
            plt.show()

        elif choice == "4":
            save_as = input("Save as (e.g. sample.jpg) : ")
            save_path = "./saved_results"
            if channel == 3:
                cv.imwrite(os.path.join(save_path,save_as), img, cv.cvtColor(img, cv.COLOR_RGB2BGR)) 
            else:
                cv.imwrite(os.path.join(save_path,save_as), img)
            print("Image saved")

        elif choice =="5":
            img = pOps.invert(img, channel)

        elif choice=="6":
            img = pOps.auto_contrast(img, channel)

        elif choice=="7":
            t_point = int(input("Threshold point: "))
            img = pOps.threshold(img, t_point)

        elif choice=="8":
            r1 = int(input("lower limit(r1): "))
            r2 = int(input("upper limit(r2): "))
            img = pOps.clipping(img, r1, r2)

        elif choice=="9":
            img = pOps.equalize(img, channel)

        elif choice == "10":
            kernel_size = int(input("Kernel size :"))
            img = filters.gaussian(img, kernel_size)
                
        elif choice == "11":
            kernel_size = int(input("Kernel size :"))
            img = filters.average_filter(img, kernel_size)

        elif choice == "12":
            kernel_size = int(input("Kernel size :"))
            img = filters.median_blur(img, kernel_size)

        elif choice == "13":
            kernel_size = int(input("Kernel size :"))
            img = filters.sobel(img, channel, kernel_size)

        elif choice == "14":
            img = filters.prewitt(img, channel)

        elif choice == "15":
            img = filters.laplacian(img, channel)

        elif choice == "16":
            img = np.copy(copy_of_image)
            
        elif choice == "16":
            break
        elif choice == "17":
            return
        else:
            print("invalid choice")
        
def main():
    while True:
        print(menu_1)
        choice = input("Choice(1/2/3/4/5) ")
        if choice == "1":
            path = input("Image Path :")
            channel,exists,img = helpers.load_image(path)
            if not exists:
                print("Image not found!")
                continue
            print("*****Image loaded successfully!*****")
            options(img, channel)

        elif choice == "2":
            path = "./sample_images/"
            print(os.listdir(path))
            choice = input("Choose an image from the following : ")
            channel,exists,img = helpers.load_image(os.path.join(path,choice))
            if not exists:
                print("Image does not exist")
            else:    
                print("*****Image loaded successfully!*****")
                options(img, channel)
        
        elif choice == "3":
            print(helpers.about())
        
        elif choice == "4":
            helpers.help_menu()

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__=="__main__":
    main()


