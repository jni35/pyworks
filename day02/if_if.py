#if 중첩문
num=int(input("숫자를 입력하세요 : "))

if num >10:
    if num%2==0:
        print("10보다 큰 짝수 입니다.")
    else:
        print("10보다 큰 홀수 입니다.")
else:
    if num%2==0:
        print("10이하의 짝수 입니다.")
    else:
        print("10이하의 홀수 입니다.")


#if ~elif~else문 호환
if num>10 and num%2==0:
    print("10보다 큰 짝수 입니다.")
elif num>10 and num%2==1:
    print("10보다 큰 홀수 입니다.")
elif num<=10 and num%2==0:
    print("10이하의 짝수 입니다.")
else:
    print("10이하의 홀수 입니다.")
