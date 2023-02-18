import pyautogui
import pyscreenshot as ImageGrab
import time
from PIL import ImageGrab
from functools import partial

import cv2
import numpy as np
from matplotlib import pyplot as plt

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

#click 夜神auto test desktop icon
pyautogui.moveTo(4191,46,2)
pyautogui.doubleClick()

iconCheck = False
imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/HomeIcon.png',0)
iconW = imgIcon.shape[1]
iconH = imgIcon.shape[0]
methods = ['cv2.TM_CCOEFF']
#time.sleep(10)

while iconCheck == False:
    imgscreen = pyautogui.screenshot()
    imgScreenCheck = imgscreen.copy()
    for meth in methods:
        method = eval(meth)
        imgScreenCheck = cv2.cvtColor(np.asarray(imgScreenCheck), cv2.COLOR_RGB2BGR)
        res = cv2.matchTemplate(imgScreenCheck,imgIcon,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(min_val, max_val, min_loc, max_loc)
        top_left = max_loc
        print(top_left)
        bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
        pyautogui.moveTo(top_left[0] + 10,top_left[1] + 10,1)
        pyautogui.doubleClick()
        iconCheck = True
        #暫時寫到這裡，這裡已經比對取得座標了
    
