# 여러개의 원 그리기
import turtle as t

n = 100
t.speed(0)      #1~10, 가장빠른속도 - 0
t.bgcolor("black")      # 무대 배경 색
t.color('green')        # 거북이 색
for i in range(n):
    t.circle(100)
    t.left(360/n)       #7.5

t.mainloop()
