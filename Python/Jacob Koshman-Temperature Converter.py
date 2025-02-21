
########################################################################################
#Jacob Koshman
#Computer Science 20
#March 26, 2024
#
#Tempurature Converter
#Purpose: To convert a temperature from celsius to fahrenheit or kelvin and vice versa.
########################################################################################
print("Answers must be between -9999.99 and 9999.99")
print("Answer all questions except for the question below with just numbers")
print("---------------------------------------------------------------------------------------")

#asking what conversion is being made
conversion_type = input("Are you converting celsius to fahrenheit, fahrenheit to celsius, kelvin to celsius, celsius to kelvin, fahrenheit to kelvin or kelvin to farenheit? ")

#converting the temperatures

#celsius to fahrenheit    
if conversion_type == "celsius to fahrenheit":
    celsius = input("What is the temperature? ")
    try:
        if float(celsius) >= -9999.99 and float(celsius) <= 9999.99:
            print("That is " + str(((float(celsius)*9/5) + 32)) + " degrees fahrenheit!")
        else:
            print("Value being converted cannot be more than 9999.99 or less than -9999.99") 
    except:
        print("Try again")

#fahrenheit to celsius
elif conversion_type == "fahrenheit to celsius":
    fahrenheit = input("What is the temperature? ")
    try:
        if float(fahrenheit) >= -9999.99 and float(fahrenheit) <= 9999.99:
            print("That is " + str(((float(fahrenheit) - 32)*5/9)) + " degrees celsius!")
        else:
            print("Value being converted cannot be more than 9999.99 or less than -9999.99")
    except:
        print("Try again")

#kelvin to celsius
elif conversion_type == "kelvin to celsius":
    kelvin = input("What is the temperature? ")
    try:
        if float(kelvin) >= -9999.99 and float(kelvin) <= 9999.99:
            print("That is " + str(((float(kelvin) - 273.15))) + " degrees celsius!")
        else:
            print("Value being converted cannot be more than 9999.99 or less than -9999.99")
    except:
        print("Try again")


#celsius to kelvin
elif conversion_type == "celsius to kelvin":
    celsius = input("What is the temperature? ")
    try:
        if float(celsius) >= -9999.99 and float(celsius) <= 9999.99:
            print("That is " + str(((float(celsius)*9/5) + 32)) + " kelvin!")
        else:
            print("Value being converted cannot be more than 9999.99 or less than -9999.99") 
    except:
        print("Try again")

#fahrenheit to kelvin
elif conversion_type == "fahrenheit to kelvin":
    fahrenheit = input("What is the temperature? ")
    try:
        if float(fahrenheit) >= -9999.99 and float(fahrenheit) <= 9999.99:
            print("That is " + str(((float(fahrenheit) - 32)*5/9)) + " kelvin!")
        else:
            print("Value being converted cannot be more than 9999.99 or less than -9999.99")
    except:
        print("Try again")


#kelvin to fahrenheit
elif conversion_type == "kelvin to fahrenheit":
    kelvin = input("What is the temperature? ")
    try:
        if float(kelvin) >= 9999.99 and float(kelvin) <= 9999.99:
            print("That is " + str(((float(kelvin) - 273.15))) + " degrees celsius!")
        else:
            print("Value being converted cannot be more than 9999.99 or less than -9999.99")
    except:
        print("Try again")

else:
    print("Try again")