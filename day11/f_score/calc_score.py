# 파일을 읽어서 성적의 총점과 평균 계산하기
with open('scorelist.txt', 'r') as f:
    score = []
    for i in range(3):
        score.append(f.readline().split())
    # print(score)

    # 총점 및 평균 계산
    for i in range(3):
        score[i][1] = int(score[i][1])      # 인덱싱한 국어(문자)를 숫자로 변환
        score[i][2] = int(score[i][1])      # 인덱싱한 수학(문자)를 숫자로 변환
        score[i].append(score[i][1] + score[i][2])
        score[i].append(score[i][3]/2)


    # 성적표 출력
    print("**********성적표**********")
    print("=========================")
    print("이름  국어  수학  총점  평균")
    print("=========================")
    for i in range(3):
        print("{}  {}  {}  {}  {}"
              .format(score[i][0], score[i][1], score[i][2], score[i][3], score[i][4]))
    print()

    print("**********과목별 평균**********")
    sum_subj = [0, 0]
    for i in range(3):
        sum_subj[0] += score[i][1]  # 국어 합계
        sum_subj[1] += score[i][2]  # 수학 합계

    print("국어 : %.2f, 수학 : %.2f" % (sum_subj[0]/3, sum_subj[1]/3))