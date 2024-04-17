cola = 2

while True:
    money = int(input('돈을 넣어주세요'))

    if money == 1000:
        print('콜라를 받으세요')
        cola -= 1
        print(f'남은 콜라의 개수는 {cola}개 입니다.')

    elif money > 1000:
        print('콜라를 받으세요')
        print(f'거스름돈은 {money - 1000}원 입니다.')
        cola -= 1
        print(f'남은 콜라의 개수는 {cola}개 입니다.')

    elif money < 1000:
        print('돈이 부족합니다')
        print(f'반환되는 {money}원을 받으세요')
        print(f'남은 콜라의 개수는 {cola}개 입니다.')

    if cola == 0:
        break

print('모든 콜라가 판매 되었습니다')
print('자판기를 이용해 주셔서 감사합니다.')







    


        


    

