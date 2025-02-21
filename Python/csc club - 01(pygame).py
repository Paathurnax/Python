import random
import turtle

WIDTH = 800
HEIGHT = 800
SIZE = 20


def random_food_position():
    x = random.randint(-WIDTH/2 + SIZE, WIDTH/2 - SIZE)
    y = random.randint(-HEIGHT/2+SIZE, HEIGHT/2-SIZE)
    return x, y

def start():
    global snake_direction, food_position, snake
    snake_direction = "up"
    snake = [[0, 0], [0,20], [0, 40], [0, 60], [0, 80]]
    food_position = random_food_position()
    food.goto(food_position)
    move_snake()
    
def move_snake():
    new_head = snake[-1].copy()
    
    if snake_direction == "up":
        new_head[1] += SIZE
    elif snake_direction = "down":
        new_head[1] -= SIZE
    elif snake_direction = "left":
        new_head[0] -= SIZE
    else:
        new_head[0] += SIZE
        
    if new_head in snake:
        start()
    
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"
        
def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"
        
def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"
        
def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

#window
window = turtle.Screen()
window.setup(WIDTH, HEIGHT)
window.bgcolor("green")
window.title("Snake Game")

#food
food = turtle.Turtle("circle")
food.color("red")
food.penup()

#pen
pen = turtle.Turtle("square")
pen.penup()


window.listen()
window.onkey(go_up, "w")
window.onkey(go_left, "a")
window.onkey(go_down, "s")
window.onkey(go_right, "d")
start()
turtle.done()