import microbit
import turtle

screen = turtle.Screen()
jimmy = turtle.Turtle()
jimmy.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    
    if x > 100:
        print("RIGHT")
        jimmy.forward(5)
    elif x < -100:
        print("LEFT")
        jimmy.backward(5)
    else:
        print("FLAT")
