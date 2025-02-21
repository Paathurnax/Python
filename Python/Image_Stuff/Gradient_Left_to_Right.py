import image

#creating a window and defining its width and height
width = 255
height = 255

win = image.ImageWin(width, height)
img = image.EmptyImage(width, height)


#looking at all the pixels in the window
for x in range(width):
    for y in range(height):
        
        #changing the colors of the pixels depending on their location relative to one half of the windows' width
        if x <= (int(width/2)):
            the_pixel = image.Pixel(255 - x, 0 + x, 0)
            img.set_pixel(x, y, the_pixel)
            
        elif x >= (int(width/2)):
            the_pixel = image.Pixel(255 - x, 0 + x, 0)
            img.set_pixel(x, y, the_pixel)
                    
            

    img.draw(win)

