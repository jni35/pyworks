# 파일 쓰기

f = open("c:/web_dev/pyfile/number.txt", "w")      # 파일 열기
f.write("%d\n"% 45)
f.write("%.2f\n"% 12.34)
f.write("%d\n"% (45+1))     # 괄호 생략하면 안됨
i=3
j=4
times = "%d * %d = %d" % (i, j, i*j)
f.write(times)


f.close()       # 파일 닫기
