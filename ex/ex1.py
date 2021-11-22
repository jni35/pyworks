#146
#1

a="Life too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")   #shirt -> 끝난다.
elif "need" in a: print("need")     # need
else: print("none")
#if(만약)/ elif(아니면 만약).../else(아니면)

'''
if "wife" in a: print("wife")
if "python" in a and "you" not in a: print("python")
if "shirt" not in a: print("shirt")   #shirt -> 끝난다.
if "need" in a: print("need")     # need
else: print("none")
'''


#2
result: int = 0
count = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        count += 1
        result += i
    i += 1

print("개수 :", count)
print("합계 :", result)

#3
print("="*30)
print("*"*5)

i = 0
while True:
    i += 1
    if i > 5: break
    print("*"*i)

#직각 삼각형 모양
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")
    print()
print()



#4
for i in range(0, 101):
    print(i)

#5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
avg = total/len(A)
print("합계 :",total)
print("평균 :",avg)

#6
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

# numbers = [1, 2, 3, 4, 5]
# result =
# print(result)

