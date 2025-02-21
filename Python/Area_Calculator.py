import streamlit as st

st.title("Area Calculator For Circles, Rectangles, and Triangles")
st.subheader("Only Answer With Numbers")
area_type = st.selectbox("What shape are you calculating the area of?", ["circle", "rectangle", "triangle"])

if area_type == "circle":
    radius = st.text_input("What is the radius?")
    if radius:
        try:
            st.text("The area is " + str(3.14*(float(radius)**2)))
        except:
            st.text("Try again")
            
elif area_type == "rectangle":
    length = st.text_input("What is the length?")
    width = st.text_input("What is the width?")
    if length and width:
        try:
            st.text("The area is " + str(float(length)*(float(width))))       
        except:
            st.text("Try again")
        
elif area_type == "triangle":
    base = st.text_input("What is the base?")
    height = st.text_input("What is the height?")
    if base and height:
        try:
            st.text("The area is " + str(float(base)*(float(height))))
        except:
            st.text("Try again")