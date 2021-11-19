#홑 따옴표, 쌍 따음표로 감싸서 문자열을 표기

say = '"힘내세요"라고 말했습니다.'
print(say)

#여러줄 출력하기
print("="*30)

song1 = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세

남산위에 저소나무 철갑을 두른 듯
바람서리 불변함은 우리 기상일세
"""

print(song1)
print("="*30)

#이스케이프 문자 사용하기 /t(탭) - 문자 간격, /n(줄바꿈)
table = """
이름/t나이/t지역
김화성/t21/t화성
이목성t31//t목성
"""

print(table)

head = "python"
tail = "is fun!"
print(head + tail)
print(head *2)

