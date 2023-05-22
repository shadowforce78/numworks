# Input asking for the user : Derivee ou primitive ? (d/p)

import math
from turtle import *
from kandinsky import *



# Fonction f(x)     # Fonction f'(x) 
# ax+b              # a
# x^n               # nx^(n-1)
# 1/x               # -1/x^2
# sin(x)            # cos(x)
# cos(x)            # -sin(x)
# sin(wT+p)         # w*cos(wT+p)
# cos(wT+p)         # -w*sin(wT+p)
# sqrt(x)           # 1/(2*sqrt(x))
# ln(x)             # 1/x
# e^x               # e^x

# Fonction f(x)     # Fonction F(x)
# a                 # ax+b        
# x^n               # 1/(n+1)*x^(n+1)
# 1/x^2             # -1/x
# sin(x)            # -cos(x)
# cos(x)            # sin(x)
# sin(wT+p)         # (-1/w)*cos(wT+p)
# cos(wT+p)         # (1/w)*sin(wT+p)
# 1/sqrt(x)         # 2*sqrt(x)
# e^x               # e^x
# 1/x               # ln(x)  


def main():
    state = input("Derivee ou primitive ? (d/p)")
    if state == "d":
        derivee()
        return
    elif state == "p":
        # primitive()
        return
    else:
        print("Erreur de saisie")
        main()


def derivee():


    # Draw a 320*222 grid with 10 rows and 2 columns
    hideturtle()
    speed(0)
    penup()
    goto(-160, -111)
    pendown()
    for i in range(10):
        forward(320)
        penup()
        backward(320)
        left(90)
        forward(22.2)
        right(90)
        pendown()
    penup()
    goto(-160, 111)
    left(90)
    pendown()

    goto(0, 222)
    goto(0, -222)


    # Write the function
    goto(-160, 111)
    pendown()
    for x in range(-160, 160):
        y = 0.1*x
        goto(x, y)
    penup()

    # Write the derivative
    goto(-160, 111)
    pendown()
    for x in range(-160, 160):
        y = 0.1*x
        goto(x, y)
    penup()









main()