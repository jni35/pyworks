# 구구단 파일 쓰기
# with as 구문 f.close()를 사용하지 않음
with open("gugudan.txt", "a") as f:      # 추가 쓰기 - 'a'모드
    for i in range(2, 10):
        for j in range(1, 10):
            times = "%dX%d=%d\n" % (i, j, i*j)
            f.write(times)
        f.write('\n')

