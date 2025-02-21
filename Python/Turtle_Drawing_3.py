import turtle

#creating the screen and the turtles with attributes
screen = turtle.Screen()
bob = turtle.Turtle()
bob.color("red")
bob.pensize(10)

#setup another turtle
john = turtle.Turtle()
john.color("blue")
john.pensize(10)

#making a third turtle
bill = turtle.Turtle()
bill.color("green")
bill.pensize(10)

#creating the shapes and their attributes
for side in range(5):
    bob.forward(100)
    bob.left(72)
john.penup()
john.backward(300)
john.pendown()
for side in range(3):
    john.forward(100)
    john.left(120)
bill.penup()
bill.forward(100)
bill.left(90)
bill.forward(200)
bill.pendown()
for side in range(4):
    bill.forward(100)
    bill.left(90)