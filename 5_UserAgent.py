# https://www.whatismybrowser.com/detect/what-is-my-user-agent/

import requests
url = "http://nadocoding.tistory.com"
headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
res = requests.get(url, headers=headers)
with open("nado.html", "w", encoding="utf8") as f:
    f.write(res.text)