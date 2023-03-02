import pyautogui
import time
#pyautogui無法將字串輸入到雷電模擬器中
#import clipboard as pc
#a1 = "Hey, nice to see you"
#pc.copy(a1)



#pyautogui.moveTo(2792,337,0.5)
#pyautogui.click(button='left')
#a1 = "qctest01"
#pc.copy(a1)
#time.sleep(1)
#pyautogui.typewrite('qctest01', interval=0.25)
#pyautogui.hotkey('ctrl', 'v')

#pyautogui.moveTo(2868,489,0.5)
#pyautogui.click(button='left')
#a1 = "Qq111111"
#pc.copy(a1)
#time.sleep(1)
#pyautogui.hotkey('ctrl', 'v')
#pyautogui.typewrite('Qq111111', interval=0.25)

#a1 = "Qq111111"
#pc.copy(a1)
#pyautogui.hotkey('ctrl', 'v')
LoopNum = 0
DeskNum = 0
StartX = 2666
StartY = 488
FinalLoopStartY = 560
XDistance = 117
YDistance = 150
ColumnItemNum = 5

while LoopNum < 5:
    while DeskNum <= 19:
        ClickX = StartX + (DeskNum % ColumnItemNum) * XDistance
        if LoopNum == 4:
            ClickY = FinalLoopStartY + (DeskNum // ColumnItemNum) * YDistance
        else:
            ClickY = StartY + (DeskNum // ColumnItemNum) * YDistance
        pyautogui.moveTo(ClickX,ClickY)
        pyautogui.click()
        time.sleep(0.3)
        DeskNum = DeskNum + 1
    if LoopNum == 4:
        break
    DeskNum = 0        
    pyautogui.moveTo(2850,1000,0.5)
    pyautogui.mouseDown(2850,1000)
    pyautogui.moveTo(2850,413,2)
    time.sleep(0.3)
    pyautogui.mouseUp(2850,413)
    LoopNum = LoopNum + 1

