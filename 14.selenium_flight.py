# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#from selenium.webdriver.common.keys import Keys

#browser = webdriver.Chrome("./chromedriver.exe") # 크롬드라이버가 설치된 경로와 실행파일
browser = webdriver.Chrome() # 소스코드와 같은 위치에 크롬드라이버 사용
browser.get("https://flight.naver.com")

#가는날 선택 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
   
el = browser.find_element_by_partial_link_text ('30')
print(el)
