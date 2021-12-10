#바이너리 파일 쓰고 읽어오기
# wb, rb 모드 사용
with open('data.bin','wb') as f:
     text = "비가 내린다."
     f.write(text.encode()) #text를 인코딩함

with open('data.bin','rb') as f:
     data = f.read()
     text = data.decode()     #코드화된 텍스트를 디코딩함
     print(text)

