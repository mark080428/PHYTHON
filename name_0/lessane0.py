##print(5)
##print('5+5')
##print("Hello world!")
##print('Hello world '+"From Mark")
##my_name = "Mark"
##print(my_name)
##print("Меня зовут "+my_name)
##name=input("Введите ваше имя ")
##print()
##print('Привет '+name)
import random
print("Компьютер загадал число от 1 до 10. Попробуйде его угадать")
items= 3
sekret_number=random.randint(1,10)
while items > 0:
    user_number=int(input('введите число: '))
    ##print(user_number)
    if sekret_number > user_number:
        print("секретное число больше")
    if sekret_number < user_number:
        print("секретное число меньше")
    if sekret_number == user_number:
        print("ты победил")
        break
##    items=items-1
    items -= 1
    if items == 0:
        print("ты проиграл")
        print("Секретное число "+str(sekret_number))
