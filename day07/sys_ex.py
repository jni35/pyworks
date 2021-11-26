# 시스템 모듈
# 명령행(cmd창 -명령프롬프트)에서 인수 전달하기
import sys

args = sys.argv[1:]     # 리스트 1번부터 끝까지 슬라이싱
print(args) # 리스트 출력

# 리스트 값 출력
for i in args:
    print(i)
