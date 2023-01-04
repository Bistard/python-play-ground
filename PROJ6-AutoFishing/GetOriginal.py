#-- include('examples/showgrabbox.py')--#
#-*- coding:utf-8 -*-
import pyscreenshot as ImageGrab
import cv2 as cv
from PIL import Image
import math
import operator
from functools import reduce
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
x,y = m.screen_size()

if __name__ == "__main__":
    img2=ImageGrab.grab((x/2-50,y/2-50,x/2+50,y/2+50)) # X1,Y1,X2,Y2
    img2.save('C:\\Users\Chris\Desktop\AutoFishing\img2.png')
