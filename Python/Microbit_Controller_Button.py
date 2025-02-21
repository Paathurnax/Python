import microbit
import turtle

screen = turtle.Screen()
jimmy = turtle.Turtle()
jimmy.shape("turtle")
jimmy.left(90)
while True:
    y = microbit.accelerometer.get_y()
    if microbit.button_a.was_pressed():
        jimmy.right(90)
    elif microbit.button_b.was_pressed():
        jimmy.left(90)   
    elif y > 100:
        jimmy.forward(5)
    elif y < -100:
        jimmy.backward(5)