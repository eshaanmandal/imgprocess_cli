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
       .                       
       |`.                     
       ;  `.                   
       ; :. \           __     
       ; ; \ \      .--"  \    
       ; ;  ; ;     :      \   
       ; ;  : :     ; ;     ;  
       ' :   ; ;    ;::     :  
        \ \  : ;--.-;; l     ; 
         \ \  ;:    :;//'-.__: 
         /\ \ ::____:::-\      
        /  ).:+'""""""""=\     
       :_,=""     /"-.    ;    
       ;"       .'    `.  |    
      :      .-^=    ==.\ |    
      |  _.-".gp      gp:;:    
      ;    /  $$      $$;: ;   
     :    :  `--      --:  |   
     ;    ;\        ,   '  |   
    :    :  \      _   /   :   
    ;    |   `.   `-' /     ;  
   :     :    :`-.__.'      |  
   ;          ;     :       |  
  :     ...._/      '.__..  |  
  ;   .'                  \ ;  
 :   /                   _ Y   
 ;  :         .g$$p.    d$$+.  
 ;  ;     :.g$$$$$$$$p.d$$$$$b 
 :  :     :$$$$$$$$$$$T$$$$$$$;
  \  ;    ;$$$$S$$$$$$$S$$$$$P 
   `.|    |$$$$S$$$$$$$S$$$$P  
     |    |T$$$$$SSSSS$$$$$$   
     :    | `T$$$$$$$$$$$$$;   
      ;   |   $$$$$$$$$$$$$    
      |   :   $$$$$$$$$$$$;    
      :    ; d$$$$$$$$$$$$;    
      |    :d$$$$$$$$$$$$$$    
      ;    :"^T$$$$$$$$$$$$b   
     :     ;   `T$$$$$$$$$$P;  
     ;    :      `T$$$$$$$P :  
     |    ;        T$$$$$P   ; 
     |   :          T$$P'    ; 
     :   ;           $'      : 
    ._;__;           :       : 
    ; ;  ;           |       : 
    :_L__:           |       ; 
    .'    ;          |       ; 
  .'      :          |      :  
 :/ _.-.  :;         |      |  
 /.'    \ |:         |      ;  
//  bug  ;| ;        |     :   
`        `' :        |     |   
             ;       |     ;   
             :       |    :    
              ;      |    |    
              :      :    ;    
              :    _.'-   ;    
              ;     /:    :    
             /     / ;     ;   
            /     :  ;     :   
           :      ;  ;     :   
           ;     :  :      :   
          :      ;  :      ;   
          ;     :   ;     :    
         :      ;   ;     ;    
         ;     :    ;    :     
         ;     ;    ;    ;     
         ;    :     ;   :      
         |    ;     ;   ;      
         |   :      ;  :       
         |   ;      ;  ;       
         :  :       :  ;       
         ;  :       :  :       
        :    ,      ;   ;      
        ;    ;      ;   :      
       :     :      :    ;     
       :     ;      :b__d$     
       $b   d$       $$$$$     
       :$bgd$;        T$P'     
        T$$$P                  
         '"'
3477
                           
Made by Eshaan Mandal, a student ECE at TIET, during his 3rd year. He just wanted to put together everything he had learnt in his 
IPCV(Image Processing and Computer Vision) class

Enjoy and do whatever you want with this program. I mean just give me credits if you use my code, please :)
"""
    return about_message

def convolve(X : np.array, F: np.array):
    # height and width of the image
    X_height = X.shape[0]
    X_width = X.shape[1]
    
    # height and width of the filter
    F_height = F.shape[0]
    F_width = F.shape[1]
    
    H = (F_height - 1) // 2
    W = (F_width - 1) // 2
    
    #output numpy matrix with height and width
    out = np.zeros((X_height, X_width))
    #iterate over all the pixel of image X
    for i in np.arange(H, X_height-H):
        for j in np.arange(W, X_width-W):
            sum = 0
            #iterate over the filter
            for k in np.arange(-H, H+1):
                for l in np.arange(-W, W+1):
                    #get the corresponding value from image and filter
                    a = X[i+k, j+l]
                    w = F[H+k, W+l]
                    sum += (w * a)
            out[i,j] = sum
    #return convolution  
    return out
    