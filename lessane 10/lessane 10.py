import tkinter as tk
import tkinter.messagebox as tm
window = tk.Tk()
window.title('Крестики - нолики')
window.geometry('300x300')
window.resizable(False, False)
area = []
def Win():
    if area[0][0]["text"] == "X" and area[0][1]["text"] == "X" and area[0][2]["text"] == "X":
        return "X"
    if area[1][0]["text"] == "X" and area[1][1]["text"] == "X" and area[1][2]["text"] == "X":
        return "X"
    if area[2][0]["text"] == "X" and area[2][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][0]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][1]["text"] == "X" and area[1][1]["text"] == "X" and area[2][1]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][2]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][1]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "0" and area[0][1]["text"] == "0" and area[0][2]["text"] == "0":
        return "0"
    if area[1][0]["text"] == "0" and area[1][1]["text"] == "0" and area[1][2]["text"] == "0":
        return "0"
    if area[2][0]["text"] == "0" and area[2][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][0]["text"] == "0" and area[1][0]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    if area[0][1]["text"] == "0" and area[1][1]["text"] == "0" and area[2][1]["text"] == "0":
        return "0"
    if area[0][2]["text"] == "0" and area[1][2]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][0]["text"] == "0" and area[1][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][2]["text"] == "0" and area[1][1]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    return ""
turn = 1
def push(button):
    global turn
    print(turn)
    turn = turn + 1
    if turn % 2 == 0:
        char = '0'
        print(f'Ходят {char}')
    else:
        char = 'X'
        print(f'Ходят {char}')
    if button['text'] is '':
        button['text'] = char
    if Win() == 'X':
        tm.showinfo(title='Победитель', message='Победили X')
        new_game()
    if Win() == '0':
        tm.showinfo(title='Победитель', message='Победили 0')
        new_game()
    if Win() == '' and turn == 10:
        tm.showinfo(title='Конец игры', message='Ничья')
        new_game()

def new_game():
    global area, turn
    turn = 1
    for x in range(3):
        for y in range(3):
            area[x][y]['text'] = ''
for i in range(3):
    area.append([])
    for y in range(3):
        button = tk.Button(window, text='', width=13, height=6)
        area[i].append(button)
        area[i][y].place(x=i*100, y=y*100)
        area[i][y]['command'] = lambda selected_button = button: push(selected_button)
window.mainloop()