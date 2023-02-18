import pyautogui
import pyscreenshot as ImageGrab
import time
from PIL import ImageGrab
from functools import partial

import cv2
import numpy as np
from matplotlib import pyplot as plt

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

#雷電 L_ForAutoTest
#pyautogui.moveTo(4191,46,0.5)
#pyautogui.doubleClick()

#夜神 QA1
pyautogui.moveTo(4752,56,0.5)
pyautogui.doubleClick()



#檢查無敵娛樂王的app icon是否存在，
#若是，則點。若否，則等一秒
iconAppCheck = False
while iconAppCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/NOX_HomeWudiAppIcon.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('Found HomeWudiAppIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconAppCheck = True
    else:
        time.sleep(1)

#檢查會員輸入的按鈕是否存在，
#若是，則點。若否，則等一秒
iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/memberLoginIcon.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)

#檢查帳號輸入的空間是否存在，
#若是，則點。若否，則等一秒
iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/MemberAccount.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)
time.sleep(1)
pyautogui.typewrite(['Q','C','T','E','S','T','0','1'],'0.3')


#檢查密碼輸入的空間是否存在，
#若是，則點。若否，則等一秒
iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/MemberPassword.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)
time.sleep(1)
pyautogui.typewrite(['Q','q','1','1','1','1','1','1'],'0.3')


#檢查帳號密碼輸入後的確定按鈕是否存在，
#若是，則點。若否，則等一秒
iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/AccPWConfirm.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)

iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/AdClose.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)


iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/GoInToGameLobby.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)


iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/TransferMoney.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)

time.sleep(1)

iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/6001.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        pyautogui.moveTo(2850,1144,0.5)
        pyautogui.mouseDown(2850,1144)
        pyautogui.moveTo(2850,650,2)
        time.sleep(0.3)
        pyautogui.mouseUp(2850,650)
        time.sleep(1)



iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/6001IntoDesk.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)

#check banner is exits or not for next step
iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/6001_Banner.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('6001_Banner is Exits')
        iconMemberLoginCheck = True
    else:
        time.sleep(1)

#time.sleep(5)
#第一排
pyautogui.moveTo(2665,485,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2780,485,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2894,485,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3009,485,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3124,485,0.2)
pyautogui.click()
#time.sleep(1)

#第2排
pyautogui.moveTo(2665,622,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2780,622,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2894,622,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3009,622,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3124,622,0.2)
pyautogui.click()
#time.sleep(1)

#第3排
pyautogui.moveTo(2665,766,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2780,766,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2894,766,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3009,766,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3124,766,0.2)
pyautogui.click()
#time.sleep(1)

#第4排
pyautogui.moveTo(2665,911,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2780,911,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2894,911,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3009,911,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3124,911,0.2)
pyautogui.click()
#time.sleep(1)

#BacktoGameLobby
iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/BacktoGameLobby.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('BacktoGameLobby')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)


iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/6002.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        pyautogui.moveTo(2850,1144,0.5)
        pyautogui.mouseDown(2850,1144)
        pyautogui.moveTo(2850,650,2)
        time.sleep(0.3)
        pyautogui.mouseUp(2850,650)
        time.sleep(1)



iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/6002IntoDesk.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('memberLoginIcon')
        pyautogui.moveTo(top_left[0] + iconW/2,top_left[1] + iconH/2,0.5)
        pyautogui.click()
        #pyautogui.doubleClick()
        iconMemberLoginCheck = True
    else:
        time.sleep(1)


#check banner is exits or not for next step
iconMemberLoginCheck = False
while iconMemberLoginCheck == False:
    screen = pyautogui.screenshot()
    screen.save("D:/Selenium/auto_test/PicTemp/temp.png")
    time.sleep(1)
    imgscreen = cv2.imread('D:/Selenium/auto_test/PicTemp/temp.png')
    imgscreen2 = imgscreen.copy()
    imgIcon = cv2.imread('D:/Selenium/auto_test/PicForCompare/6002_Banner.png')
    iconW = imgIcon.shape[1]
    iconH = imgIcon.shape[0]
    imgscreen = imgscreen2.copy()
    res = cv2.matchTemplate(imgscreen,imgIcon,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    print(top_left)

    bottom_right = (top_left[0] + iconW, top_left[1] + iconH)
    imgscreenIcon = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    imgscreenIcon.save("D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png")
    #存檔確認比對圖案是否正確
    time.sleep(1)
    imgscreenIcon2 = cv2.imread('D:/Selenium/auto_test/PicTemp/ScreenIconTemp.png')
    hsv_base = cv2.cvtColor(imgIcon, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(imgscreenIcon2, cv2.COLOR_BGR2HSV)
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    
    compare_method = cv2.HISTCMP_CORREL
    base_test = cv2.compareHist(hist_base, hist_test, compare_method)

    print('base_test Similarity = ', base_test)
    if base_test > 0.9:
        print('6002_Banner is Exits')
        iconMemberLoginCheck = True
    else:
        time.sleep(1)

#time.sleep(5)
#第一排
pyautogui.moveTo(2665,485,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2780,485,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2894,485,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3009,485,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3124,485,0.2)
pyautogui.click()
#time.sleep(1)

#第2排
pyautogui.moveTo(2665,622,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2780,622,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2894,622,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3009,622,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3124,622,0.2)
pyautogui.click()
#time.sleep(1)

#第3排
pyautogui.moveTo(2665,766,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2780,766,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2894,766,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3009,766,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3124,766,0.2)
pyautogui.click()
#time.sleep(1)

#第4排
pyautogui.moveTo(2665,911,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2780,911,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(2894,911,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3009,911,0.2)
pyautogui.click()
#time.sleep(1)

pyautogui.moveTo(3124,911,0.2)
pyautogui.click()
#time.sleep(1)