import turtle

screen = turtle.Screen()
sheldon = turtle.Turtle()

side_length = screen.textinput("screen", "How long should the sides be? ")
shape_type = screen.textinput("screen", "What shape do you want? ")

if shape_type == "triangle":
    for side in range(3):
        sheldon.forward(int(side_length))
        sheldon.left(120)
elif shape_type == "square":
    for side in range(4):
        sheldon.forward(int(side_length))
        sheldon.left(90)
elif shape_type == "pentagon":
    for side in range(6):
        sheldon.forward(int(side_length))
        sheldon.left(60)