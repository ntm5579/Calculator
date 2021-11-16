import tkinter as tk
from tkinter import *

#graphic calculator 3d slots

#theming stuff--------------------------------------------------------------
bgColor = 'lightgrey'
red = 'firebrick'

def themer(button, color = True, size= True, font = True, pad = True):
    if color:
        button.config(fg = 'white', bg = 'darkgray')
    if size:
        button.config(width= 4, height= 2)
    if font:
        button.config(font= ("Courier New", 20, "bold"))
    if pad:
        button.grid(padx= 5, pady= 5)

#---------------------------------------------------------------------------

window = tk.Tk()
window.title("Calculator")
window.geometry('500x600')
window.config(bg= bgColor)
window.resizable(False, False)

displayLabel = Label(window, text = 'test and 000101010', width = 40, height = 2, bg = 'white', font = ("Courier New", 12, "bold"))
displayLabel.grid(column= 0, row = 0, padx = 5, pady = 5, columnspan= 3)

numFrame = Frame(window, width = 100, height = 100)
numFrame.config(bg= bgColor)
numFrame.grid(column= 0, row = 2, rowspan = 4)

button7 = Button(numFrame, text = "7",  command= None) 
themer(button7)
button7.grid(column= 0, row = 0)

button8 = Button(numFrame, text = "8",  command= None) 
themer(button8)
button8.grid(column= 1, row = 0)

button9 = Button(numFrame, text = "9",  command= None) 
themer(button9)
button9.grid(column= 2, row = 0)

button4 = Button(numFrame, text = "4",  command= None) 
themer(button4)
button4.grid(column= 0, row = 1)

button5 = Button(numFrame, text = "5",  command= None) 
themer(button5)
button5.grid(column= 1, row = 1)

button6 = Button(numFrame, text = "6",  command= None) 
themer(button6)
button6.grid(column= 2, row = 1)

button1 = Button(numFrame, text = "1",  command= None) 
themer(button1)
button1.grid(column= 0, row = 2)

button2 = Button(numFrame, text = "2",  command= None) 
themer(button2)
button2.grid(column= 1, row = 2)

button3 = Button(numFrame, text = "3",  command= None) 
themer(button3)
button3.grid(column= 2, row = 2)

button0 = Button(numFrame, text = "0",  command= None) 
themer(button0)
button0.grid(column= 0, row = 3)

buttonDot = Button(numFrame, text = ".",  command= None) 
themer(buttonDot)
buttonDot.grid(column= 1, row = 3)

buttonEquals = Button(numFrame, text = "=",  command= None) 
buttonEquals.config(bg = red)
themer(buttonEquals, color= False)
buttonEquals.grid(column= 2, row = 3)

buttonMult = Button(window, text = 'x',  command= None) 
themer(buttonMult)
buttonMult.grid(column = 2, row = 2)

buttonMinus = Button(window, text = '-',  command= None) 
themer(buttonMinus)
buttonMinus.grid(column = 2, row = 3)

buttonPlus = Button(window, text = '+',  command= None) 
themer(buttonPlus, size=False)
buttonPlus.config(width = 4, height = 4)
buttonPlus.grid(column = 2, row = 4, rowspan = 2)

window.mainloop()
