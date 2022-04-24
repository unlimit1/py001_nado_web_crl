# BueautifulSoup 으로 동적 페이지 확장을 못하는 예제
import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/category/MOVIE'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    #, 'Accept_Language':'ko-KR,ko'
}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

movies = soup.find_all('div', attrs={'class':'ULeU3b neq64b'})
print(len(movies))

for i, item in enumerate(movies):
    e_name = item.find("div", attrs={"class":"Epkrse"}); name = e_name.get_text() if e_name else 'NoTitle'
    e_star = item.find("div", attrs={"class":"LrNMN"}); star = e_star.get_text() if e_star else 'NoStar'
    e_pirce = item.find("span", attrs={"class":"VfPpfd VixbEe"}); price = e_pirce.get_text() if e_pirce else 'NoPrice'
    print(f'[{i}] {name}   {star}  {price}')

with open('movies.html','w',encoding='utf8') as f:
    f.write(soup.prettify())
