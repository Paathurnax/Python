import image

rooster = image.Image("rooster.jpg")
width_1 = rooster.get_width()
height_1 = rooster.get_height()

smile = image.Image("smile.png")
width_2 = smile.get_width()
height_2 = smile.get_height()


window = image.ImageWin(width_1, height_1)
rooster.draw(window)

for y in range(height_2):
    for x in range(width_2):
        the_pixel = smile.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()

        if (r < 255 or g < 255 or b < 255):               
            rooster.set_pixel(x + 165, y + 52, the_pixel)
    rooster.draw(window)
        
        
        