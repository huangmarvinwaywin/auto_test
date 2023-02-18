from PIL import ImageGrab
from functools import partial
import pyautogui
import time

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

#screen = pyautogui.screenshot()
imgscreenIcon = ImageGrab.grab(bbox=(2587, 1035, 2587 + 595, 1035 + 145))
pyautogui.moveTo(2665,485,0.2)
pyautogui.click()
time.sleep(0.1)
#screen2 = pyautogui.screenshot()
imgscreenIcon2 = ImageGrab.grab(bbox=(2587, 1035, 2587 + 595, 1035 + 145))
#screen.save("D:/Selenium/auto_test/comparePIC/all.png")
#screen2.save("D:/Selenium/auto_test/comparePIC/all2.png")
imgscreenIcon.save("D:/Selenium/auto_test/comparePIC/cut.png")
imgscreenIcon2.save("D:/Selenium/auto_test/comparePIC/cut2.png")
