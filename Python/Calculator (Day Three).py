#determining the type of shape
shape = input("Are you calculating the area of a circle, triangle or a rectangle? ")

#calculating the area of a circle
if shape == "circle":
    radius = float(input("What's the radius? "))
    print("The area is " + str(3.1415926535897932384626*(radius**2)))

#calculating the area of a triangle
elif shape == "triangle":
    base = float(input("What's the base? "))
    height = float(input("What's the height? "))
    print("The area is " + str((0.5*base)*height))

#calculating the area of a rectangle
elif shape == "rectangle":
    length = float(input("What's the length? "))
    width = float(input("What's the width? "))
    print("The area is " + str(length*width))
                   
 
 