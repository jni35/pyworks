# datetime - 날짜, 시간 표시하는 모듈
import datetime

print(datetime.datetime.today())    #날짜, 시간 모두 출력
print(datetime.datetime.now())    #날짜, 시간 모두 출력

print(datetime.date.today())        #날짜
# print(datetime.time())            #시간

now = datetime.datetime.today()
'''
print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))
'''
print("{}년 {}월 {}일".format(now.year, now.month, now.day))
print("{}시 {}분 {}초".format(now.hour, now.minute, now.second))

print(now.strftime("%Y.%m.%d %H:%M:%S"))
