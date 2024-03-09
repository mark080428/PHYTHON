##age = int(input('Введите ваш возраст: '))
##print(age<14)
##if age<14:
##    print('Ты младше 14')
##if age>14:
##    print('Ты старше 14')
##if age == 14:
##    print("Тебе 14 лет")
##    
##if age <= 14:
##    print('Ты младше 14 либо тебе 14')
##if age >= 14:
##    print('Ты старше 14 либо тебе 14')
##if age != 14:
##    print('Тебе не 14 лет')
##
##if 7 <= age <= 17:
##    print("Ты ходишь в школу")

##if "пять" == "пять":
##    print("Строка 5 равна строке 5")
##
##if "5" == "5":
##    print("пять равно пяти")
##
##if 5 == int("5"):
##    print("cвершилось чудо!")
##
##if 5 != int("5"):
##    print("Неравно!")
##text= "На столе лежит тетрадь и карандаш"
##if "тетрадь" in text:
##    print("Я нашёл тетрадь")
##if "ручка" not in text:
##    print('Нету ручки')

##number= int(input('Введите число: '))
##if number % 2 == 0:
##    print("Число чётное")
##else:
##    print('Число не чётное')

##temp= int(input("Какая сейчас температура? "))
##if temp <= 0:
##    print('Очень холодно')
##elif 0 < temp <= 12:
##    print('ХОлодно')
##elif 12 < temp <= 18:
##    print('ПРохладно')
##elif 18 < temp <= 25:
##    print('тепло')
##elif 25 < temp <= 32:
##    print('жарко')
##else:
##    print('ООООООчень жарко')

##money= True
##seets= False
##if money == True and seets == True:
##    print('Мы можем посмотреть фильм')
##else:
##    print('Мы не можем посмотреть фильм')
##
##age= 11
##parents= False
##if age >= 12 or parents == True:
##    print('Ты можешь купить билет')
##else:
##    print('Ты не можешь купить билет')
print('Введите любое число, если оно делится на 3 то я скажу Кала, если оно делится на 5 то я скажу банга, если оно делится и на 3 и на 5 тоя скажу: КАЛАБАНГА')
number= int(input('Введите число: '))
if number %3 == 0 and number %5 == 0:
    print('КАЛАБАНГА!!!!')
elif number %3 == 0:
    print('Кала')
elif number %5 == 0:
    print('Банга')
