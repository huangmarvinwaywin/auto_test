import cv2 as cv
import numpy as np
from skimage import metrics
from PIL import Image
import imagehash

img1 = Image.open('D:/Selenium/auto_test/GameInfo/6001_Info.png')
img2 = Image.open('D:/Selenium/auto_test/GameInfo/6001_Info_.png')

hash1 = imagehash.average_hash(img1)
hash2 = imagehash.average_hash(img2)
if hash1 == hash2:
    print("hash is the same")
else:
    print(("hash is not the same"))
#print('ssim = ', ssim)
"""
base = cv.imread('D:/Selenium/auto_test/comparePIC/TableDetail.png')
test = cv.imread('D:/Selenium/auto_test/comparePIC/TableDetailClose.png')
test2 = cv.imread('D:/Selenium/auto_test/comparePIC/PicToTXT5.png')

hsv_base = cv.cvtColor(base, cv.COLOR_BGR2HSV)
hsv_test = cv.cvtColor(test, cv.COLOR_BGR2HSV)
hsv_test2 = cv.cvtColor(test2, cv.COLOR_BGR2HSV)

h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges
channels = [0, 1]

hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
hist_test = cv.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
hist_test2 = cv.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

compare_method = cv.HISTCMP_CORREL

base_base = cv.compareHist(hist_base, hist_base, compare_method)
base_test = cv.compareHist(hist_base, hist_test, compare_method)
base_test2 = cv.compareHist(hist_base, hist_test2, compare_method)

print('base_base Similarity = ', base_base)
print('base_test Similarity = ', base_test)
print('base_test2 Similarity = ', base_test2)
"""