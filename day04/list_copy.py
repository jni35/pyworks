# 리스트의 복사
a1 = [1, 2, 3, 4]
a2 = []     # 빈 리스트 생성
a3 = []

#a1에 5를 저장
a1.append(5)
print(a1)

#복사 저장(a1->a2)
for i in a1:
    a2.append(i*2)

print(a2)

#a1에서 a3에 홀수만 저장
for i in a1:
    if i % 2 == 1:
        a3.append(i)
print(a3)
