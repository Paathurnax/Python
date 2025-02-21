import turtle

def draw_string(some_turtle, instructions, distance, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

canvas = turtle.Screen()
joe = turtle.Turtle()

instructions = "F++F++F++F"
draw_string(joe, instructions, 100, 45)


