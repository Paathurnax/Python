import turtle

screen = turtle.Screen()
john = turtle.Turtle()

def draw_squares(starting_angle, amount_of_squares):
    for shape in range(amount_of_squares):
        john.setheading(starting_angle)
        john.forward(75)
        for side in range(3):
            john.left(90)
            john.forward(150)
        john.goto(0, 0)
        starting_angle = starting_angle + 72
        
draw_squares(18, 5)
        