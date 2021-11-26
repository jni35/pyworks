# threading 모듈 - 프로세스(프로그램 실행)의 작동, 즉 작업 단위를 말한다.
# 일정 시간 후에 타이머를 종료
import datetime
import threading

def call():
    print("타이머 종료!!")
    print(datetime.datetime.now())  # call 후의 시간

print(datetime.datetime.now())  # 현재 날짜와 시간
timer = threading.Timer(10, call)
timer.start()
# repeat() 콜백함수 - 매개변수로 함수를 사용
# 재귀함수 - 자신을 호출하는 함수와 비슷