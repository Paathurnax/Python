import turtle

screen = turtle.Screen()
john = turtle.Turtle()
def draw_hollow_c(some_turtle, longest_side_length, width):
    for i in [longest_side_length, -longest_side_length, width, -longest_side_length + width, -longest_side_length + (width*2), -longest_side_length + width, width, -longest_side_length]:
        some_turtle.right(90)
        some_turtle.forward(i)
        
draw_hollow_c(john, 200, 40)
