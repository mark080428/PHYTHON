import colorama
print(colorama.Fore.BLACK)
arena = [["", "", ""],["", "", ""],["", "", ""]]

def Win():
        if arena[0][0] == "X" and arena[0][1] == "X" and arena[0][2] == "X":
            return "X"
        elif arena[1][0] == "X" and arena[1][1] == "X" and arena[1][2] == "X":
            return "X"
        elif arena[2][0] == "X" and arena[2][1] == "X" and arena[2][2] == "X":
            return "X"


        elif arena[0][0] == "X" and arena[1][0] == "X" and arena[2][0] == "X":
            return "X"
        elif arena[0][1] == "X" and arena[1][1] == "X" and arena[2][1] == "X":
            return "X"
        elif arena[0][2] == "X" and arena[1][2] == "X" and arena[2][2] == "X":
            return "X"

        elif arena[0][2] == "X" and arena[1][1] == "X" and arena[2][0] == "X":
            return "X"
        elif arena[0][0] == "X" and arena[1][1] == "X" and arena[2][2] == "X":
            return "X"




        if arena[0][0] == "0" and arena[0][1] == "0" and arena[0][2] == "0":
            return "0"
        elif arena[1][0] == "0" and arena[1][1] == "0" and arena[1][2] == "0":
            return "0"
        elif arena[2][0] == "0" and arena[2][1] == "0" and arena[2][2] == "0":
            return "0"


        elif arena[0][0] == "0" and arena[1][0] == "0" and arena[2][0] == "0":
            return "0"
        elif arena[0][1] == "0" and arena[1][1] == "0" and arena[2][1] == "0":
            return "0"
        elif arena[0][2] == "0" and arena[1][2] == "0" and arena[2][2] == "0":
            return "0"

        elif arena[0][2] == "0" and arena[1][1] == "0" and arena[2][0] == "0":
            return "0"
        elif arena[0][0] == "0" and arena[1][1] == "0" and arena[2][2] == "0":
            return "0"

        return ''

for i_2 in range (1, 10):
    print(f'Ход: {i_2}')
    if i_2 % 2 == 0:
        char = '0'
        print(f"Ходят: {char}")
        print()
    else:
        char = 'X'
        print(f"Ходят: {char}")
        print()
    row = int(input('Введите номер строки (0, 1 или 2): '))
    row_2 = int(input('Введите номер столбца (0, 1 или 2): '))
    if arena [row] [row_2] == '':
        arena [row] [row_2] = char
    else:
        print('Ячейка занята')



    for i in arena:
        print(colorama.Fore.BLACK)
        print(i)
    if i_2 == 9 and Win() == '':
        print('Ничья')
    if Win() == 'X':
        print('Крестики победили')
        break
    if Win() == '0':
        print('Нолики победили')
        break