import turtle as t
t.pencolor('red')
t.pensize(3)

def KrivayaGospera(level, n):
    if (n == 8):
        return level
    newlevel = ''
    for i in level:
        if i == '+':
            newlevel = newlevel + '+'
        elif i == '-':
            newlevel = newlevel + '-'
        elif i == 'X':
            newlevel = newlevel + 'X+YF++YF-FX--FXFX-YF+'
        elif i == 'Y':
            newlevel = newlevel + '-FX+YFYF++YF+FX--FX-Y'
    level = newlevel
    return KrivayaGospera(level, n + 1)
w = KrivayaGospera('FX', 1)
t.speed(20000000000)
t.penup()
t.setx(-300)
t.sety(100)
t.pendown()
for i in w:
    if i == '-':
        t.left(60)
    elif i == '+':
        t.right(60)
    else:
        t.forward(5) 
            
