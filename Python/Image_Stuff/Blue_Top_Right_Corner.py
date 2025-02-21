import image

#finding the image and getting its width and height
img = image.Image("berries.jpg")
width = img.get_width()
height = img.get_height()

#creating a window and drawing the image inside the window
win = image.ImageWin(width, height)
img.draw(win)

#looking at all the pixels
for y in range(height):
    for x in range(width):
        
        #defing the pixels being looked at as a variable and getting the pixels colors
        the_pixel = img.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #changing the rgb values of the pixels depending on their locations
        if x > width/2 and y < height/2:
            new_r = r
            new_g = g
            new_b = b + 100
        
        #leaving the pixels that are outside the top right corner the same as before
        else:
            new_r = r
            new_g = g
            new_b = b
            
        #making a new pixel using the altered rgb values
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)      

    img.draw(win)
