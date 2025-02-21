import image

#finding the image and getting its width and height
img = image.Image("berries.jpg")
width = img.get_width()
height = img.get_height()

#creating a window and drawing the image inside that window
win = image.ImageWin(width, height)
img.draw(win)

#looking at all the pixels in the image
for y in range(height):
    for x in range(width):
        
        #defining the pixels as a variable and creating another variable to determine how far each pixel is from the line of symmetry
        the_pixel = img.get_pixel(x, y)
        distance = width - 1

        #changing the pixels or leaving them the same depending on their distance from the line of symmetry
        if x < distance:
            img.set_pixel(distance - x, y, the_pixel)
            
        else:
            img.set_pixel(x, y, the_pixel)      

    img.draw(win)


