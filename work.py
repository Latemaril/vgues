import numpy as np


a = [1, 2, 3, 56, 74]
print(len(a))
c = 0


for b in a:
    if b < 50:
        print(b)
print(sum(a))


for b in a:
    c += b
print(c)


def Hello():
    print("Какаду")


Hello()


def Hi2(x, y):
    if x > y:
        return x
    return y


def Hi3(x, y, z):
    return Hi2(x, Hi2(y, z))


def Hi6(x, y, z, w, e, t):
    return Hi2(Hi3(x, y, z), Hi3(w, e, t))



print(Hi6(3, -412, 14, 30, 45, 2))        


m = [1, 5, 2, 7, 6, 3]
print(len(m))


def summa():
    k = 0
    for n in m:
        k += n
    print(k)


def mn():
    l = 1
    for n in m:
        l = n * l
    print(l)


def sred():
    j = 0
    h = 0
    for n in m:
        j += n
    h = j / len(m)
    print(j)    


summa()
mn()
sred()

A = np.array([[input(), input(), input()], [input(), input(), input()], [input(), input(), input()]])

B = np.array([[input(), input(), input()], [input(), input(), input()], [input(), input(), input()]])

print(A + B)


