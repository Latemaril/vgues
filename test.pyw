from tkinter import *


def clicked(): # Создаём функцию для вывода текста после клика по кнопке
    lbl.configure(text='Пошёл нахуй программист ебаный!', fg='blue') # Обращаемся к модулю configure(настроить)


root = Tk() # Собственно создаём окно с помощью модуля Tk. root это переменная и вместо неё можно написать например window
root.title('Знакомство с модулем окон') # Задаём название окна


lbl = Label(root, text='Здарова славяне', fg='purple', font=('Arial Bold', 30)) # Создаём текст в окне с помощью модуля Label.fg - цвет текста, font - шрифт
lbl.grid(column=0, row=0) # Расположение текста(ряд и столбец)
root.geometry('770x150') # Задаём размер окна по пикселям(ось x на ось y)


btn = Button(root, text='Нажми меня', fg='red', bg='black', font=('Arial', 10), command=clicked) # Создаём кнопку с помощью модуля Button, btn также переменная. bg - цвет фона, command - команда которая выполняется после клика по кнопке
btn.grid(column=1, row=0 ) 


root.mainloop()