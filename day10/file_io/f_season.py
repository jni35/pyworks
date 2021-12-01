# 파일에 리스트 쓰기
season = ['봄', '여름', '가을', '겨울']
f = open("c:/web_dev/pyfile/season.txt", "w")    # 쓰기 모드
for i in season:
    f.write(i+'\n')      # 파일에 쓰기(저장)
f.close()   # 닫기

try:
    f = open("c:/web_dev/pyfile/season.txt", "r")
    season = f.read()
    print(season)
except FileNotFoundError:
    print("파일을 열 수 없습니다.")

