import turtle

def draw_cross(some_turtle, side_length):
    for shape in range(4):
        some_turtle.forward(side_length)
        some_turtle.right(90)
        some_turtle.forward(side_length)
        some_turtle.right(90)
        some_turtle.forward(side_length)
        some_turtle.left(90)
        
screen = turtle.Screen()
john = turtle.Turtle()

draw_cross(john, 100)