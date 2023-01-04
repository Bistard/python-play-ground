
#-*- coding:utf-8 -*-
import pyscreenshot as ImageGrab
#import cv2 as cv
from PIL import Image
import math
import operator
from functools import reduce
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
x,y = m.screen_size()
results = []

def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )

    return result

def game_HookUp():
    m.click(x//2,y//2,1)
    
while __name__ == "__main__":
    time_start = time.time()
    
    img1=ImageGrab.grab((x/2-50,y/2-50,x/2+50,y/2+50))
    img1.save('C:\\Users\Chris\Desktop\AutoFishing\img1.png')
    
    img1 = "C:\\Users\Chris\Desktop\AutoFishing\img1.png"
    img2 = "C:\\Users\Chris\Desktop\AutoFishing\img2.png"
    result = image_contrast(img1,img2)
    results.append(result)
    ave_result = sum(results)/len(results) #找出平均数
    
    time_end = time.time()
    print('new is:',result)
    print('ave is:',ave_result) #数字越大,越不相同
    print('Time:',time_end - time_start)
    print('--------')

    if result - ave_result >= 20:
        game_HookUp()
