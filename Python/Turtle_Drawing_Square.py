import turtle

#setting up the window and its attributes
window = turtle.Screen()
window.bgcolor("purple")

#create turtle and its atrributes
drake = turtle.Turtle()
drake.shape("turtle")
drake.color("green")
drake.pensize(25)

for side in range(4):
    drake.forward(100)
    drake.left(90)

#exit the window when you click
window.exitonclick()