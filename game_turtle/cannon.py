# 거북이 대포 게임
# 각도를 맞춰 대포를 발사해 목표지점을 맞히는 게임
import http.client
import turtle as t
import random as r
# 좌표 이동
# t.shape('turtle')
'''
t.up()
t.goto(0, 200)      # x=0, y=200
t.goto(0, -200)     # x=0, y=-200
t.goto(200, 0)      # x=200, y=0
t.goto(-200, 0)     # x=-200, y=0
'''
def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()       # 거북이가 바라보는 각도 설정

    while t.ycor() > 0:     # 거북이의 y좌표가 0보다 크면
        t.forward(15)       # 15픽셀 이동
        t.right(5)          # 오른쪽으로 5도 돌림

    #whlie 반복문을 빠져 나오면 땅에 닿은 상태임
    d = t.distance(target, 0)   # 거북이와 목표지점과의 거리 저장
    t.sety(r.randint(10, 100))  # 성공 또는 실패를 료시할 위치 지정
    if d < 25:
        t.color("blue")
        t.write("good!", False, "canter", ("", 15))  #명중 처리
        # 글자쓰기 함수("문자열",위치 이동 않음,가운데 정렬,글꼴 크기)
    else:   # 그렇지 않으면 실패한 것으로 처리
        t.color("red")
        t.write("bad!", False, "canter", ("", 15))  #명중 처리
        t.color("blue")
        t.goto(-200, 10)    # 거북이를 처음 위치로 되돌림
        t.setheading(ang)   # 각도를 처음 저장한 각도로 되돌림

# 땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

# 목표지점
target = r.randint(50, 150)     # 목표지점은 50~150 사이의 임의의 수
t.color('green')
t.pensize(2)
t.up()
t.goto(target - 25, 2)           # x좌표, y좌표:2
t.down()
t.goto(target + 25, 2)            # x좌표, y좌표:2

# 거북이의 처음위치 설정
t.color("black")        # 거북이를 검은색으로 변경
t.up()
t.goto(-200, 10)
t.setheading(20)

# 동작하는 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()

t.mainloop()
