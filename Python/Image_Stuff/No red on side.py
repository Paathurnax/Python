import image

img = image.Image("berries.jpg")
width = img.get_width()
height = img.get_height()

win = image.ImageWin(width, height)
img.draw(win)


for y in range(height):
    for x in range(int(width/2)):
        the_pixel = img.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()

        new_r = 0
        new_g = g
        new_b = b
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)      

    img.draw(win)
