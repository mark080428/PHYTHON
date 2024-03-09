import random
point = 100
while point > 0:
    user_numbers = int(input('Введите число от 2 до 12: '))
    if user_numbers > 12 or user_numbers < 2:
        print('Нельзя так!')
        continue
    bet = int(input('Введите ставку '))
    number = random.randint(1,6)
    number_2 = random.randint(1,6)
    print(f'Первый кубик: {number}')
    print(f'Второй кубик: {number_2}')
    summa = number + number_2
    print(f'Общяя сумма: {summa}')
    if summa < 7 and user_numbers < 7:
        print('Ты выиграл')
        point += bet
        print(f'Ваши очки равны {point}')
    elif summa > 7 and user_numbers > 7:
        print('Ты выиграл')
        point += bet
    elif summa == user_numbers:
        print('Джекпот')
        point += bet*4
    else:
        print('Ты приграл ставку')
        point -= bet
    print(f'У вас осталось: {point}')
    stop = input('Остановить игру? ')
    if stop == 'да':
        print('Игра остановлена')
        break

