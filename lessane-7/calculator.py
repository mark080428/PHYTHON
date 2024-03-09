import tkinter
window = tkinter.Tk()
window.title('калькулятор')
window.geometry('300x300')

window.configure(bg='silver')

def set_answer(result):
    text_num_3.delete(0, 'end')
    text_num_3.insert(0, result)

def add():
    num_1 = int(text_num_1.get())
    num_2 = int(text_num_2.get())
    result = num_1 + num_2
    set_answer(result)


def subster():
    num_1 = int(text_num_1.get())
    num_2 = int(text_num_2.get())
    result = num_1 - num_2
    set_answer(result)


def share():
    num_1 = int(text_num_1.get())
    num_2 = int(text_num_2.get())
    result = num_1 / num_2
    set_answer(result)

def multiply():
    num_1 = int(text_num_1.get())
    num_2 = int(text_num_2.get())
    result = num_1 * num_2
    set_answer(result)



buttom_ate = tkinter.Button(window, text='+', command=add, width=7, height=2, bg='gold')
buttom_ate.place(x=65, y=110)
buttom_supp = tkinter.Button(window, text='-', command=subster, width=7, height=2, bg='gold')
buttom_supp.place(x=162, y=110)
buttom_mult = tkinter.Button(window, text='*', command=multiply, width=7, height=2, bg='gold')
buttom_mult.place(x=65, y=170)
buttom_share = tkinter.Button(window, text='/', command=share, width=7, height=2, bg='gold')
buttom_share.place(x=162, y=170)

text_num_1 = tkinter.Entry(window, width=20, bg='black', fg='white')
text_num_1.place(x=65, y=30)
text_num_2 = tkinter.Entry(window, width=20, bg='black', fg='white')
text_num_2.place(x=65, y=81)
text_num_3 = tkinter.Entry(window, width=20, bg='black', fg='white')
text_num_3.place(x=65, y=255)


label_num_1 = tkinter.Label(window, text='Введите первое число', bg='silver')
label_num_1.place(x=65, y=4)
label_num_2 = tkinter.Label(window, text='Введите второе число', bg='silver')
label_num_2.place(x=65, y=61)
label_num_3 = tkinter.Label(window, text="Ответ", bg='silver')
label_num_3.place(x=65, y=225)
window.mainloop()