# HTTP Methode.... GET & POST
# GET : ? 뒤에 vari=value & 로 연결
# 쿠팡에서 김치 5kg 으로 검색
# https://www.coupang.com/np/search?rocketAll=true&q=%EA%B9%80%EC%B9%98+5kg&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=rocket_wow%2Ccoupang_global&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=13754&component=&rating=0&sorter=scoreDesc&listSize=36
# 쿠팡은 GET 방식으로 진행됨... 쉽게 접근하겠네...

import requests
import re
from bs4 import BeautifulSoup

# url = "https://www.coupang.com/np/search?component=&q=%EA%B9%80%EC%B9%98+5kg&channel=user" # 김치 5kg, 조회 첫 페이지
url = "https://www.coupang.com/np/search?q=%EA%B9%80%EC%B9%98+5kg&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=" # 조회 2 페이지
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}

#print(res.text)

print('---------------- starting for loop ------------------------')
for p in range(1,6) : # 1~5 페이지 조회
    res = requests.get(url.format(str(p)),headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # 한 페이지 안 모든 해당 li 에 대하여 가져오기 
    products = soup.find_all('li', attrs={'class':re.compile('^search-product')}) #class값을 정규표현식으로 찾기!!
    for no, prd in enumerate(products):                                           #enumerate 활용, type(prd):<class 'bs4.element.Tag'> 
        # 상품명
        print(f'[{str(p)}-{no+1:2d}]', prd.find("div",attrs={'class':'name'}).get_text())              #element내에서 tag 와 attrs 조건으로 맨 처음것 찾기 
        # 로켓프레쉬 배지
        badge_rocket = prd.find("span",attrs={'class':'badge rocket'})        #결과가 없는 건을 위하여 먼저 조회
        print('[로켓프레쉬]', end='') if badge_rocket else print('', end='')   #다음줄에서 if로 처리, if 한줄처리 문법!!
        # 가격
        print(prd.find("strong",attrs={'class':'price-value'}).get_text(),'원\t', end='')
        # 100g당 가격
        unit_price = prd.find("span",attrs={'class':'unit-price'})
        print(unit_price.get_text(), end='') if unit_price else print('단위가격없음\t', end='')
        # 상품평 수
        rate_count = prd.find("span",attrs={'class':'rating-total-count'})
        print('평'+rate_count.get_text()[1:-1],'\t', end='') if rate_count else print('평없음', end='')
        # 별점
        print('*'+prd.find("span",attrs={'class':'star'}).get_text(),'\t', end='')
        # print(type(prd.find('a')),  type(prd.find('a')['href']))    #  <class 'bs4.element.Tag'>  <class 'str'>
        # 링크
        print('\t', 'https://www.coupang.com'+prd.find('a')['href'])          
        print('', end='\n')
    
    
