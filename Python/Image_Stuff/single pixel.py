import image

width = 400
height = 300

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

this_pixel = image.Pixel(255, 0, 0)
the_pixel = image.Pixel(0, 255, 0)

for y in (50, 100, 150, 200, 250):
    for i in range(400):
        the_image.set_pixel(i, y, this_pixel)

for x in (50, 100, 150, 200, 250, 300, 350):
    for i in range(300):
        the_image.set_pixel(x, i, the_pixel)

the_image.draw(canvas)