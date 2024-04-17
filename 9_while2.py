#5000이하의 자연수중 짝수만 출력하기

i = 0
while True:
    i+=1
    if i%2 == 1:
        continue
    print(i)

    if i == 5000:
        break

