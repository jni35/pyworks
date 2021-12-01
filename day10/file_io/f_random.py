# 파일에 리스트 쓰기
import random as r

f = open("c:/web_dev/pyfile/season.txt", "r")

# 랜덤하게 자료 읽기
word = f.read().split()     # 공백으로 구분   #한 줄로 있을 경우는 readline()
w = r.choice(word)
print(w)

f.close()       # 파일 닫기
