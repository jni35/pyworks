# word.txt 만들기
import random as r

with open("word.txt", "w") as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'strawberry', 'grape', 'garlic', 'onion', 'potato']
    for w in word:
        f.write(w + ' ')

# 단어를 랜덤하게 추출하기
with open("word.txt", "r") as f:
    # word = f.readlines()    # 리스트로 반환됨
    word = f.readline().split()     # 단어 전체 공백문자로 구분
    w = r.choice(word)      # 랜덤하게 단어 1개 추출
    print(w)





