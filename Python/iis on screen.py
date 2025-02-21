import turtle
import random

STEP_SIZE = 5

def is_on_screen(window, the_turtle):
    '''returns true if the_turtle is on the screen returns false if otherwise'''
    right_side = window.window_width() / 2
    left_side = -window.window_width() / 2
    top_side = window.window_height() / 2
    bottom_side = -window.window_height() / 2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    return x > left_side and x < right_side and y < top_side and y > bottom_side

screen = turtle.Screen()
john = turtle.Turtle()
john.pensize(3)
john.shape("turtle")
john.speed(0)

while is_on_screen(screen, john):
    choice = random.randrange(1, 4)
    if choice == 1:
        john.left(90)
    elif choice == 2:
        john.right(90)
    john.forward(STEP_SIZE)
print("i am off the screen now")