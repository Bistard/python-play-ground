from PIL import ImageGrab, Image
from functools import reduce
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import math
import time
import threading


def image_contrast(img1, img2):

    h1 = img1.histogram()
    h2 = img2.histogram()

    h3 = list(map(lambda a, b: (a - b) ** 2, h1, h2))
    result = math.sqrt(reduce(lambda a, b: a+b, h3)/len(h3))

    return result


def change_detect_area():
    global xx
    xx[0] += 25
    xx[1] += 25
    t = threading.Timer(10, change_detect_area)
    t.start()


m = PyMouse()
k = PyKeyboard()

differs = []
xx = [460, 635]

t = threading.Timer(10, change_detect_area)
t.start()

day = Image.open('example1.jpg')
night = Image.open('example2.png')
switch = -1
differs = []

while True:

    img = ImageGrab.grab((xx[0], 480, xx[1], 600))
    differ = image_contrast(day, img)
    #print(differs)
    differs.append(differ)
    if len(differs) == 3:
        differs.pop(0)
        if differs[1] - differs[0] == 0:
            xx = [460, 635]
            m.click(460, 280)
        if differ > 1000:
            switch *= -1
        if 60 < differ < 500:
            k.press_key(' ')
            time.sleep(0.15)
            k.release_key(' ')
