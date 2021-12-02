# 영어 타자 게임
import random as r
import time

with open("word.txt", "r") as f:
    word = f.readline().split()     # 단어 전체 공백문자로 구분

n = 1   # 문제 번호
input("[타자게임}준비되면 엔터!")
start = time.time()
while n < 11:
    print('-문제', n)
    question = r.choice(word)  # 문제 단어 출력
    print(question)
    answer = input()    # 답을 입력
    # 통과 이니면 오타 코드 작성
    if question == answer:
        print("통과")
        n += 1
    else:
        print("오타! 다시 도전!")
end = time.time()
print("게임 소요 시간 : %.2초" % (end-start))
