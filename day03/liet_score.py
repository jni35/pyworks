#점수의 합계와 평균, 최고 점수, 최저 점수


score = [70, 80, 90, 20, 40]
count = len(score)  #개수
sum_v = 0
# avg = 0.0
print(sum(70, 80, 90, 20, 40))
print(max(70, 80, 90, 20, 40))

#합계 계산
for i in score:
    sum_v += i

#평균 계산
avg = sum_v/count

#최고 점수
max_v = score[0]
for i in score:
    if max_v < i:
        max_v = i

#최저 점수
min_v = score[0]
for i in score:
    if max_v > i:
        max_v = i


print("개수 :", count)
print("합계 :", sum_v)
print("평균 :", avg)
print("최고점수 :", max(score))
print("최저점수 :", min_v)



