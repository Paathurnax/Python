import turtle

def draw_shape():
    '''draws 6 triangles in the form of a hexagon'''
    for shape in range(6):
        for side in range(3):
            john.forward(200)
            john.left(120)
        john.left(60)
        


screen = turtle.Screen()
john = turtle.Turtle()
john.pensize(5)

draw_shape()