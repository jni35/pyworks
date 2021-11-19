#자리배치도 프로그램
#고객수를 열(좌석)로 나워 행(줄)을 구해서 for문으로 배치
customer = int(input("입장객 수 입력 : "))
col = int(input("좌석 열 수 입력 : "))

#나머지 없는 경우와 있는 경우로 row 계산
if customer%col == 0:
    row = customer // col
else:
    row = customer // col +1 #몫+1

for i in range(0, row):
    for j in range(0, col+1):
        seat = i*col+j
        if seat>customer:
            break
        print("좌석",seat, end=" ")
    print()
