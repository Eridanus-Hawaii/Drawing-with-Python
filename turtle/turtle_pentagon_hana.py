import turtle 
import math

obj = turtle.Turtle()
def polygon(t, n, r):
    theta = (360 / n)
    step = r * 2 * math.sin(math.pi / n)
    for i in range(n):
        t.right(theta)
        t.forward(step)

polygon(obj, 99, 100)

polygon(obj, 5, 100)

polygon(obj, 9, 100)

screen = turtle.Screen()
screen.exitonclick()