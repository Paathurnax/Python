import random
import PySimpleGUI as psg

draw_shape = random.choice(["circle", "triangle", "square", "pentagon", "hexagon", "septagon", "octagon", "star"])
print(draw_shape)

def microbit_popup():
    file=open("turtlecontrolmicrobit.txt", "r", encoding="UTF-8")
    text=file.read()
    psg.popup_scrolled(text, title="Microbit Controls", font=("Helvetica", 16), size=(50,20))

microbit_popup()