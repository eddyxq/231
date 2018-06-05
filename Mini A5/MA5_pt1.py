# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01
# Ver. 1.0.0
# June 14, 2017

"""
A program that will draw a pink rectangle with gold borders.
"""


from tkinter import *

aWindow = Frame()
aButton = Button(aWindow)

# Since the parameter list is pre-defined passing aButton into the function
# is problematic (created as a global).
def button_clicked() :
    window = Tk()
    aDrawingCanvas = Canvas(window,width=640,height=480,bg ="white")

    # Draws rectangle
    aDrawingCanvas.create_rectangle(50,100,250,200, fill ="pink", outline ="gold")
     
    # Draw window and start the gui
    aDrawingCanvas.pack()
    window.mainloop()


def start ():
    global aWindow
    global aButton

    aWindow.pack()
    aButton["text"] = "Press me"
    aButton["command"] = button_clicked
    aButton.grid(row=0, column=0)
    aWindow.mainloop()

start()