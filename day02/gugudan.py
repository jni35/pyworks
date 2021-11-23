#구구단
dan= int(input("단을 입력하세요 : "))

print("[", dan, "]단")
for i in range(1, 10):
    print(dan, "*", i, "=", dan*i)
