import turtle

def draw_rectangles():
    '''draws four rectangles in the approximate shape of a windmill'''
    for direction in (90, 0, 270, 180):
        john.seth(direction)
        for side in (300, 100, 300, 100):
            john.forward(side)
            john.left(90)
screen = turtle.Screen()
john = turtle.Turtle()

draw_rectangles()