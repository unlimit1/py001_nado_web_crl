import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhnsosok=0&page='

filename = "12코스피시가총액순.csv"
f=open(filename, 'w', encoding='utf-8-sig', newline='') # 엑셀에서 한글 안깨지게 'utf8' 대신 'utf-8-sig'    newline='' 넣지 않으면 한줄 넣고 줄바꿈됨
writer = csv.writer(f)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'
print(title.split())
writer.writerow(title.split())

for page in range(1,37):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # data_rows = soup.find('table',attrs={'class':'type_2'}).find_all('tr')
    # for d in data_rows: print(d.text.split())
    
    data_rows = soup.find('table',attrs={'class':'type_2'}).find('tbody').find_all('tr')
    for row in data_rows:
        columns = row.find_all('td')
        if len(columns) <= 1: continue # 의미없는 데이터 스킵
        data = [column.get_text().strip() for column in columns] # strip() 화이트스페이스 제거
        # print(data)
        writer.writerow(data)
