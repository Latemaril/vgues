import time
from tkinter import Tk, Label

root = Tk()
root.title('clock')
root.geometry('+10+10')

lb = Label(root, bg = 'black', fg='blue', text = 'Python', font='Segoe Print 90')
lb.pack(ipadx=20, ipady=20)


def gettime()
    p = ':' if int(time.strftime('%S')) % 2 == 0 else ' '
    lb['text'] = time.strftime(f'H{p}%{p}%S')
    lb.after(1000, gettime)


gettime()


root.mainloop()


while True:
    pass