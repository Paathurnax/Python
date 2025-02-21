import turtle

PIXEL_SIDE_LENGTH = 25
CURSORSIZE = 15

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
    "wwrrbrrbrwwww",
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
bob = turtle.Turtle()
bob.hideturtle()
bob.shape("square")
bob.shapesize(PIXEL_SIDE_LENGTH/CURSORSIZE)
bob.penup()
x_initial = -LENGTH/2 *PIXEL_SIDE_LENGTH
y_initial = WIDTH/2 *PIXEL_SIDE_LENGTH
for i, row in enumerate(PIXELS):                         
    bob.setposition(x_initial, y_initial - i*PIXEL_SIDE_LENGTH)
    print(i, row)    
#     for pixel in row:
#         bob.color(COLORS[pixel])
#         bob.stamp()
#         bob.forward(PIXEL_SIDE_LENGTH)
        
