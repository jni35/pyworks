import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')  #resp.text로 생략하지 않도록 주의!

# print(soup.head)
print(soup.title)   #<title> 태그 출력
print(soup.title.string)    #태그를 제외한 문자열 출력

# 지하철 이미지 경로 출력
target_img = soup.find('img', attrs={'alt':'Seoul-metro-2009-20180916-103548.jpg'})
print(target_img)