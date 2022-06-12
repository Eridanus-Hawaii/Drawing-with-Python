from turtle import *

def Recursive_Koch(t, length, depth):
    if depth == 0:
        t.forward(length)
    
    else:
        Recursive_Koch(t, length, depth-1)
        t.right(60)
        Recursive_Koch(t, length, depth-1)
        t.left(120)
        Recursive_Koch(t, length, depth-1)
        t.right(60)
        Recursive_Koch(t, length, depth-1)

t = Turtle()
# t.left(90)
# t.backward(300)
Recursive_Koch(t, 5, 8)

