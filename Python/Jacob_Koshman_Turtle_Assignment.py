import turtle
# import microbit
import random
import time
import PySimpleGUI as psg

##########################################################################################
#Jacob Koshman
#Computer Science 20
#April 21, 2024
#
#Turtles
#Purpose: To control a python turtle with input from either a keyboard or from a microbit
##########################################################################################

#creating the screen and the turtle with attributes
screen = turtle.Screen()
john = turtle.Turtle()
john.shape("turtle")
john.speed(0)

#making a scrollable popup window to show the user what the keybinds are
def keybinds_popup():
    file=open("turtlecontrolkeyboard.txt")
    text=file.read()
    psg.popup_scrolled(text, title="Turtle Keybinds", font=("Helvetica", 16), size=(50, 10))
    
#making the turtle do a flip
def do_a_flip():
    john.penup()
    john.speed(1)
    john.left(45)
    john.forward(25)
    john.left(270)
    time.sleep(0.5)
    john.forward(25)
    john.speed(0)
    john.left(45)
    john.pendown()

#making the turtle visible
def show_john():
    john.showturtle()

#hiding the turtle
def hide_john():
    john.hideturtle()
    
#opening and reading the turtle color text file
with open("turtlecolors.txt", "r", encoding="UTF-8") as file: 
            color = file.read() 
            colors = list(map(str, color.split()))

#making the turtle "jump"
def jump():
    john.penup()
    john.forward(100)
    john.pendown()
#turning towards and moving north
def north():
    john.setheading(90)
    john.forward(100)

#turning towards and moving south
def south():
    john.setheading(270)
    john.forward(100)

#turning towards and moving west
def west():
    john.setheading(180)
    john.forward(100)

#turning towards and moving east
def east():
    john.setheading(0)
    john.forward(100)

#turning the turtle without moving   
def turn():
    john.left(90)
    
#changing the background color using user input
def change_background_color():
    bg_color = screen.textinput("Background Color", "What color do you want the background to be? ")
    screen.bgcolor(str(bg_color))
    screen.listen()
    
#changing the turtles color to red   
def change_color_red():
    john.color("red")
    
#changing the turtles color to orange    
def change_color_orange():
    john.color("orange")
    
#changing the turtles color to yellow   
def change_color_yellow():
    john.color("yellow")
    
#changing the turtles color to green  
def change_color_green():
    john.color("green")
    
#changing the turtles color to blue 
def change_color_blue():
    john.color("blue")
    
#changing the turtles color to indigo       
def change_color_indigo():
    john.color("indigo")

#changing the turtles color to violet
def change_color_violet():
    john.color("violet")
    
#drawing a star  
def draw_star():
    for side in range(5):
        john.forward(100)
        john.left(144)
        
#drawing a circle       
def draw_circle():
    john.circle(50)

#drawing a triangle
def draw_triangle():
    for side in range(3):
        john.forward(100)
        john.left(120)    

#drawing a square
def draw_square():
    for side in range(4):
        john.forward(100)
        john.left(90)
        
#drawing a pentagon        
def draw_pentagon():
    for side in range(5):
        john.forward(100)
        john.left(72)
        
#drawing a hexagon       
def draw_hexagon():
    for side in range(6):
        john.forward(100)
        john.left(60)
        
#drawing a septagon        
def draw_septagon():
    for side in range(7):
        john.forward(100)
        john.left(360/7)
        
#drawing a octagon       
def draw_octagon():
    for side in range(8):
        john.forward(100)
        john.left(45)



#asking the user if they are using a keyboard or a microbit to control the turtle 
# controller_type = screen.textinput("Controller Type", "Are you using a keyboard or a microbit to control this turtle? ")    
controller_type = "keyboard"

#if the user is using a keyboard to control the turtle
if controller_type == "keyboard":
    keybinds_popup()
    screen.listen()
    screen.onkey(do_a_flip, "f")
    screen.onkey(show_john, "j")
    screen.onkey(hide_john, "h")
    screen.onkey(jump, "space")
    screen.onkey(turn, "e")
    screen.onkey(north, "w")
    screen.onkey(south, "s")
    screen.onkey(east, "d")
    screen.onkey(west, "a")
    screen.onkey(change_background_color, "q")
    screen.onkey(change_color_red, "r")
    screen.onkey(change_color_orange, "o")
    screen.onkey(change_color_yellow, "y")
    screen.onkey(change_color_green, "g")
    screen.onkey(change_color_blue, "b")
    screen.onkey(change_color_indigo, "i")
    screen.onkey(change_color_violet, "v")
    screen.onkey(draw_circle, "0")
    screen.onkey(draw_triangle, "1")
    screen.onkey(draw_square, "2")
    screen.onkey(draw_pentagon, "3")
    screen.onkey(draw_hexagon, "4")
    screen.onkey(draw_septagon, "5")
    screen.onkey(draw_octagon, "6")
    screen.onkey(draw_star, "7")

#if the user is using a microbit to control the turtle
# elif controller_type == "microbit":
#     x = microbit.accelerometer.get_x()
#     y = microbit.accelerometer.get_y()
#     if x > 250:
#         east()
#     elif x < -250:
#         west()
#     elif y > 250:
#         north()
#     elif y < -250:
#         south()
#     elif microbit.button_a.was_pressed():
#         john.color(str(random.choice(colors)))
#     elif microbit.button_b.was_pressed():
#         draw_shape = screen.textinput("Shape Drawing", "What shape would you like to draw, circle, triangle, square, pentagon, hexagon, septagon, octagon, or star? ")
#         if draw_shape == "circle":
#             draw_circle()
#         elif draw_shape == "triangle":
#             draw_triangle()
#         elif draw_shape == "square":
#             draw_square()
#         elif draw_shape == "pentagon":
#             draw_pentagon()
#         elif draw_shape == "hexagon":
#             draw_hexagon()
#         elif draw_shape == "septagon":
#             draw_septagon()
#         elif draw_shape == "octagon":
#             draw_octagon()
#         elif draw_shape == "star":
#             draw_star()
    