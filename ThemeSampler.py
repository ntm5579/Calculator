import tkinter as tk
from tkinter import *
from Theme import *

window = tk.Tk()
window.title("Sampler")
window.geometry('500x620')
window.resizable(False, False)

Header = Label(window, text = "Test", bg= "teal")
Header.grid(column = 0, columnspan = len(themes), row = 0)

samplers = []
class Sampler():
    def __init__(self, myTheme):
        self.Frame = Frame(window, bg = myTheme.bgColor)
        self.Button1 = Button(self.Frame, fg = fontColor, bg = buttonColor)

def selectTheme(i):
    currentTheme = themes[i]

for i in range(len(themes)):
    samplers.append(Sampler(themes[i]))
    samplers[i].grid(column = i, row = 1)



