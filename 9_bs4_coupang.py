# HTTP Methode.... GET & POST
# GET : ? 뒤에 vari=value & 로 연결
# 쿠팡에서 김치 5kg 으로 검색
# https://www.coupang.com/np/search?rocketAll=true&q=%EA%B9%80%EC%B9%98+5kg&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=rocket_wow%2Ccoupang_global&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=13754&component=&rating=0&sorter=scoreDesc&listSize=36
# 쿠팡은 GET 방식으로 진행됨... 쉽게 접근하겠네...

import requests
from bs4 import BeautifulSoup

#url = "https://www.coupang.com/np/search?component=&q=%EA%B9%80%EC%B9%98+5kg&channel=user"
url = "https://www.coupang.net/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
print(1)
res = requests.get(url,headers=headers)
print(2)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

print(res.text)
