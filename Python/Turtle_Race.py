import turtle
import random

STARTING_X_COORDINATE = -250
VERTICAL_BUFFER = 50
REF_X_VALUE = 250

screen = turtle.Screen()
john = turtle.Turtle()
bob = turtle.Turtle()

john.shape("turtle")
bob.shape("turtle")

john.color("orange")
bob.color("green")

john.penup()
bob.penup()
john.goto(STARTING_X_COORDINATE, -VERTICAL_BUFFER)
bob.goto(STARTING_X_COORDINATE, VERTICAL_BUFFER)
john.pendown()
bob.pendown()

ref = turtle.Turtle()
ref.penup()
ref.pensize(5)
ref.goto(REF_X_VALUE, (VERTICAL_BUFFER*2))
ref.pendown()
ref.goto(REF_X_VALUE, (VERTICAL_BUFFER*-2))
ref.hideturtle()

    
while bob.xcor() < REF_X_VALUE and john.xcor() < REF_X_VALUE:
    john.forward(random.randrange(0, 11))
    bob.forward(random.randrange(0, 11))
    bob.speed(random.randrange(0, 11))
    john.speed(random.randrange(0, 11))
    
if bob.xcor() > john.xcor():
    bob.write("BOB IS THE WINNER!!!!!!!!!!!!! ", move=False, align="right", font=("Arial Bold", 20))
elif john.xcor() > bob.xcor():
    john.write("JOHN IS THE WINNER!!!!!!!!!!!!! ", move=False, align="right", font=("Arial Bold", 20))
else:
    ref.goto(REF_X_VALUE, (VERTICAL_BUFFER*2))
    ref.write("ITS A TIE!!!!!!!!!!!! ", move=False, align="right", font=("Arial Bold", 20))