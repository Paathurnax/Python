import turtle
import time
import PySimpleGUI as psg

##########################################################################################
#Jacob Koshman
#Computer Science 20
#April 21, 2024
#
#Turtles/Loops Assignment
#Purpose: To draw pixel art or to control a turtle with a keyboard
##########################################################################################

def keybinds_popup():
    '''opens a file, reads it, then makes the text inside the file popup on the screen'''
    file=open("turtlecontrolkeyboard.txt", "r", encoding="UTF-8")
    text=file.read()
    psg.popup_scrolled(text, title="Turtle Keybinds", font=("Helvetica", 16), size=(50, 20))
    screen.listen()
    
def do_a_flip():
    '''makes the turtle do a "flip"'''
    john.penup()
    john.speed(1)
    john.left(45)
    john.forward(25)
    john.left(270)
    time.sleep(0.5)
    john.forward(25)
    john.speed(0)
    john.left(45)
    john.pendown()

def show_john():
    '''makes the turtle visible'''
    john.showturtle()

def hide_john():
    '''hides the turtle'''
    john.hideturtle()

def jump():
    '''makes the turtle "jump"'''
    john.penup()
    john.forward(100)
    john.pendown()

def north():
    '''turns the turtle towards and makes it move 100 pixels north'''
    john.setheading(90)
    john.forward(100)

def south():
    '''turns the turtle towards and makes it move 100 pixels south'''
    john.setheading(270)
    john.forward(100)

def west():
    '''turns the turtle towards and makes it move 100 pixels west''' 
    john.setheading(180)
    john.forward(100)

def east():
    '''turns the turtle towards and makes it move east'''
    john.setheading(0)
    john.forward(100)
   
def turn():
    '''turns the turtle 90 degrees left without moving'''
    john.left(90)
    
def change_background_color():
    '''changes the background color based on user input'''
    bg_color = psg.popup_get_text("Background Color", "What color do you want the background to be? ")
    screen.bgcolor(str(bg_color))
    screen.listen()
      
def change_color_red():
    '''changes the turtles color to red'''
    john.color("red")
       
def change_color_orange():
    '''changes the turtles color to orange'''
    john.color("orange")
      
def change_color_yellow():
    '''changes the turtles color to yellow'''
    john.color("yellow")
      
def change_color_green():
    '''changes the turtles color to green'''
    john.color("green")
    
def change_color_blue():
    '''changes the turtles color to blue'''
    john.color("blue")
          
def change_color_indigo():
    '''chnages the turtle to indigo'''
    john.color("indigo")

def change_color_violet():
    '''changes the turtles color to violet'''
    john.color("violet")
      
def draw_star():
    '''draws a star using a for loop'''
    for side in range(5):
        john.forward(100)
        john.left(144)
               
def draw_circle():
    '''draws a circle'''
    john.circle(50)

def draw_triangle():
    '''draws a triangle using a for loop'''
    for side in range(3):
        john.forward(100)
        john.left(120)    

def draw_square():
    '''draws a square using a for loop'''
    for side in range(4):
        john.forward(100)
        john.left(90)
              
def draw_pentagon():
    '''draws a pentagon using a for loop'''
    for side in range(5):
        john.forward(100)
        john.left(72)
               
def draw_hexagon():
    '''draws a hexagon using a for loop'''
    for side in range(6):
        john.forward(100)
        john.left(60)
                
def draw_heptagon():
    '''draws a heptagon using a for loop'''
    for side in range(7):
        john.forward(100)
        john.left(360/7)
               
def draw_octagon():
    '''draws an octagon using a for loop'''
    for side in range(8):
        john.forward(100)
        john.left(45)

def stop():
    '''opens a window to ask the user if the are sure they want to exit before exiting the window'''
    if psg.popup_yes_no("Are you sure you want to exit? ") == "Yes":
        exit()
    else:
        screen.listen()
        
#Defining Pixel Art Variables
PIXEL_SIDE_LENGTH = 25
CURSORSIZE = 15

#Creating Both The Screen and The Turtle With Attributes
screen = turtle.Screen()
john = turtle.Turtle()
john.shape("turtle")
john.speed(0)
screen.tracer()

#Asking The User if They Want to Either Control The Turtle Manually or if They Want to Create Pixel Art 
pixel_art = psg.popup_get_text("Do you want the turtle to make pixel art or do you want to control the turtle using your keyboard? (pixel art or keyboard) ", "Options")

