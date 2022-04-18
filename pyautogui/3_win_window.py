# https://automatetheboringstuff.com/2e/chapter20/
import pyautogui

fw = pyautogui.getActiveWindow() #현재 활성화된 창
print(fw.title)
print(fw.size)
print(fw.left, fw.top, fw.right, fw.bottom)
pyautogui.click(fw.left+50, fw.top+10)

for w in pyautogui.getAllWindows():
    print(w)

for w in pyautogui.getWindowsWithTitle('Visual'): #title 에 문자열을 포함한 윈도우들
    print(w)    

w = pyautogui.getWindowsWithTitle('Visual')[0]

if w.isActive == False: w.activate()
if w.isMaximized == False: w.maximize()
#if w.isMinimized == False: w.minimize()

pyautogui.sleep(1)
w.restore()

# 윈도우 리사이즈 및 이동
w.width = 955
w.height = 1030
w.moveTo(960,5)

# w.close()