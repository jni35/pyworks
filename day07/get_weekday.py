# 날짜로 요일 알아내기
import datetime

def get_weekday(yyyy, mm, dd):
    days = ["월","화","수","목","금","토","일"]
    x = datetime.date().weekday()   # 요일 결과는 숫자로 출력("월"-0,.....)
    print(x)
    return days[x]

yyyy = 2021
mm = 11
dd = 25

weekday = get_weekday(yyyy, mm, dd)
print("{}요일".format(weekday))


