from turtle import *

screen = Screen()

def draw_2_squares():
    for side_length in (300, 200):
        for side in range(4):
            forward(side_length)
            left(90)
        forward(50)
        penup()
        setheading(90)
        forward(50)
        pendown()
        setheading(0)

def draw_squares():
    for direction in (0, 22.5, 45, 67.5):
        setheading(direction)
        for side in range(4):
            forward(300)
            left(90)
        penup()
        forward(150)
        setheading(270)
        forward(75)
        pendown()

draw_squares()
        
        