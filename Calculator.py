import tkinter as tk
from tkinter import *

#graphic calculator 3d slots

#theming stuff--------------------------------------------------------------
bgColor = 'cornflowerblue'
red = 'firebrick'

def themer(button, color = True, size= True, font = True, pad = True, unsunken=True, border = True):
    if color:
        button.config(fg = 'white', bg = 'slategray')
    if size:
        button.config(width= 4, height= 2)
    if font:
        button.config(font= ("Courier New", 20, "bold"))
    if pad:
        button.grid(padx= 5, pady= 5)
    if unsunken:
        button.config(relief = 'groove')
    if border:
        pass

#---------------------------------------------------------------------------
#Button functions
def numButton(button):
    displayLabel.config(text= displayLabel.cget("text") + button.cget("text"))


#passed as an argument when the equals button it called
current_function = None
num1 = None
def setFunction(myFunc):
    #sets global current function to the one pressed
    #clears the screen of the old number and saves it in global num1

    pass

def equals(num1, num2, funcion):
    #get the current text from label, or do that at call
    #casting
    #check the function passed
    #display the new number formated on displayLabel
    pass

#------------------------------------------------------------------------------
window = tk.Tk()
window.title("Calculator")
window.geometry('500x600')
window.config(bg= bgColor)
window.resizable(False, False)

#might want to change this to a text field?
displayLabel = Label(window, text = '', width = 40, height = 2, bg = 'white', font = ("Courier New", 12, "bold"))
displayLabel.grid(column= 0, row = 0, padx = 5, pady = 5, columnspan= 3)

numFrame = Frame(window, width = 100, height = 100)
numFrame.config(bg= bgColor)
numFrame.grid(column= 0, row = 2, rowspan = 4)

button7 = Button(numFrame, text = "7",  command= lambda:numButton(button7)) 
themer(button7)
button7.grid(column= 0, row = 0)

button8 = Button(numFrame, text = "8",  command= lambda:numButton(button8)) 
themer(button8)
button8.grid(column= 1, row = 0)

button9 = Button(numFrame, text = "9",  command= lambda:numButton(button9)) 
themer(button9)
button9.grid(column= 2, row = 0)

button4 = Button(numFrame, text = "4",  command= lambda:numButton(button4)) 
themer(button4)
button4.grid(column= 0, row = 1)

button5 = Button(numFrame, text = "5",  command= lambda:numButton(button5)) 
themer(button5)
button5.grid(column= 1, row = 1)

button6 = Button(numFrame, text = "6",  command= lambda:numButton(button6)) 
themer(button6)
button6.grid(column= 2, row = 1)

button1 = Button(numFrame, text = "1",  command= lambda:numButton(button1)) 
themer(button1)
button1.grid(column= 0, row = 2)

button2 = Button(numFrame, text = "2",  command= lambda:numButton(button2)) 
themer(button2)
button2.grid(column= 1, row = 2)

button3 = Button(numFrame, text = "3",  command= lambda:numButton(button3)) 
themer(button3)
button3.grid(column= 2, row = 2)

button0 = Button(numFrame, text = "0",  command= lambda:numButton(button0)) 
themer(button0)
button0.grid(column= 0, row = 3)

buttonDot = Button(numFrame, text = ".",  command= lambda:numButton(buttonDot)) 
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
buttonPlus.config(width = 4, height = 5)
buttonPlus.grid(column = 2, row = 4, rowspan = 2)

window.mainloop()