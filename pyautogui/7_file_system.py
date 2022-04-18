import os
print(os.getcwd())
os.chdir("pyautogui")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())

#파일 전체 경로와 파일명
file_path_name = os.path.join(os.getcwd(), "file.txt")
print(file_path_name)

#풀 경로에서 파일경로만 추출
print(os.path.dirname(r"C:\Users\lp\dev\py001_nado_web_crl\pyautogui\menu_help.PNG"))

import time
import datetime

f = r"C:\Users\lp\dev\py001_nado_web_crl\pyautogui\7_file_system.py"
c_time = os.path.getctime(f) #생성일자
print(c_time)
print(datetime.datetime.fromtimestamp(c_time))
print(datetime.datetime.fromtimestamp(c_time).strftime('%Y%m%d %H:%M:%S'))

m_time = os.path.getmtime(f) #수정일자
print(datetime.datetime.fromtimestamp(m_time).strftime('%Y%m%d %H:%M:%S'))

a_time = os.path.getatime(f) #접근일자
print(datetime.datetime.fromtimestamp(a_time).strftime('%Y%m%d %H:%M:%S'))

size = os.path.getsize(f)
print(size)

# 파일목록 가져오기
print(os.getcwd())
print(os.listdir())
print(os.listdir('pyautogui'))

# 하위 폴더 포함 목록 가져오기
# result = os.walk(os.getcwd())
# print(result)
# print('-----------------------------')
# for root, dirs, files in result:
#     print(root, dirs, files)

# *.py 만 찾기
import fnmatch
result = []
print('-----------------------------')
for root, dirs, files in os.walk(os.getcwd()):
    for name in files:
        if fnmatch.fnmatch(name, "*.py"):
            result.append(os.path.join(root, name))

print(r for r in result)
print([r for r in result]) # for 문 한줄로 쓰기....리스트로 감싸야 하는군... --;  #https://leedakyeong.tistory.com/entry/python-for%EB%AC%B8-if%EB%AC%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%EC%BD%94%EB%94%A9%ED%95%98%EA%B8%B0
print("\n".join(r for r in result)) #  join함수의 모습 : "구분자".join(리스트)
