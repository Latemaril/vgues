import turtle as tu

def Koch(length):
    if length <= 2 :
        tu.fd(length)
        return
    Koch(length/2)
    tu.lt(50)
    Koch(length/2)
    tu.rt(100)
    Koch(length/2)
    tu.lt(50)
    Koch(length/2)


tu.speed(0)
length = 300.0
tu.penup()
tu.backward(length/2.0)
tu.pendown()
Koch(length)
tu.done()