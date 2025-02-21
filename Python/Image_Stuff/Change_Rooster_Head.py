import image

#finding the image file and getting its width and height
img = image.Image("rooster.jpg")
width = img.get_width()
height = img.get_height()

#creating a window for the image and displaying he original image
win = image.ImageWin(width, height)
img.draw(win)

#looking at all the pixels
for y in range(height):
    for x in range(width):
        
        #defining the pixels it is looking at as a variable and getting the rgb values of those pixels
        the_pixel = img.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #changing certain pixels based on their rgb values
        if r > 190 and b < 165 and g < 165:
            new_r = 0
            new_g = 0
            new_b = 255
        
        #leaving the other pixels the same
        else:
            new_r = r
            new_g = g
            new_b = b
            
        #defining and setting a new pixel
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)      

    img.draw(win)

