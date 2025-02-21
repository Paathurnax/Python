import turtle

#Drawing a Fire Flower
    elif character == "Fire Flower":
        COLORS = {
            'r': "OrangeRed",
            'o': "orange",
            'y': "gold",
            'w': "white",
            'b': "black",
            'g': "green1",
        }
        PIXELS = [
            "wwwwbbbbbbbbwwww",
            "wwbbrrrrrrrrbbww",
            "wbrrroooooorrrbw",
            "brrooybyybyoorrb",
            "brroywbwwbwyorrb",
            "brrooybyybyoorrb",
            "wbrrroooooorrrbw",
            "wwbbrrrrrrrrbbww",
            "wwwwbbbbbbbbwwww",
            "wbbwwwbggbwwwbbw",
            "bggbbwbggbwbbggb",
            "bggggbbggbbggggb",
            "bgggggbggbgggggb",
            "wbggggbggbggggbw",
            "wwbbggggggggbbww",
            "wwwwbbbbbbbbwwww",
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
            
            for pixel in row:
                bob.color(COLORS[pixel])
                bob.stamp()
                bob.forward(PIXEL_SIDE_LENGTH)                
    