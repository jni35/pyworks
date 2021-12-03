# try ~ except ~ else 구문
# 에러가 없으면 try~else 실행
# 에러가 있으면 try~except 실행
try:
    print('1번')
    with open('2021kbo.txt', 'r') as f:
        team = f.readlines()
except:
    print('2번')
    print('파일을 열 수 없습니다.')
else:
    for i in team:
        print(i, end='')
