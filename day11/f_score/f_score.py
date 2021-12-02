# 파일의 과목의 성적 저장
with open('score.txt', 'w') as f:
    try:
        name = input("이름 입력 : ")
        kor = int(input("국어 점수 : "))
        math = int(input("수학 점수 : "))
        sum_v = kor + math
        avg = sum_v/2
    except ValueError:
        print("유효한 숫자가 아닙니다. 다시 입력해 주세요.")

    f.write(name + ' ')
    f.write(str(kor) + ' ')    # 숫자를 문자로 형변환
    f.write(str(math) + ' ')
    f.write(str(sum_v) + ' ')
    f.write(str(avg) + '\n')

