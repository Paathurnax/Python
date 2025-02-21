import turtle

screen = turtle.Screen()
bob = turtle.Turtle()

for side in range(12):
    bob.penup()
    bob.forward(100)
    bob.pendown()
    bob.forward(50)
    bob.penup()
    bob.forward(20)
    bob.clone()
    bob.backward(170)
    bob.left(30)