import image

img = image.Image("sneakers.jpg")
width = img.get_width()
height = img.get_height()

win = image.ImageWin(width, height)
img.draw(win)

for x in range(width):
    for y in range(height):
        the_pixel = img.get_pixel(x, y)
        
        #get the colors
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #halfing the red
        new_r = r/2
        new_g = g
        new_b = b
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)
    img.draw(win)


    

