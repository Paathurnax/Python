import microbit
import turtle

screen = turtle.Screen()
jimmy = turtle.Turtle()
jimmy.shape("turtle")
jimmy.left(90)
while True:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    if x > 100:
        jimmy.right(10)
    elif x < -100:
        jimmy.left(10)   
    elif y > 100:
        jimmy.forward(5)
    elif y < -100:
        jimmy.backward(5)