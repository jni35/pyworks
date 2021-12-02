# 반복해서 과목의 성적 저장
# y키 누르면 계속 저장, n키 누르면 종료

with open('scorelist.txt', 'a') as f:
    while True:
        try:
            key = input("성적을 저장할까요(y/n)")
            if key == 'n':
                break
            elif key == 'y':
                name = input("이름 입력 : ")
                kor = int(input("국어 점수 : "))
                math = int(input("수학 점수 : "))

                f.write(name + ' ')
                f.write(str(kor) + ' ')  # 숫자를 문자로 형변환
                f.write(str(math) + '\n')
            else:
                print("잘못된 입력입니다. 다시 입력해 주세요.")
        except ValueError:
            print("유효한 숫자가 아닙니다. 다시 입력해 주세요.")
    print("입력을 종료합니다.")