from PIL import Image
import pytesseract
  
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/huang_marvin/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
img = Image.open('D:/Selenium/auto_test/comparePIC/Snipaste_2023-02-02_16-44-51.png')
text = pytesseract.image_to_string(img, lang='chi_tra')
text = text.split('\n')

print(text)
print("===============================================================")
print(text[0])
print("0===============================================================")
print(text[1])
print("1===============================================================")
print(text[2])
print("2===============================================================")

print(text[3])
print("3===============================================================")

'''
desk = text[2].replace("(","")
desk = desk.replace(")","")


print(desk)

if desk == '3':
    print("OK")
else:
    print("XX")
'''