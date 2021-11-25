# 가변 매개변수 - 입력값이 정해지지 않고 변경할 수 있는 변수
# 매개변수 앞에 *을 붙임
def calc_avg(*number):
    sum_v = 0
    for i in number:
        sum_v += i
    avg = sum_v / len(number)
    return avg

avg1 = calc_avg(1, 2)
avg2 = calc_avg(1, 2, 3)
print(avg1)
print(avg2)
