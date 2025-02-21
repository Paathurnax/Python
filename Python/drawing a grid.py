import turtle

screen = turtle.Screen()
john = turtle.Turtle()
screen.tracer(10)
def draw_grid():
    john.setheading(90)
    john.penup()
    john.goto(-750, -500)
    john.pendown()
    for line in range(30):
        for length in (1000, -1000):
            john.setheading(90)
            john.forward(length)
            john.setheading(0)
            john.forward(30)
    john.goto(-750, -500)       
    for horizon in range(20):
        for long in (1500, -1500):
            john.setheading(0)
            john.forward(long)
            john.setheading(90)
            john.forward(30)
