import image

#finding the image and getting its width and height
img = image.Image("berries.jpg")
width = img.get_width()
height = img.get_height()

#creating a window for the image
win = image.ImageWin(width, height)
img.draw(win)

#looking at all the pixels
for y in range(height):
    for x in range(width):
        
        #defining all of the pixels it is looking at as a variable and obtaining the rgb values of those pixels
        the_pixel = img.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #changing and leaving pixels the same based on their locations
        if x < width/2:
            img.set_pixel(x + 200, y, the_pixel)
            
        else:
            img.set_pixel(x, y, the_pixel)      

    img.draw(win)

