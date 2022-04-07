import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


cartoons = soup.find_all("td",attrs={"class":"title"}) 

print(cartoons[0].a.get_text()) # 결과리스트 첫번째 것[0]의 하위 a 엘리먼트의 get_text()
print(cartoons[0].a["href"]) # 결과리스트 첫번째 것[0]의 하위 a 엘리먼트의 attrs 키="href" 의 값 

print("title ---------------------")
for cartoon in cartoons:
    print(cartoon.a.get_text())
    print("https://comic.naver.com" + cartoon.a["href"])


print("rating ---------------------")
total_rate = 0
ratings = soup.find_all("div",attrs={"class":"rating_type"}) 
for rating in ratings:
    # print(rating.strong.get_text()) # 용훈
    rate = (rating.find("strong").get_text())
    total_rate += float(rate)
print("평점평균 : ", float(total_rate/len(ratings)))

    