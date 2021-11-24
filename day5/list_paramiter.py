# 리스트를 매개변수로 전달하기
# 점수의 평균 계산하기

def calc_avg(a):
    sum_v = 0
    print(len(a))   # 요소의 개수
    count = 0
    for i in a:
        sum_v += i
        count += 1
    # avg = sum_v /len(a)
    avg = sum_v /count
    return avg

v = [70, 90, 50, 80, 100, 70]
average = calc_avg(v)
print("평균 %.1f점" % average)

