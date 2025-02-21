import turtle

screen = turtle.Screen()
sheldon = turtle.Turtle()
screen_color = screen.textinput("screen", "What color should the background be? ")
pen_size = screen.textinput("screen", "How thick should the lines be? ")
turtle_color = screen.textinput("screen", "What color should the turtle be? ")
side_length = screen.textinput("screen", "How long should the sides be? ")

screen.bgcolor(screen_color)
sheldon.pensize(int(pen_size))
sheldon.color(turtle_color)
sheldon.left(36)
for side in range(5):
    sheldon.forward(int(side_length))
    sheldon.left(144)