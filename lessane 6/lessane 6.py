# def say_hello():
#     print('Привет')
# say_hello()
# say_hello()
# def say_hello(name):
#     print(f'Привет {name}')
# say_hello('Марк')
# say_hello('Андрей')
# month = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
# lange = len(month)
# for i in range(lange):
#     print(f'{i+1}. {month[i]}')
# def areas_square(side):
#     s = side * side
#     print(f'Площадь квадрата со стороной {side} = {s}')
# areas_square(100)
# def areas_rectangle(side_b, side_a):
#     s_rectangle = side_a * side_b
#     print(f'Площадь прямоугольника со сторонами: {side_a} и {side_b} равна {s_rectangle}')
# areas_rectangle(5, 10)
# import random
# def lotary():
#     tickets = [13, 35, 2, 58, 24, 65, 86, 42]
#     ticket = random.choice(tickets)
#     return ticket
# print(lotary())
# winner = lotary() + 2
# print(winner)
#

summa = lambda x, y: x + y**2
print(summa(4, 5))