from ctypes import *
import pyautogui

def get_color(x,y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)
    pixel = gdi32.GetPixel(hdc,x,y)
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    print(r,g,b)

get_color(4378,1289)