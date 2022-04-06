import requests
url = "http://nadocoding.tistory.com"

# https://www.whatismybrowser.com/detect/what-is-my-user-agent/
# header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
res = requests.get(url, headers=header) # 왜 user agent 를 넣으면 에러가 날까요...??? header 의 형식에 주의
res.raise_for_status()
with open("nado.html", "w", encoding="utf8") as f:
    f.write(res.text)

# gitpod 에서 파일변경