import turtle

def draw_cross_thing(side_length, some_turtle):
    for direction in [270, 180, 90, 0]:
        for b in range(4):
            for c in range(3):
                some_turtle.forward(side_length)
                some_turtle.left(90)
            some_turtle.left(180)
        some_turtle.setheading(direction)
        
john = turtle.Turtle()
screen = turtle.Screen()

draw_cross_thing(50, john)