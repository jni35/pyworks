# 파일 쓰기

f = open("c:/web_dev/pyfile/file.txt", "w")      # 파일 열기
f.write("하늘이 파랗다.\n")
f.write("Thank you!!\n")
f.write("社員\n")
# f.write(45\n)       # 숫자를 바로 입력 불가
f.write("45\n")     # 문자는 가능


f.close()       # 파일 닫기
