import PySimpleGUI as psg

age = psg.popup_get_text("How old are you?")

if int(age) > 15:
    psg.popup("Wow already " + age + " years old!")