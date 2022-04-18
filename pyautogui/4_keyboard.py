import pyautogui

w = pyautogui.getWindowsWithTitle("메모장")[0] # 메모장을 띄우고 최소화 상태에서..
print(w)
w.activate()

pyautogui.write("12345")
pyautogui.write("abcdefg", interval=0.2)
pyautogui.write("한글은 안됨") # 클립보드로 처리..

#  list로 처리 주의
pyautogui.write(["enter","a",'p','p','l','e','left','left','enter'], interval=0.1)

# https://automatetheboringstuff.com/2e/chapter20/

pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

pyautogui.keyDown("shift")
pyautogui.keyDown("5")
pyautogui.keyUp("5")
pyautogui.keyUp("shift")

# ctrl 누르고, alt 누르고, a 누르고, a 떼고, ...
pyautogui.hotkey('ctrl','alt','a')

# 한글 처리 -> 클립보드 활용
# pip install pyperclip

import pyperclip
pyperclip.copy("나랏말싸미~")
pyautogui.hotkey("ctrl","v")

# 자동화 중간 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q

