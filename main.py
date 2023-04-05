import os
import tkinter
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('400x250')
window.title("Задание № 3")

file_title = tkinter.StringVar()
file_content = None

def open_file():
    global file_content
    try:
        dir = 'C:/Users/User/PycharmProjects/pythonProject/'
        file_name = file_title.get()
        full_path = os.path.join(dir, file_name)
        fb = open(full_path,'r', encoding="utf-8")
        file_content = fb.read()
    except:
        file_content = 'Файла с таким название не существует'
    text_box.delete('1.0', END)
    text_box.insert(INSERT, file_content)

def retrieve_input():
    input_value = text_box.get("1.0",END)
    return input_value

def save_file():
    global file_content
    file_content = retrieve_input()
    if file_content:
        dir = 'C:/Users/User/PycharmProjects/pythonProject/'
        file_name = file_title.get()
        full_path = os.path.join(dir, file_name)
        fb = open(full_path, 'w', encoding="utf-8")
        fb.write(file_content)
        fb.close()

entry = ttk.Entry(window, textvariable=file_title)
entry.pack()

button1 = ttk.Button(window, text="Открыть", command=open_file)
button1.pack()

button2 = ttk.Button(window, text="Сохранить", command=save_file)
button2.pack()

text_box = Text(window, width=100, height=100)
text_box.pack()

window.mainloop()