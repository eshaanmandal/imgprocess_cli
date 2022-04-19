import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def load_image(path_to_image: str):
    try:
        img = cv.imread(path_to_image)
        if len(img.shape) == 3:
            channel = 3
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        else:
            channel = 1
    
        return (channel, True, img)

    except cv.error as error:
        return (False, None)

why = '''

'''
how = '''

'''
about_point_ops = '''

'''
about_filters = '''

'''


def help_menu():
    '''Help message for using the program and also prints info about all the filters and point operations'''
    while True:
        message = '''
        1. Why this program? 
        2. How to use this program? 
        3. About point operations 
        4. About filters 
        5. Go back to previous menu 
    '''
        print(message)
        choice = input("Choice : ")
        if choice == "1":
            print(why)
        elif choice == "2":
            print(how)
        elif choice == "3":
            print(about_point_ops)
        elif choice == "4":
            print(about_filters)
        elif choice == "5":
            return
        else:
            print("Invalid choice")
    
    
def about():
    about_message = """
quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     \\
        :##.       ==             .###.       `.      `.    `\\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:'    

The above artwork was shamelessly copied from the internet

Made by Eshaan Mandal, a student ECE at TIET, during his 3rd year. He just wanted to put together everything he had learnt in his 
IPCV(Image Processing and Computer Vision) class

Enjoy and do whatever you want with this program. I mean just give me credits if you use my code, please :)
"""
    
    return about_message


    