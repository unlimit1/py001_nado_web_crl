import requests

res = requests.get("http://naver.com")
print("naver 응답코드 : ", res.status_code) #200이면 정상

res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() # 200이면 통과 아니면 오류내고 멈춤
print("nadocoding 응답코드 : ", res.status_code) #200이면 정상

#if res.status_code == requests.codes.ok:  # requests.codes.ok = 200
#    print('정상입니다.')
#else:
#    print('문제가 있네요. [에러코드 ',res.status_code,']')    