# homework = ["сделать алгебру", 'физику', 'литературу', 'програмирование']
# print(homework)
# print(homework[0])
# homework[1] = 'Математика'
# print(homework)
# homework.append('ОБЖ')
# print(homework)
# homework.remove('ОБЖ')
# print(homework)
# delo = homework.pop()
# print(homework)
# print(delo)
# delo2 = homework.index('Математика')
# print(delo2)
#
# text = ['танки', 'песни', 'философия']
# print(text)
# if 'песни' in text:
#     print('я люблю песни')
# if 'песни' not in text:
#     print('не люблю песни')
# for i in text:
# #     print(i)
# # lange = len(text)
# # print(lange)
# # for i in range(lange):
# #     print(f'{i+1}. {text[i]}')

import random
harakter = ["мудрый", "дерзкий", "жизнерадостный", "хромой", "трусливый", "смелый", "бешеный", "гордый", "лопоухий", "неудержимый"]
animals = ["тигр", "суслик", "орел", "заяц", "олень", "кабан", "сайгак", "медведь", "мустанг", "жираф"]
first_name = random.choice(harakter)
second_name = random.choice(animals)
print(f'Племени индейцев тумба-юмбы тебя назвали {first_name}-{second_name}')