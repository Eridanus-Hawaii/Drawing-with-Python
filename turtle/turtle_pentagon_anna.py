import turtle 
import numpy as np 
import math
obj = turtle.Turtle()
def polygon(t, n, r):
    #theta = 180 - (180 - (360 / n))
    theta = 360 / n
    step = r * 2 * np.sin(np.pi/n)
    for i in range(n):
        t.right(theta)
        t.forward(step)

polygon(obj, 5, 100)
polygon(obj, 98, 100)
screen = turtle.Screen()
screen.exitonclick()