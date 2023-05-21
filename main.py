from kandinsky import *
from ion import *
import turtle
import math

# Define the pages
MENU_PAGE = 0
MATHS_PAGE = 1
PHYSIQUE_PAGE = 2
I2D_PAGE = 3
TRIGO_PAGE = 4
RAD_TO_DEG_PAGE = 5
DEG_TO_RAD_PAGE = 6

def menu():
    current_page = MENU_PAGE
    subject = ["MATHS", "PHYSIQUE CHIME", "I2D"]

    fill_rect(0, 0, 320, 222, color(255, 255, 255))

    for i in range(3):
        draw_string(subject[i], 10, 10 + 40 * i)
    
    # If the user is on the menu and inputs
    while True:
        if current_page == MENU_PAGE:
            if keydown(KEY_ONE):
                current_page = MATHS_PAGE
            elif keydown(KEY_TWO):
                current_page = PHYSIQUE_PAGE
            elif keydown(KEY_THREE): 
                current_page = I2D_PAGE
        elif current_page == MATHS_PAGE:
            maths()
            if keydown(KEY_SHIFT):
                current_page = MENU_PAGE
                menu()
        elif current_page == PHYSIQUE_PAGE:
            physique()
            if keydown(KEY_SHIFT):
                current_page = MENU_PAGE
                menu()
        elif current_page == I2D_PAGE:
            i2d()
            if keydown(KEY_SHIFT):
                current_page = MENU_PAGE
                menu()

def maths():
    chapter = ["1. Trigonometrie", "2. Nombre Complexe", "3. Derivation", "4. Produit Scalaire", "5. Primitive"]
    current_page = MATHS_PAGE
    
    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    
    # Draw each chapter
    for i in range(5):
        draw_string(chapter[i], 10, 10 + 40 * i)
    
    # If the user is on the menu and inputs
    while True:
        if current_page == MATHS_PAGE:
            if keydown(KEY_ONE):
                current_page = TRIGO_PAGE
                trigo()
            elif keydown(KEY_SHIFT):
                current_page = MENU_PAGE
                menu()
        elif current_page == TRIGO_PAGE:
            if keydown(KEY_NINE):
                current_page = MATHS_PAGE
                maths()
            elif keydown(KEY_SHIFT):
                current_page = MENU_PAGE
                menu()

def physique():
    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    
    # Make 3 string blank and one "Soon..."
    draw_string("Soon...            ", 10, 10)
    draw_string("Soon...            ", 10, 50)
    draw_string("Soon...            ", 10, 90)


def i2d():
    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    
    # Make 3 string blank and one "Soon..."
    draw_string("Soon...            ", 10, 10)
    draw_string("Soon...            ", 10, 50)
    draw_string("Soon...            ", 10, 90)

def trigo():
    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    current_page = TRIGO_PAGE
    
    tools = ["1. Radians => Degres", "2. Degres => Radians", "9. Retour              ", "SHIFT. Menu                         "]
    for i in range(5):
        draw_string(tools[i], 10, 10 + 40 * i)

    while True:
        if current_page == TRIGO_PAGE:
            if keydown(KEY_ONE):
                current_page = RAD_TO_DEG_PAGE
                rad_to_deg()
            elif keydown(KEY_TWO):
                current_page = DEG_TO_RAD_PAGE
                deg_to_rad()
            elif keydown(KEY_NINE):
                current_page = MATHS_PAGE
                maths()
            elif keydown(KEY_SHIFT):
                current_page = MENU_PAGE
                menu()


def rad_to_deg():

    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    draw_string("Radians => Degres", 10, 10)
    draw_string("Entrez la valeur en radians", 10, 50)
    draw_string("SHIFT. Retour", 10, 90)

    while True:
        if keydown(KEY_SHIFT):
            trigo()
        elif keydown(KEY_EXE):
            rad = input("Radians: ")
            deg = math.degrees(rad)
            draw_string(deg, 10, 130)
            draw_string("SHIFT. Retour", 10, 90)

def deg_to_rad():
    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    draw_string("Degres => Radians", 10, 10)
    draw_string("Entrez la valeur en degres", 10, 50)
    draw_string("SHIFT. Retour", 10, 90)

    while True:
        if keydown(KEY_SHIFT):
            trigo()
        elif keydown(KEY_EXE):
            deg = input("Degres: ")
            rad = math.radians(deg)
            draw_string(rad, 10, 130)
            draw_string("SHIFT. Retour", 10, 90)


menu()
