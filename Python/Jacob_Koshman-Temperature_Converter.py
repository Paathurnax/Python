import streamlit as st

########################################################################################
#Jacob Koshman
#Computer Science 20
#March 26, 2024
#
#Tempurature Converter
#Purpose: To convert a temperature from celsius to fahrenheit or kelvin and vice versa.
########################################################################################
st.title("Temperature Converter") 
st.subheader("Answer With Just Numbers")
st.subheader("Answers Must Be Between -9999.99 and 9999.99")
conversion_type = st.selectbox("What are you converting?", ["celsius to fahrenheit", "fahrenheit to celsius", "kelvin to celsius", "celsius to kelvin", "kelvin to fahrenheit", "fahrenheit to kelvin"])

#converting the temperatures

#celsius to fahrenheit    
if conversion_type == "celsius to fahrenheit":
    celsius = st.text_input("What is the temperature? ")
    if celsius:
        try:
            if float(celsius) >= -9999.99 and float(celsius) <= 9999.99:
                st.text("That is " + str(((float(celsius)*9/5) + 32)) + " degrees fahrenheit!")
            else:
                st.text("Value being converted cannot be more than 9999.99 or less than -9999.99") 
        except:
            st.text("Try again")
        
#fahrenheit to celsius
elif conversion_type == "fahrenheit to celsius":
    fahrenheit = st.text_input("What is the temperature? ")
    if fahrenheit:
        try:
            if float(fahrenheit) >= -9999.99 and float(fahrenheit) <= 9999.99:
                st.text("That is " + str(((float(fahrenheit) - 32)*5/9)) + " degrees celsius!")
            else:
                st.text("Value being converted cannot be more than 9999.99 or less than -9999.99")
        except:
            st.text("Try again")

#kelvin to celsius
elif conversion_type == "kelvin to celsius":
    kelvin = st.text_input("What is the temperature? ")
    if kelvin:
        try:
            if float(kelvin) >= -9999.99 and float(kelvin) <= 9999.99:
                st.text("That is " + str(((float(kelvin) - 273.15))) + " degrees celsius!")
            else:
                st.text("Value being converted cannot be more than 9999.99 or less than -9999.99")
        except:
            st.text("Try again")

#celsius to kelvin
elif conversion_type == "celsius to kelvin":
    celsius = st.text_input("What is the temperature? ")
    if celsius:
        try:
            if float(celsius) >= -9999.99 and float(celsius) <= 9999.99:
                st.text("That is " + str(((float(celsius)*9/5) + 32)) + " kelvin!")
            else:
               st.text("Value being converted cannot be more than 9999.99 or less than -9999.99") 
        except:
            st.text("Try again")

#fahrenheit to kelvin
elif conversion_type == "fahrenheit to kelvin":
    fahrenheit = st.text_input("What is the temperature? ")
    if fahrenheit:
        try:
            if float(fahrenheit) >= -9999.99 or float(fahrenheit) <= 9999.99:
                st.text("That is " + str(((float(fahrenheit) - 32)*5/9)) + " kelvin!")
            else:
                st.text("Value being converted cannot be more than 9999.99 or less than -9999.99")
        except:
            st.text("Try again")

#kelvin to fahrenheit
elif conversion_type == "kelvin to fahrenheit":
    kelvin = st.text_input("What is the temperature? ")
    if kelvin:
        try:
            if float(kelvin) >= 9999.99 and float(kelvin) <= 9999.99:
                st.text("That is " + str(((float(kelvin) - 273.15))) + " degrees celsius!")
            else:
                st.text("Value being converted cannot be more than 9999.99 or less than -9999.99")
        except:
            st.text("Try again")
