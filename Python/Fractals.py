import turtle

def draw_string(some_turtle, instructions, distance, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

def apply_rules(letter):
    '''apply rules to a single letter and return the result'''
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    else:
        return letter
    
def process_string(some_string):
    '''Apply the rules to every letter in a string then return the results'''
    transformed_string = ""
    for letter in some_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(axiom, number_of_iterations):
    '''start with the axiom and apply the rules to the string a given number of times'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string

canvas = turtle.Screen()
joe = turtle.Turtle()
joe.speed(0)
canvas.tracer(0)
joe.penup()
joe.goto(-300, -400)
joe.pendown()


instructions = create_l_system("FXF--FF--FF", 15)
draw_string(joe, instructions, 0.1, 60)