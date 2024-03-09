with open("blank.txt") as file:
    for i in file:
        print(f'{i}')
text = input()
with open('lessane_9.txt', 'w') as file_2:
    file_2.write(text)
with open('lessane_9.txt',) as file_2:
    print(file_2.read())