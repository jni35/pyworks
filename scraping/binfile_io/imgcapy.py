# 이미지 파일을 읽어서 쓰기

with open("../healing.jpg",'rb') as f1:
    pic = f1.read()

with open("./healing2.jpg",'wb') as f2:
    f2.write(pic)
    
