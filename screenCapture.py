'''
OverwatchCharacterDetection v1.0 - James Murphy
Created with Python 3.9.7
Requires installation of: mss, opencv-python, pillow
NOTE:  
    - Must set Overwatch Resolution to 1024 x 768
    - Must put Overwatch Window in top left of your screen as small as possible
    - Recommended to set the game to 30FPS for best results
'''
from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time

print("Window is now running....CRTL+C to close program")

win = {'top' : 30, 'left' : 0, 'width' : 1024, 'height' : 580}

sct = mss()

while 1:
    sct_img = sct.grab(win)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) 
    cv2.imshow('test', np.array(img_bgr))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
