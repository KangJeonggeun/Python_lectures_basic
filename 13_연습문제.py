answer = 0

for i in range(10001):
    if i%3 == 0:
        answer += i
    elif i%7==0:
        answer += i

print(answer)

