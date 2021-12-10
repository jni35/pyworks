import requests #url의 접속 밎 정보를 가져오는 모듈(pip install requsts)

#로봇 배제 표준 내역 가져오기

url = "https://www.naver.com/robots.txt"

response = requests.get(url)    # url 요청해 응답 객체 생성
print(response)     # 200=성공, 404=실패
print(response.text)

response2 = requests.get("http://www.python.org/robots.txt")
print(response2)
print(response2.text)