mebel = [['Стол','Стул','Шкаф'], ['Стул','','Кресло']]

def viktory(i):
    if i [0] [2] == 'Кресло' and i [1] [2] == 'Шкаф':
        print('Победа!')
        return True
    else:
        return False

turn = 0

while not viktory(mebel):
    turn +=  1
    for i in mebel:
        print(i)
    row = int(input('Из какого квадрата хочешь передвинуть мебель?(1,2 или 3) ')) - 1
    column = int(input('Какая строка?(1 или 2)')) - 1
    row_2 = int(input('В какой квадрат хочешь передвинуть? ')) - 1
    column_2 = int(input('В какой стобец хочешь поставить?')) -1

    item = mebel[column] [row]

    if mebel[column_2][row_2] != '':
        print('Ход не возможен')
    else:
        mebel[column_2][row_2] = item
        mebel[column][row] = ''
    print(f'Сделан: {turn} ход')
    if turn > 4:
        print('ВЫ проиграли')
        break