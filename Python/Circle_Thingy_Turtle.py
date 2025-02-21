import turtle

#creating the screen and the bob with attributes
screen = turtle.Screen()
john = turtle.Turtle()
john.color("blue")
john.pensize(10)
john.speed("fastest")
john.penup()
john.left(90)
john.backward(450)
john.pendown()
john.right(90)
bob = turtle.Turtle()
bob.color("red")
bob.pensize(1)
bob.speed("fastest")

#creating the shape and its attributes
side_thing = int(screen.textinput("screen", "How many sides? "))
side_length = int(screen.textinput("screen", "How long should the sides be? "))
    
for shape in range(360):
    for side in range(side_thing):
        john.forward(side_length)
        john.left(360/side_thing)
    john.penup()
    john.forward(8)
    john.left(1)
    john.pendown()
bob.penup()
bob.left(90)
bob.backward(450 - side_length)
bob.right(90)
bob.pendown()
for shape in range(360):
    for side in range(side_thing):
        bob.forward(10)
        bob.left((360/side_thing)*2)
    bob.penup()
    bob.forward(8)
    bob.left(1)
    bob.pendown()
