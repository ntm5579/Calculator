#import tkinter as tk
from tkinter import *
from tkinter.ttk import *

#graphic calculator 3d slots

#theming stuff--------------------------------------------------------------
style = Style()
style.configure('normalButton', font= ("Courier New", 20, "bold"), foreground = 'white', background='darkgray')
bgColor = 'lightgrey'
red = 'firebrick'

#---------------------------------------------------------------------------

window = Tk()
window.title("Calculator")
window.geometry('500x600')
window.config(bg= bgColor)
window.resizable(False, False)

displayLabel = Label(window, text = 'test and 000101010', width = 40, height = 2, bg = 'white', font = ("Courier New", 12, "bold"))
displayLabel.grid(column= 0, row = 0, padx = 5, pady = 5, columnspan= 3)

numFrame = Frame(window, width = 100, height = 100)
#numFrame.config(bg= bgColor)
numFrame.grid(column= 0, row = 2, rowspan = 4)

button7 = Button(numFrame, text = "7", style = 'normalButton', command= None)
button7.grid(column= 0, row = 0)

button8 = Button(numFrame, text = "8", style = 'normalButton', command= None)
button8.grid(column= 1, row = 0)

button9 = Button(numFrame, text = "9", style = 'normalButton', command= None)
button9.grid(column= 2, row = 0)

button4 = Button(numFrame, text = "4", style = 'normalButton', command= None)
button4.grid(column= 0, row = 1)

button5 = Button(numFrame, text = "5", style = 'normalButton', command= None)
button5.grid(column= 1, row = 1)

button6 = Button(numFrame, text = "6", style = 'normalButton', command= None)
button6.grid(column= 2, row = 1)

button1 = Button(numFrame, text = "1", style = 'normalButton', command= None)
button1.grid(column= 0, row = 2)

button2 = Button(numFrame, text = "2", style = 'normalButton', command= None)
button2.grid(column= 1, row = 2)

button3 = Button(numFrame, text = "3", style = 'normalButton', command= None)
button3.grid(column= 2, row = 2)

button0 = Button(numFrame, text = "0", style = 'normalButton', command= None)
button0.grid(column= 0, row = 3)

buttonDot = Button(numFrame, text = ".", style = 'normalButton', command= None)
buttonDot.grid(column= 1, row = 3)

buttonEquals = Button(numFrame, text = "=", style = 'normalButton', command= None)
buttonEquals.config(bg = red)
buttonequals.grid(column= 2, row = 3)

buttoMmult = Button(window, text = 'x', style = 'normalButton', command= None)
buttonMult.grid(column = 2, row = 2)

buttonMinus = Button(window, text = '-', style = 'normalButton', command= None)
buttonMinus.grid(column = 2, row = 3)

buttonPlus = Button(window, text = '+', style = 'normalButton', command= None)
buttonPlus.config(width = 5, height = 4)
buttonPlus.grid(column = 2, row = 4, rowspan = 2)

window.mainloop()