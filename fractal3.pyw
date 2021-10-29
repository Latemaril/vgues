import turtle as t
t.pencolor('green')
t.pensize(2)

def KrivadratGospera(level, n):
    if (n == 3):
        return level
    newlevel = ''
    for i in level:
        if i == '+':
            newlevel = newlevel + '+'
        elif i == '-':
            newlevel = newlevel + '-'
        elif i == 'X':
            newlevel = newlevel + 'XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-'
        elif i == 'Y':
            newlevel = newlevel + '+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY'
    level = newlevel
    return KrivadratGospera(level, n + 1)
w = KrivadratGospera('YF', 1)
t.speed(2000000000)
t.penup()
t.setx(-300)
t.sety(100)
t.pendown()
for i in w:
    if i == '-':
        t.left(90)
    elif i == '+':
        t.right(90)
    else:
        t.forward(5) 
            