#The User Wants to Control The Turtle Manually
if pixel_art == "keyboard":
    john.showturtle()
    keybinds_popup()
    screen.listen()
    screen.onkey(stop, "Escape")
    screen.onkey(do_a_flip, "f")
    screen.onkey(show_john, "j")
    screen.onkey(hide_john, "h")
    screen.onkey(jump, "space")
    screen.onkey(turn, "e")
    screen.onkey(north, "w")
    screen.onkey(south, "s")
    screen.onkey(east, "d")
    screen.onkey(west, "a")
    screen.onkey(change_background_color, "q")
    screen.onkey(change_color_red, "r")
    screen.onkey(change_color_orange, "o")
    screen.onkey(change_color_yellow, "y")
    screen.onkey(change_color_green, "g")
    screen.onkey(change_color_blue, "b")
    screen.onkey(change_color_indigo, "i")
    screen.onkey(change_color_violet, "v")
    screen.onkey(draw_circle, "0")
    screen.onkey(draw_triangle, "1")
    screen.onkey(draw_square, "2")
    screen.onkey(draw_pentagon, "3")
    screen.onkey(draw_hexagon, "4")
    screen.onkey(draw_heptagon, "5")
    screen.onkey(draw_octagon, "6")
    screen.onkey(draw_star, "7")

