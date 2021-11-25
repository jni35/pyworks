# 날짜로 요일 알아내기
import datetime
import calendar

days = ["월","화","수","목","금","토","일"]
print(days[0])

# 오늘의 요일
today = datetime.date.today().weekday()
print(today)
print(days[today])

# 특정한 날의 요일
theday = datetime.date(2021, 10, 26).weekday()
print(days[theday])

# 달력확인
calendar.prmonth(2021, 10)
