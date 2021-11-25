# 전역변수

def one_up():
    global x
    x += 1
    return x

x = 1   #전역변수(프로그램이 종료될때 메모리에서 해제)
print(one_up())     #2
print(one_up())     #3
print(one_up())     #4
print(x)     #전역변수(프로그램이 종료될때 메모리에서 해제)