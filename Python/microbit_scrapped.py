elif controller_type == "microbit":
    if john.xcor() == -1500:
        john.setheading(0)
    elif john.xcor() == 1500:
        john.setheading(180)
    elif john.ycor() == -500:
        john.setheading(90)
    elif john.ycor() == 500:
        john.setheading(270)
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    while john.xcor() > -1500 and john.xcor() < 1500 and john.ycor() > -500 and john.ycor() < 500:
        if x == 0 and y == 0:
            microbit_popup()        
        elif x > 100:
            east()
        elif x < -100:
            west()
        elif y > 100:
            north()
        elif y < -100:
            south()
        elif microbit.button_a.was_pressed():
            john.color(str(random.choice(colors)))
        elif microbit.button_b.was_pressed():
            draw_shape = random.choice(["circle", "triangle", "square", "pentagon", "hexagon", "septagon", "octagon", "star"])
            if draw_shape == "circle":
                draw_circle()
            elif draw_shape == "triangle":
                draw_triangle()
            elif draw_shape == "square":
                draw_square()
            elif draw_shape == "pentagon":
                draw_pentagon()
            elif draw_shape == "hexagon":
                draw_hexagon()
            elif draw_shape == "septagon":
                draw_septagon()
            elif draw_shape == "octagon":
                draw_octagon()
            elif draw_shape == "star":
                draw_star()


