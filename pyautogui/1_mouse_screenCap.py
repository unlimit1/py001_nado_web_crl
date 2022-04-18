#pip install pyautogui
import pyautogui

desktop_size = pyautogui.size() #현재 화면 크기 가져옴 Size(width=1920, height=1080)
print(desktop_size, desktop_size[0], desktop_size[1])

pyautogui.moveTo(100,100) # 데스크탑 절대좌표 지정한 위치로 마우스 이동
print(pyautogui.position()) # 마우스 절대위치
pyautogui.moveTo(200,300, duration=2) # 2초 동안 천천히 움직임
print(pyautogui.position())
pyautogui.move(100,100, duration=2) # 상대좌표 이동
print(pyautogui.position())
pyautogui.move(100,-100, duration=2) # 상대좌표 이동
print(pyautogui.position())


point = pyautogui.position() # 마우스 절대위치
print (point[0], point.x) 


pyautogui.sleep(3) 

pyautogui.click() # 마우스 현재위치 에서 클릭
pyautogui.click(100,100) # 마우스 현재위치 에서 클릭
pyautogui.click(100,100, duration = 1) # 마우스 현재위치 에서 클릭
pyautogui.mouseDown()
pyautogui.mouseUp()

pyautogui.doupleClick()
pyautogui.rightClick()
pyautogui.middleClick() # 마우스 휠 처리
pyautogui.click(clicks=100) # 100회 클릭
pyautogui.drag(100,0,duration=1) # 마우스 상대좌표 개념으로 드래그 이동
pyautogui.dragTo(100,0,duration=1) # 마우스 절대좌표 개념으로 드래그 이동
pyautogui.scroll(300) #위 방향으로 300 방향으로 스크롤 , 음수일 때는 아래방향

pyautogui.mouseInfo() #마우스 정보툴.... 3초 누르고 있으면 좌표,RGB값 복사

#마우스를 네 귀퉁이로 옮기면 pyautogui 작동 끝남
pyautogui.FAILSAFE = False # 네 귀퉁이 끝남 off
pyautogui.PAUSE = 1 #  모든 동작에 1초씩 sleep


img = pyautogui.screenshot() #전체 화면 캡처
img.save('screen.png') #파일저장

pixel = pyautogui.pixel(100,100) #해당 죄표의 RGB 값 가져옴
print(pixel)

print(pyautogui.pixcelMatchesColor(100,100, (255,0,0))) #True False








