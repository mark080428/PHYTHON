import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm

window = tk.Tk()
window.geometry("400x400")
window.title("Блокнот")

file_name = ""

def write_to_file(file_name):
    content = content_text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(content)

def open_file():
    content_text.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    file_label["text"] = "Файл: "+file_name
    with open(file_name) as file:
        content_text.insert(1.0, file.read())
        
def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    file_label["text"] = "Файл: " + file_name
    write_to_file(file_name)

def save_file():
    global file_name
    if file_name=="":
        save_as_file()
    else:
        write_to_file(file_name)
        tkm.showinfo("Файл сохранен","Сохранения записаны в файл "+file_name)


def new_file():
    global file_name
    if tkm.askokcancel("Создание нового файла", "Вы уверены? Несохраненный текст будет удален"):
        file_name = ""
        file_label["text"] = "Файл: " + file_name
        content_text.delete(1.0, "end")


content_text = tk.Text(window, wrap="word")
content_text.place(relx=0,rely=0, relwidth=1, relheight=1)

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)

new_file_icon = tk.PhotoImage(file='new_file.gif')
open_file_icon = tk.PhotoImage(file='open_file.gif')
save_file_icon = tk.PhotoImage(file='save_file.gif')

file_menu.add_command(label="Новый", compound='left', image=new_file_icon, command = new_file)
file_menu.add_command(label="Открыть", compound='left', image=open_file_icon, command = open_file)
file_menu.add_command(label="Сохранить", compound='left', image=save_file_icon, command = save_file)
file_menu.add_command(label="Сохранить как", compound='left', image=save_file_icon, command = save_as_file)

file_label = tk.Label(window, text="Файл: "+file_name)
file_label.place(relx=0, rely=1, anchor="sw")

tkm.showinfo("Добро пожаловать!","Вас приветствует программа\"Мой блокнот\"")
window.mainloop()

