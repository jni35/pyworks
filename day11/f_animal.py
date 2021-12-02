# 파일을 읽어서 이차원 리스트 만들기
with open('animal.txt','w')as f:
    animal = ['dog', 'cow', 'cat', 'pig']

    # 파일에 쓰기
    for i in animal:
        f.write(i+'\n')

# animal.txt 읽기
with open('animal.txt','r')as f:
    # animal = f.readlines()
    # print(animal)     # 1차원 리스트
    # 2차원 리스트
    animal = []
    for i in range(4):
        animal.append(f.readline().split())     # 공백제거 리스트에 저장
    print(animal)















