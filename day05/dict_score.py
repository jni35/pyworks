# 학생의 성적 합계 및 평균
# 대응 서식 문자 - 정수 : %d, 실수:%f, 문자열:%s

students = [
    {'name':'김하나', 'kor': 80, 'math': 70, 'eng': 90},       #1명의 세과목의 점수
    {'name':'이두울', 'kor': 60, 'math': 50, 'eng': 40},
    {'name':'박세엣', 'kor': 90, 'math': 90, 'eng': 80}
]

# 개인별 총점과 평균
print(" 이름 총점 ")
for s in students:
    sum_v = s['kor'] + s['math'] + s['eng']
    avg = sum_v / 3
    print("%s  %d %.1f" % (s['name'], sum_v, avg))

# 과목별 총점과 평균
'''
sum_kor = 0      #국어 합계
sum_math = 0     #수학 합계
sum_eng = 0      #영어 합계
'''
sum_subj = [0, 0, 0]    #리스트로 초기화
avg_subj = [0.0, 0.0, 0.0]

for s in students:
    sum_subj[0] += s['kor']
    sum_subj[1] += s['math']
    sum_subj[2] += s['eng']
print('국어 합계 : %d점' % sum_subj[0])
print('수학 합계 : %d점' % sum_subj[1])
print('영어 합계 : %d점' % sum_subj[2])

avg_subj[0] = sum_subj[0] / 3
avg_subj[1] = sum_subj[1] / 3
avg_subj[2] = sum_subj[2] / 3
print("국어 평균 : %.1f" % avg_subj[0])
print("수학 평균 : %.1f" % avg_subj[1])
print("영어 평균 : %.1f" % avg_subj[2])



