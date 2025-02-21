import image

width = 250
height = 200

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

the_pixel = image.Pixel(255, 0, 0)


for y in range(height):
    for x in range(width):
        the_image.set_pixel(x, y, the_pixel)
        
the_image.draw(canvas)