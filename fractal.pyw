import turtle as t
t.pencolor('blue')
t.pensize(1)

def ReshetkaSerpinskogo(level, n):
    if (n == 8):
        return level
    newlevel = ''
    for i in level:
        if i == '+':
            newlevel = newlevel + '+'
        elif i == '-':
            newlevel = newlevel + '-'
        elif i == 'F':
            newlevel = newlevel + 'FF'
        elif i == 'X':
            newlevel = newlevel + '--FXF++FXF++FXF--'
    level = newlevel
    return ReshetkaSerpinskogo(level, n + 1)
w = ReshetkaSerpinskogo('FXF--FF--FF', 1)
t.speed(2000000000000)
t.penup()
t.setx(-300)
t.sety(300)
t.pendown()
for i in w:
    if i == '-':
        t.left(120)
    elif i == '+':
        t.right(120)
    else:
        t.forward(5) 
            
