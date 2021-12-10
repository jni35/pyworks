import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')  #resp.text로 생략하지 않도록 주의!

# 지하철 이미지 경로 출력
target_img = soup.find('img', attrs={'alt':'Seoul-metro-2009-20180916-103548.jpg'})
print(target_img)

# 지하철 이미지를 파일에 저장(쓰기)
target_img_src = target_img.get('src')
print("이미지 경로:", target_img_src)

#이미지 파일 경로 url 경로
target_img_resp = requests.get("http:" + target_img_src)

#바이너리 파일 쓰기
with open("./output/subway_train.jpg","wb") as f:
    f.write(target_img_resp.content)    #이미지.content 속성 사용
