import image

width = 255
height = 255

win = image.ImageWin(width, height)
img = image.EmptyImage(width, height)



for x in range(width):
    for y in range(height):
        if x <= (int(width/2)) or y <= (int(height/2)):
            the_pixel = image.Pixel(150, 50, 255 - x/2)
            img.set_pixel(x, y, the_pixel)
        elif x >= (int(width/2)) or  y >= (int(height/2)):
            the_pixel = image.Pixel(255 - x, 0 + x, 0)
            img.set_pixel(x, y, the_pixel)
                    
            

    img.draw(win)

