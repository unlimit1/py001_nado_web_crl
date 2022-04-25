# pip install beautifulsoup4
# pip install lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print("type(soup) : ",type(soup)) 
print("soup.title : ", soup.title) # tag 포함 전체
print("type(soup.title) : ",type(soup.title)) 
print("soup.title.get_text() : ",soup.title.get_text()) #텍스트만
print("soup.a : ", soup.a) # soup 객체가 가지고있는 가장 처음 a 라는 엘리먼트! 를 보여줌  엘리먼트 = tag, attr 인듯
print("soup.a.attrs : ",soup.a.attrs) # dictionay 형태로 제공
print("soup.a['href'] : ", soup.a['href'])

print("soup.find('a',attrs={'class':'Nbtn_upload'} ) : ",soup.find('a',attrs={"class":"Nbtn_upload"} )) # soup.find 헬프 보기!!
print("soup.find(attrs={'class':'Nbtn_upload'} ) : ",soup.find(attrs={"class":"Nbtn_upload"} )) # 같은 결과 가 나오는 이유 이해하기!!
# 각 tag, attrs 의 필터조건에 따라 결과가 나옴!!

print('----------------------')
print("soup.find('li', attrs={\"class\":\"rank01\"} ): ",soup.find('li', attrs={"class":"rank01"} ))
rank01 = soup.find('li', attrs={"class":"rank01"}) # tag 의 필터조건 = 'li', attrs 의 필터조건 ={"class":"rank01"} 중 첫번째
print(rank01) # <class 'bs4.element.Tag'> li tag 객체
print(rank01.img) # <class 'bs4.element.Tag'> img tag 객체
print(rank01.img.attrs) # tag 의 attrs로 이루어진 dictionary
print(rank01.img.attrs['src']) # dictionary 중 키 'src' 의 값

# 부모, 자식, 형제의 엘리먼트?태그? 로 이동 
rank02 = rank01.next_sibling.next_sibling # 다음 형제가 CR 등 일수 있어서 2회 다음 형제를 찾은 경우 
rank03 = rank02.next_sibling.next_sibling 

print(rank02)
print(rank02.a.get_text())
print(rank03.a.get_text())
print(rank03.previous_sibling.previous_sibling.a.get_text())
print(rank01.parent)

print(rank01.find_next_sibling("li").a.get_text()) # CR 등에 상관 없이 조건으로 다음 형제를 찾을 수 있음

print(rank01.find_next_siblings("li")) # 리스트 형태로 전체 tag 를 제공함

print(soup.find("a", text='신비-외전 2화'))











