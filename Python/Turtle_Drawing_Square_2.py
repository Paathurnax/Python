import turtle

#making the screen and asking the user what color they want the screen to be
screen = turtle.Screen()
screen_color = screen.textinput("screen", "What color do you want the screen to be? ")
screen.bgcolor(str(screen_color))

#creating the turtle and asking the user what color they want the turtle to be
john = turtle.Turtle()
john.shape("turtle")
line_thickness = screen.textinput("screen", "How thick do you want the lines to be? (should be a number) ")
turtle_color = screen.textinput("screen", "What color do you want the turtle to be? ")
john.pensize(int(line_thickness))
john.color(str(turtle_color))


#drawing a square with instructions given by the user
side_length = screen.textinput("screen", "How long do you want the sides to be? (should be a number) ")
for side in range(4):
    john.forward(int(side_length))
    john.left(90)
