#import pyautogui

#pyautogui.moveTo(4191,46,2)
#pyautogui.doubleClick()
#pyautogui.position()

import pyscreenshot as ImageGrab

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

image = ImageGrab.grab()
image.save("full_2023010701.png")
