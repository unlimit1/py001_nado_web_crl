import pyautogui

print("Countdown... ", end='')
pyautogui.countdown(5)
print("Start")

pyautogui.alert("alert 창")
cfm_rlst = pyautogui.confirm('wanna continue...?') #Ok Cancle
print(cfm_rlst)
in_rslt = pyautogui.prompt('파일명을 넣으세요')
print(in_rslt)
pw_rslt = pyautogui.password('암호를 넣으세요')
print(pw_rslt)