#The User Wants to Create Pixel Art 
elif pixel_art == "pixel art":
    character = screen.textinput("Character", "Which character would you like to draw, Mario, Luigi, Peach, Bowser, Yoshi, a Goomba, Toad, or Wario? ")
    john.hideturtle()
    
    #if you want to use tracer only use it for pixel art not for the manual controls
    #screen.tracer(10)
    
    #Drawing Mario
    if character == "Mario":
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
            
            for pixel in row:
                bob.color(COLORS[pixel])
                bob.stamp()
                bob.forward(PIXEL_SIDE_LENGTH)
    
    #Drawing Luigi
    elif character == "Luigi":
        COLORS = {
            'b': "blue",
            'y': "yellow",
            'g': "green",
            'B': "black",
            'w': "white",
            's': "sandy brown",
            'R': "brown",
        }
        PIXELS = [
            "wwwggggggwwww",
            "wwggggggggggw",
            "wwRRRsssBswww",
            "wRsRssssBsssw",
            "wRsRRssssBsss",
            "wRRsssssBBBBw",
            "wwwssssssssww",
            "wwggbggggwwww",
            "wgggbggbgggww",
            "ggggbbbbggggw",
            "ssgbybbybgssw",
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
            
            for pixel in row:
                bob.color(COLORS[pixel])
                bob.stamp()
                bob.forward(PIXEL_SIDE_LENGTH)
    
    #Drawing Peach
    elif character == "Peach":
        COLORS = {
            'b': "blue",
            'y': "yellow",
            'v': "VioletRed",
            's': "wheat1",
            'w': "white",
            'h': "HotPink",
            'g': "yellow2",
            'p': "WhiteSmoke",
            'l': "LightBlue",
        }
        PIXELS = [
            "wwwwwgwgwgwwww",
            "wwwwwlgvglwwww",
            "wwwwyyyyyywwww",
            "wwwyyyyyyyywww",
            "wwwyyyyyysyyww",
            "wyyyyyysbsyyww",
            "wwyyysyslsswww",
            "wwwyybysssswww",
            "wwyyyysssswwww",
            "wyyyyvvvylhwww",
            "wwyyhhhhhhhhww",
            "wwwysshhhhhsww",
            "wwwppvvvvvvppw",
            "wwppvvvvhhvvpp",
            "wwwwvvhhhhhvww",
            "wwwwhhhhhhhhww",
            "wwwhhhhhhhhhhw",
            "wwvvvvvvvvvvvw",
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
    
    #Drawing Bowser
    elif character == "Bowser":
        COLORS = {
            'r': "red",
            'm': "maroon",
            'd': "DarkGreen",
            'G': "Gray",
            'g': "green",
            'b': "black",
            'y': "gold1",
            'Y': "goldenrod2",
            'w': "white",
            'p': "WhiteSmoke",
            'R': "LightGray",
            'B': "LightBlue", 
        }
        PIXELS = [
            "wwwwwwwwwwbmrrrrmbwwwwwwwwww",
            "wwwbbbwwwrrrggggrrrwwwbbbwww",
            "wwwbypbbbdprrggrrpdbbbpybwww",
            "wwwwbyppbgppbddbppgbppybwwww",
            "wwwwwbyybggyyyyyyggbyybwwwww",
            "wwwwwwbbYygybyybygyYbbwwwwww",
            "wwwwwwbYyyyyyyyyyyyyYbwwwwww",
            "wwwwwwbYyyYpYYYYpYyyYbwwwwww",
            "wwwbwwwbYpbbbbbbbbpYbwwwbwww",
            "wwbwbwbbYYbbbbbbbbYYbbwbwbww",
            "wwwbdbRRbybbbbbbbbybRRbdbwww",
            "wwwbbbRRbybbmmmmbbybRRbbbwww",
            "wwbyybbRbypmrrrrmpybRbbyybww",
            "wbyyyybRbYymprrpmyYbRbyyyybw",
            "bYyyyyybRbyypmmpyybRbyyyyyYb",
            "bYyyyyGGbbYyyyyyyYbbGGyyyyYb",
            "bYYYyGGyyybYbbbbYbyyyGGyYYYb",
            "wbYYGGYyyyybYbbYbyyyyYGGYYbw",
            "wwbYGGYyyyybbRRbbyyyyYGGYbww",
            "wwwbbGYYYYYbRbbRbYYYYYGbbwww",
            "wwwwbbbYYbbRbbbbRbbYYbbbwwww",
            "wbbbYYybbypbRbbRbpybbyYYbbbw",
            "bRRYYYbypYYYbbbbYYYpybYYYRRb",
            "bGGYYYbYYYYybbbbyYYYYbYYYGGb",
            "bbbbbbbpYyyyybbyyyyYpbbbbbbb",
            "bbGGGGbYYYyyYbbYyyYYYbGGGGbb",
            "bbRRRRbbBBBBBbbBBBBBbbRRRRbb",
            "bbGGGGbRBYYYYbbYYYYBRbGGGGbb",
            "wbbbbbbRBbYYbRRbYYbBRbbbbbbw",
            "wbbbbbbwRRRRRRRRRRRRwbbbbbbw",
            "wwbbbbwwwbbbbbbbbbbwwwbbbbww",
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
     
    #Drawing King Boo
    elif character == "King Boo":
        COLORS = {
            's': "WhiteSmoke",
            'b': "black",
            'g': "DarkGray",
            'r': "red",
            'w': "white",
            'd': "gray",
            'p': "HotPink",
            'y': "yellow",
            'a': "DarkGoldenrod2",
            'm': "maroon",
        }
        PIXELS = [
            "wwwwwwwwwwwwbbwbbwbbwwwwwwwwwwww",
            "wwwwwwwwwwwwbybyybybwwwwwwwwwwww",
            "wwwwwwwwwwwwbyayyaybwwwwwwwwwwww",
            "wwwwwwwwwwwwbabayrabwwwwwwwwwwww",
            "wwwwwwwwwwbbbssssssbbbwwwwwwwwww",
            "wwwwwwwwbbssssssssssssbbwwwwwwww",
            "wwwwwwwbssssssssssssssssbwwwwwww",
            "wwwwwwbssssssssssssssssssbwwwwww",
            "wwwwwbgsssssssssssssssssssbwwwww",
            "wwwwwbgsssssssssssssssssssbwwwww",
            "wwwwbggssssssssbdgssbbgssbsbwwww",
            "wwwwbggssssssssgbbbbggbbbssbwwww",
            "wwwwbggsssssssssggddssddsssbwwww",
            "wwwbsggsssssssssssdssssdssssbwww",
            "wwwbsgggssssssssssddssddssssbwww",
            "wwwbsgggssssssssssbbssbbssssbwww",
            "wwwbsggggssssssbssssssssssssbwww",
            "wwwbsgbsggsssssmbbssssssbmsgbwww",
            "wwwbbbssssggsssmggbbbbbbgmgbsbww",
            "bbbsbsssssggggsmgsmgmgmgsggbgsbw",
            "bssbssssssggggggmsmmmmmmsggbggsb",
            "bggbssssbbggggggrppprmmmggbgggsb",
            "wbsgbbbbgggggggggpppprmgggbbbbbw",
            "wwbbggbsssggggggggpppggggbwwwwww",
            "wwwwbbbbssssggggggggggggbwwwwwww",
            "wwwwwwwwbbsssssgggggggbbwwwwwwww",
            "wwwwwwwwwwbbbwwwwwwbbbwwwwwwwwww",
            "wwwwwwwwwwwwwbbbbbbwwwwwwwwwwwww",
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
        
    #Drawing a Goomba
    elif character == "Goomba":
        COLORS = {
            'w': "white",
            'b': "brown",
            'l': "black",
            'm': "WhiteSmoke",
            's': "sandy brown",
        }
        PIXELS = [
            "wwwwwwbbbbwwwwww",
            "wwwwwbbbbbbwwwww",
            "wwwwbbbbbbbbwwww",
            "wwwbbbbbbbbbbwww",
            "wwbllbbbbbbllbww",
            "wbbbmlbbbblmbbbw",
            "wbbbmllllllmbbbw",
            "bbbbmlmbbmlmbbbb",
            "bbbbmmmbbmmmbbbb",
            "bbbbbbbbbbbbbbbb",
            "wbbbbssssssbbbbw",
            "wwwwsssssssswwww",
            "wwllssssssssllww",
            "wlllllsssslllllw",
            "wllllllwwllllllw",
            "wwlllllwwlllllww",
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
     
    #Drawing Yoshi
    elif character == "Yoshi":       
        COLORS = {
            'b': "blue",
            'l': "LightBlue",
            'B': "black",
            'o': "orange",
            'O': "DarkOrange",
            'g': "SpringGreen",
            'G': "LimeGreen",
            'w': "white",
        }
        PIXELS = [
            "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
            "blblblblblblblBBbBBlblblblblb",
            "lbbblbbblbbblBGgBGgBlblblblbl",
            "lblblblblblbBGGwwwwgBlblblblb",
            "bbbbbbbbbBBBBGwwBwBwBbbbbbbbb",
            "blblblblBOooBwwwBwBwBlblblblb",
            "lbbblbbbBOOBBwwwwwwwBBBblbbbl",
            "blblblblBBBggGwwwGwBgggBblblb",
            "bbbbbblBoBGgwgGGGgGggwwgBbbbb",
            "blblblBOOBGggwwwgGgggBwBBlbbl",
            "lbbblbBOOBGGwwwwGGgggggggBbbb",
            "blblblbBBBGGwwwwGGGggggggBlbl",
            "bblbbblbBBGGwwwwBGGGGgggGBblb",
            "blblblblBOBGGwwBBGGGGGGGGBlbl",
            "lllblblblBBBGGwwBGGGGGGGBlblb",
            "blblblblbBOBGGwwwBGGGGBBlblll",
            "lblblbBBBBBGGGwwBBBBBBblblllb",
            "blblbBowBBBGGwwwBBBblblblblbl",
            "lblBBooBBggggwwwBwgBllblblblb",
            "lBBBwBBGGggBwwwwBBwgBblblblbl",
            "lBgGBBggggBwwwwwBBBgBlllblblb",
            "bBwGBgggwwgBwwwwBBggBblllblll",
            "lBwwBGggwwBBwwwBBgggBlblblllb",
            "llBwBGGggggBwwwBBgggBblbllbll",
            "lbBwwBGGGGBwwwBBBBBBllblblllb",
            "bllBBBBBBBwwwwBllblllblllblll",
            "lblBOOooBwwBBBBlblblblblblblb",
            "bllBOOooBBBoBBBBlllblllblllbl",
            "llBOOOOwoBOOoowBlllllllllllll",
            "llBOOOoooBOOOOoBlllllllllllll",
            "BBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
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
     
    #Drawing Toad
    elif character == "Toad":
        COLORS = {
            'r': "red",
            'b': "black",
            'w': "white",
            's': "sandy brown",
            'l': "blue",
            'o': "brown",
        }
        PIXELS = [
            "wwwwwbbbbbwwwwww",
            "wwwbbwwwwwbbwwww",
            "wwbwwwrrrwwwbwww",
            "wbwwwrrrrrwwwbww",
            "wbwwwrrrrrwwwwbw",
            "brwwwrrrrrwwwrbb",
            "brrwwwrrrwwwwrrb",
            "brrwwwwwwwwwwrrb",
            "brwwwbbbbwwwwrrb",
            "bwwbbbssbbbwwwrb",
            "bwbssbssbssbwwwb",
            "wbbssbssbsssbwbw",
            "wwbsssssssssbwbw",
            "wwbssbbbbsssbbww",
            "wwwbsssssssbbwww",
            "wwwbbbbbbbbbbwww",
            "wwbblbssblbssbww",
            "wbsblbssbllbssbw",
            "bsblbsssbllbssbw",
            "bsblbbbbblllbssb",
            "bsblbwwwwbllbssb",
            "wbbbwwbwwwbbbbbw",
            "wwwbwwwbwwwwbwww",
            "wwbooobboobbbwww",
            "wboooobooooobwww",
            "wbbbbbbbbbbbbwww",
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
                
    elif character == "Wario":
        COLORS = {
            'p': "purple",
            'y': "yellow",
            'B': "black",
            'w': "white",
            's': "sandy brown",
            'g': "green",
            'R': "brown",
            'm': "magenta",
        }
        PIXELS = [
            "wwwyyyyyywwww",
            "wwyyyyyyyyyyw",
            "wwRRRssBswwww",
            "wssRsssBsmmww",
            "wRsRRsBsBmmmw",
            "wRRssssBsBBww",
            "wwwssssssswww",
            "wwyypyypywwww",
            "wyyypyypyyyww",
            "yyyyppppyyyyw",
            "ssypyppypyssw",
            "sssppppppsssw",
            "wwpppwwpppwww",
            "wgggwwwwgggww",
            "ggggwwwwggggw",
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
        
        