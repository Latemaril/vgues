from tkinter import *


def clicked(): # Создаём функцию для вывода текста после клика по кнопке
    lbl.configure(text='Короче тут я пока ничего не придумал', fg='blue') # Меняем настройки текста с помощью configure(настроить)


def clicked1(): # Создаём функцию для отображения введённого текста с некоторым словом(В данном случае перед текстом будет Гачи)
    res = "Привет {}".format(txt.get()) # Можно получить текст ввода, использую функцию get(непонятная херня так что лучше просто запомнить)
    lbl1= Label(root, text=res, fg='purple', font=('Arial Bold', 60))
    lbl1.grid(column=0, row=2)
    

root = Tk() # Собственно создаём окно с помощью класса Tk. root это переменная и вместо неё можно написать например window
root.title('Знакомство с модулем окон') # Задаём название окна


lbl = Label(root, text='Здарова славяне', fg='purple', font=('Arial Bold', 50)) # Создаём текст в окне с помощью класса Label.fg - цвет текста, font - шрифт
lbl.grid(column=0, row=0) # Расположение текста(ряд и столбец)
root.geometry('1280x600') # Задаём размер окна по пикселям(ось x на ось y)


btn = Button(root, text='Нажми меня', fg='red', bg='black', font=('Arial', 18), command=clicked) # Создаём кнопку с помощью класса Button, btn также переменная. bg - цвет фона, command - команда которая выполняется после клика по кнопке
btn.grid(column=1, row=0 ) 


btn1 = Button(root, text='Клик!', fg='red', bg='black', font=('Arial', 18), command=clicked1) 
btn1.grid(column=1, row=1)


txt = Entry(root, width=40) # Используем класс для пользовательского ввода текста. width(ширина) - ширина окна ввода
txt.grid(column=0, row=1)


root.mainloop() # Mainloop - функция, которая вызывает бесконечный цикл окна, поэтому окно будет ждать любого взаимодействия с пользователем, пока не будет закрыто