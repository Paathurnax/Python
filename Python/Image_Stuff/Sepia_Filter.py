import image

#finding image file and getting its width and height
img = image.Image("sneakers.jpg")
width = img.get_width()
height = img.get_height()

#creating a window for the image
win = image.ImageWin(width, height)
img.draw(win)

#looking at all the pixels
for x in range(width):
    for y in range(height):
        
        #defining the pixels being looked at as a variable
        the_pixel = img.get_pixel(x, y)
        
        #get the colors
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #changing the rgb values of the pixels to replicate the filter sepia
        new_r = (r * .393) + (g *.769) + (b * .189)
        new_g = (r * .349) + (g *.686) + (b * .168)
        new_b = (r * .272) + (g *.534) + (b * .131)
        
        #creating and drawing a new pixel with the altered rgb values
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)
    img.draw(win)


    

