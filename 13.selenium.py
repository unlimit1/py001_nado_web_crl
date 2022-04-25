# 공식 홈페이지 https://selenium-python.readthedocs.io/
# 셀레니움 기본 사용법 한글 https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/#%EC%84%A4%EC%B9%98_-_install

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬드라이버 다운로드 : https://sites.google.com/a/chromium.org/chromedriver/downloads
#browser = webdriver.Chrome("./chromedriver.exe") # 크롬드라이버가 설치된 경로와 실행파일
browser = webdriver.Chrome() # 소스코드와 같은 위치에 크롬드라이버 사용
browser.get("http://naver.com")

el = browser.find_element_by_class_name('ico_naver')
el.click()
browser.back()
browser.forward()
browser.back()
 
el = browser.find_element_by_id('query')
el.send_keys("미래에셋생명")
el.send_keys(Keys.ENTER)

el = browser.find_element_by_tag_name('a')
el
print(type(el))

el = browser.find_elements_by_tag_name('a') # 모두 리스트로 가져오기 .. element"s"
for i, e in enumerate(el):
    print(i, e.text ,  e.get_attribute("href"))
    if i > 50: break 

browser.get("http://daum.net")
el = browser.find_element_by_name('q')
el.send_keys("삼성전자")

el = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
el.click()

browser.close() # 해당 탭 만 닫음
browser.quit() # 브라우저 전체를 닫음



