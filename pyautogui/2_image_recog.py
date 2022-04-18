import pyautogui

menu_help = pyautogui.locateOnScreen('.\pyautogui\menu_help.png') #파일명 대소문자는 구분안하는데.... 파일 디렉토리 위치는 주의
#해당 이미지 파일의 locate 를 찾지못하면 None 리턴 -> 상황 처리에 활용
print(menu_help) # Box(left=1158, top=11, width=40, height=26) 
                 # 전체화면 중에서 찾으므로 시간이 어느정도 소요됨
pyautogui.click(menu_help)

for box in pyautogui.locateAllOnScreen('checkbox.png'): #해당 이미지 모두 처리
    print(box)
    pyautogui.click(box, duration=0.5)


######################################
# 속도개선

# 1.GrayScale .... 30% 정도 속도개선이 된다고 함.
menu_help = pyautogui.locateOnScreen('menu_help.png', grayscale=True) 

# 2.범위 지정 region = (x, y, width, height)
menu_help = pyautogui.locateOnScreen('menu_help.png', region = (100, 100, 100, 100)) 

# 3.정확도 조정
# pip install opencv-python
menu_help = pyautogui.locateOnScreen('menu_help.png', confidence=0.7) 


######################################
# 다음 동작 사이 딜레이
menu_help = pyautogui.locateOnScreen('menu_help.png', confidence=0.7) 
# if menu_help:
#     pyautogui.click(menu_help)
# else:
#     print("실패") 
while menu_help is None:    #해당 이미지가 있을 때 까지 반복
    menu_help = pyautogui.locateOnScreen('menu_help.png')   
pyautogui.click(menu_help) #참이 되면 빠져 나옴

# 함수화 하여 처리
import time
import sys

def find_tar_img(img_file, timeout=10):
    s_time = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        e_time = time.time()
        if e_time - s_time > timeout:
            break
    return target

def my_click(img_file, timeout=10):
    target = find_tar_img(img_file, timeout=10)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target no found ({img_file}). Terminating Program")
        sys.exit()

my_click('menu_help.png', 10)












