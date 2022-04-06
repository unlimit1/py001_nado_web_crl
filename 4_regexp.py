import re

p = re.compile("ca.e")

# . 아무 한문자   ^  $ ...

m = p.match("case") #주어진 문장의 첫번째부터 조건과 일치하는지 확인
print(m.group()) # 매치되면 첫번째 검색결과, 매치되지 않으면 에러

def print_match(m):
    print("-----------------\nm :",m)
    if m:
        print("m.group() : ", m.group())
        print("m.string() : ", m.string) # string은 함수가 아님...!
        print("m.start() : ", m.start())
        print("m.end() : ", m.end())
        print("m.span() : ", m.span())
    else:
        print("매칭되지 않음")

print_match(p.match("cafe")) # match 주어진 문자열의 첫번째부터 조건과 일치하는지 확인
print_match(p.match("caffe")) 
print_match(p.search("good care")) # search 주어진 문자열 중 조건과 일치하는지 확인

print('--------------------')
print(p.findall("good care in cafe")) # findall 일치하는 모든 부분을 리스트로 반환

