import image

flag = image.Image("skflag.png")

width = flag.get_width()
height = flag.get_height()
new_value = -243

canvas = image.ImageWin(width, height)
flag.draw(canvas)

for y in range(height):
    for x in range(width):
        current_pixel = flag.get_pixel(x, y)
        r = current_pixel.get_red()
        g = current_pixel.get_green()
        b = current_pixel.get_blue()
        
        the_pixel = image.Pixel(r + new_value, g + new_value, b + new_value)
        
        
        flag.set_pixel(x, y, the_pixel)
        
    flag.draw(canvas)