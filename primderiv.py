# Input asking for the user : Derivee ou primitive ? (d/p)

from math import *
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
        primitive()
        return
    else:
        print("Erreur de saisie")
        main()


def derivee():


    # Draw a 320*222 grid with 10 rows and 2 columns
    hideturtle()
    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    speed(300)
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
    penup()

    # Fonction f(x)
    draw_string("ax+b", 50,1)
    draw_string("x^n", 50, 23)
    draw_string("1/x", 50, 45)
    draw_string("sin(x)", 50, 67)
    draw_string("cos(x)", 50, 89)
    draw_string("sin(wT+p)", 50, 115)
    draw_string("cos(wT+p)", 50, 137)
    draw_string("sqrt(x)", 50, 159)
    draw_string("ln(x)", 50, 181)
    draw_string("e^x", 50, 203)
    
    # Fonction f'(x)
    draw_string("a", 190, 1)
    draw_string("nx^(n-1)", 190, 23)
    draw_string("-1/x^2", 190, 45)
    draw_string("cos(x)", 190, 67)
    draw_string("-sin(x)", 190, 89)
    draw_string("w*cos(wT+p)", 190, 115)
    draw_string("-w*sin(wT+p)", 190, 137)
    draw_string("1/(2*sqrt(x))", 190, 159)
    draw_string("1/x", 190, 181)
    draw_string("e^x", 190, 203)




def primitive():
    
    # Draw a 320*222 grid with 10 rows and 2 columns
    hideturtle()
    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    speed(300)
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
    penup()


        # Fonction f(x)
    draw_string("a", 50,1)
    draw_string("x^n", 50, 23)
    draw_string("1/x^2", 50, 45)
    draw_string("sin(x)", 50, 67)
    draw_string("cos(x)", 50, 89)
    draw_string("sin(wT+p)", 50, 115)
    draw_string("cos(wT+p)", 50, 137)
    draw_string("1/sqrt(x)", 50, 159)
    draw_string("e^x", 50, 203)
    draw_string("1/x", 50, 181)
    
    # Fonction f'(x)
    draw_string("ax+b", 165, 1)
    draw_string("1/(n+1)*x^(n+1)", 165, 23)
    draw_string("-1/x", 165, 45)
    draw_string("-cos(x)", 165, 67)
    draw_string("sin(x)", 165, 89)
    draw_string("(-1/w)*cos(wT+p)", 161, 115)
    draw_string("(1/w)*sin(wT+p)", 165, 137)
    draw_string("2*sqrt(x)", 165, 159)
    draw_string("ln(x)", 165, 181)
    draw_string("e^x", 165, 203)


main()