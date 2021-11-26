import time
import math
print(time.time())      # 1970. 01. 01. 자정이후 초로 롼산
days = round(time.time()/(24*60*60))        # 초를 1로 환산
year = round(time.time()/(365*24*60*60))    # 초를 년으로 환산

print("{}일".format(days))
print("{}년".format(days))

# time.sleep() x초만큼 시간 간격을 둠
# for문 수행 시간 측정
start = time.time()

for i in range(10):
    print(i)
    time.sleep(1)  #파이썬 1 : 1초, 다른언어 1000 : 1초

end = time.time()
et = math.floor(end-start)
print("for문 수행 시간 : {}초".format(et))
