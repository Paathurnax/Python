import turtle

PIXEL_SIDE_LENGTH = 30
CURSORSIZE = 20
COLORS = {
    'b': "blue",
    'y': "yellow",
    'r': "red",
    'B': "black",
    'w': "white",
    's': "sandy brown",
    'R': "brown",
}
PIXELS = [
    "wwwrrrrrrwwww",
    "wwrrrrrrrrrrw",
    "wwRRRsssBswww",
    "wRsRssssBsssw",
    "wRsRRssssBsss",
    "wRRsssssBBBBw",
    "wwwssssssssww",
    "wwrrbrrrrwwww",
    "wrrrbrrbrrrww",
    "rrrrbbbbrrrrw",
    "ssrbybbybrssw",
    "sssbbbbbbsssw",
    "wwbbbwwbbbwww",
    "wRRRwwwwRRRww",
    "RRRRwwwwRRRRw",
]
LENGTH, WIDTH = len(PIXELS[0]), len(PIXELS)
screen = turtle.Screen()
john = turtle.Turtle()
john.hideturtle()
john.shape("square")
john.shapesize(PIXEL_SIDE_LENGTH/CURSORSIZE)
john.penup()
x_initial = -LENGTH/2 *PIXEL_SIDE_LENGTH
y_initial = WIDTH/2 *PIXEL_SIDE_LENGTH
for i, row in enumerate(PIXELS):
    john.setposition(x_initial, y_initial - i*PIXEL_SIDE_LENGTH)
    
    for pixel in row:
        john.color(COLORS[pixel])
        john.stamp()
        john.forward(PIXEL_SIDE_LENGTH)
screen.tracer(10)