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

#t = Turtle()
#t.left(90)
#t.backward(300)
#Recursive_Koch(t, 5, 4)
#screen = t.Screen()
#screen.exitonclick()

#4! - 階乗
# 4 factorial
def fact(n):
    result = 1 
    for i in range(n):
        print(i + 1) # for debug
        result *= (i + 1)
    return result

res = fact(4)
print(res)

def fact0(n):
    # fact(1): return 1
    # fact(2): 2 * fact(2-1) = 2 * fact(1)
    # fact(3): 3 * fact(3-1) = 3 * fact(2)
    # fact(4): 4 * fact(4-1) = 4 * fact(3)
    # 4 * 3 * 2 * 1 = 4 * (3 * 2 * 1) = 4 * fact(3)
    #--------------
    # N! = N * (N-1) * (N-2) ...... 3 * 2 * 1
    # N! = N * (N-1)!

    if n == 1:
        return 1 # this is the first practice
    return n * fact0(n-1)
print(fact0(5))
print(fact0(40))
