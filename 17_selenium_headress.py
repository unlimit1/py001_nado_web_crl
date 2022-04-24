
from selenium import webdriver

# Headless 를 하기 위하여 아래 4줄의 옵션 설정 및 webdriver.Chrome(options=options) 설정
# 아래 get_screenshot 처리 참조
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("Window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
 
browser = webdriver.Chrome(options=options)

#페이지 이동
url = 'https://play.google.com/store/movies/category/MOVIE'
browser.get(url)

"""
# 지정한 위치로 스크롤 내리기
# 해상도 높이인 1080 위치로 스크롤 내리기
browser.execute_script("window.scrollTo(0, 1080)")
browser.execute_script("window.scrollTo(0, 3080)")

# 화면 가장 아래로 내리기
browser.execute_script("window.scrollTo(0, document.body,scrollHeight)")
"""

# 스크롤 다운시 계속 항목이 추가되는 동적 페이지 크롤링 
# 스크롤을 가장 아래로 내렸을 때, 이전 높이와 동일하면 스크롤 다운 멈추는 로직
import time
interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")
i=0
while True:
    i+=1
    # 스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 동적 페이지 로딩 시간 확보
    time.sleep(interval)
    # 현재 문서 높이 재 확인
    curr_height = browser.execute_script("return document.body.scrollHeight")
    print(i, prev_height, curr_height)
    if prev_height == curr_height: break
    prev_height = curr_height

print("스크롤 가장 아래 도달")    

# headless 스크린샷 처리
browser.get_screenshot_as_file("google_movie_headless.png")

import requests
from bs4 import BeautifulSoup

# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,'lxml')
soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all('div', attrs={'class':'ULeU3b neq64b'}) 
             #find_all('div', attrs={'class':['ULeU3b neq64b','LrNMN']})  or 로 2개 이상 어트리뷰트 find 가능
print(len(movies))

for i, item in enumerate(movies):
    e_name = item.find("div", attrs={"class":"Epkrse"}); name = e_name.get_text() if e_name else 'NoTitle'
    e_star = item.find("div", attrs={"class":"LrNMN"}); star = e_star.get_text() if e_star else 'NoStar'
    e_pirce = item.find("span", attrs={"class":"VfPpfd VixbEe"}); price = e_pirce.get_text() if e_pirce else 'NoPrice'
    
    org_price = item.find("span", attrs={"class":"SUZt4c P8AFK"}); org_price = org_price.get_text() if org_price else 'NoOrgPrice'
    
    link = item.find("a", attrs={"class":"Si6A0c ZD8Cqc"})
    link = link['href'] if link else 'NoLink'

    print(f'[{i}] {name}   {star}  {price} 할인전:{org_price}  https://play.google.com{link}')

with open('movies.html','w',encoding='utf8') as f:
    f.write(soup.prettify())

browser.quit()

