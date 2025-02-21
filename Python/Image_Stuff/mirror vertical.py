import image

img = image.Image("berries.jpg")
width = img.get_width()
height = img.get_height()

win = image.ImageWin(width, height)
img.draw(win)


for y in range(height):
    for x in range(width):
        the_pixel = img.get_pixel(x, y)
        distance = height - 1
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        new_pixel = image.Pixel(r, g, b)

        if y < distance:
            img.set_pixel(x, distance - y, the_pixel)
            
        else:
            img.set_pixel(x, y, new_pixel)      

    img.draw(win)


