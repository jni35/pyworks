# 용어 사전
dic = {
    "이진수" : "2진법으로 표기한 숫자, 0과 1로 구성됨",
    "함수" : "특정한 기능을 수행하는 명령어 코드 모음",
    "버그" : "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지"
            "않는 원인을 제공하는 코드 조각"
}

print("**********용어 사전**********")
x = input('정의되어 있는 단어를 입력하세요 : ')
try:
    print(dic[x])
except:
    print("정의된 단어가 없습니다.")
# 문제가 발생하면 프로그래밍이 정상적으로 동작하지 않을 수 있다.
# 예외 처리: try ~ except 구문 사용
