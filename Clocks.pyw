import time
from tkinter import Tk, Label

root = Tk()
root.title('clock')
root.geometry('+10+10')

lb = Label(root, bg = 'black', fg='red', text='Python', font='arial 150')
lb.pack(ipadx=1280, ipady=720)


def gettime():
    p = ':' if int(time.strftime('%S')) % 2 == 0 else ' '
    r = '%H' if int(time.strftime('%S')) % 2 == 0 else 'Time'
    s = '%M' if int(time.strftime('%S')) % 2 == 0 else 'to'
    j = '%S' if int(time.strftime('%S')) % 2 == 0 else 'die'
    lb['text'] = time.strftime(f'{r}{p}{s}{p}{j}')
    lb.after(1000, gettime)


gettime()


root.mainloop()


