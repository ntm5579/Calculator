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
#Top Button functions
def checkDisplayClear():
    if displayLabel.cget("text").count('=') > 0:
        displayLabel.config(text = '')

def numButton(button):
    checkDisplayClear()
    displayLabel.config(text= displayLabel.cget("text") + button.cget("text"))

def allClear():
    global num1
    global num2
    global currentFunction
    num1 = None
    num2 = None
    currentFunction = None
    displayLabel.config(text='')

#passed as an argument when the equals button it called
currentFunction = None
num1 = None
num2 = None
def setFunction(button):
    #sets global current function to the one pressed
    global num1
    global currentFunction
    num1 = displayLabel.cget("text")
    displayLabel.config(text= '')
    currentFunction = button.cget("text")

#does not work, error about floats
def equals():
    global num1
    global num2
    global currentFunction
    num2 = displayLabel.cget("text")
    try:
        num1 = float(num1)
        num2 = float(num2)
    except TypeError:
        print("None Type Probably")
        return
    if currentFunction == '+':
        result = num1 + num2
    elif currentFunction == '-':
        result = num1 - num2
    elif currentFunction == 'x':
        result = num1 * num2
    elif currentFunction == '/':
        result = num1 / num2
    elif currentFunction == 'x\u207F':
        result = num1 ** num2
    else:
        print('What kinda funky shit are you trying?')
        return
    displayLabel.config(text= '= ' + str(result))
    num1 = result 
    num2 = None
    return result
#------------------------------------------------------------------------------
window = tk.Tk()
window.title("Calculator")
window.geometry('500x620')
window.config(bg= bgColor)
window.resizable(False, False)

#might want to change this to a text field?
displayLabel = Label(window, text = '', width = 40, height = 4, bg = 'white', font = ("Courier New", 14, "bold"), justify = 'right')
displayLabel.grid(column= 0, row = 0, padx = 20, pady = 20, columnspan= 4)

buttonAllClear = Button(window, text= 'Ac', command=allClear)
themer(buttonAllClear)
buttonAllClear.grid(column= 0, row = 1)

buttonExp = Button(window, text= 'x\u207F', command=lambda:setFunction(buttonExp))
themer(buttonExp)
buttonExp.grid(column= 1, row = 1)

buttonTBD2 = Button(window, text= 'TBD2')
themer(buttonTBD2)
buttonTBD2.grid(column= 2, row = 1)

buttonDiv = Button(window, text= '/', command= lambda:setFunction(buttonDiv))
themer(buttonDiv)
buttonDiv.grid(column= 3, row = 1)

button7 = Button(window, text = "7",  command= lambda:numButton(button7)) 
themer(button7)
button7.grid(column= 0, row = 2)

button8 = Button(window, text = "8",  command= lambda:numButton(button8)) 
themer(button8)
button8.grid(column= 1, row = 2)

button9 = Button(window, text = "9",  command= lambda:numButton(button9)) 
themer(button9)
button9.grid(column= 2, row = 2)

button4 = Button(window, text = "4",  command= lambda:numButton(button4)) 
themer(button4)
button4.grid(column= 0, row = 3)

button5 = Button(window, text = "5",  command= lambda:numButton(button5)) 
themer(button5)
button5.grid(column= 1, row = 3)

button6 = Button(window, text = "6",  command= lambda:numButton(button6)) 
themer(button6)
button6.grid(column= 2, row = 3)

button1 = Button(window, text = "1",  command= lambda:numButton(button1)) 
themer(button1)
button1.grid(column= 0, row = 4)

button2 = Button(window, text = "2",  command= lambda:numButton(button2)) 
themer(button2)
button2.grid(column= 1, row = 4)

button3 = Button(window, text = "3",  command= lambda:numButton(button3)) 
themer(button3)
button3.grid(column= 2, row = 4)

button0 = Button(window, text = "0",  command= lambda:numButton(button0)) 
themer(button0)
button0.grid(column= 0, row = 5)

buttonDot = Button(window, text = ".",  command= lambda:numButton(buttonDot)) 
themer(buttonDot)
buttonDot.grid(column= 1, row = 5)
#--------------------------------------------------------------------------------
#right side function buttons
buttonEquals = Button(window, text = "=",  command= lambda:equals()) 
buttonEquals.config(bg = red)
themer(buttonEquals, color= False)
buttonEquals.grid(column= 2, row = 5)

buttonMult = Button(window, text = 'x',  command= lambda:setFunction(buttonMult)) 
themer(buttonMult)
buttonMult.grid(column = 3, row = 2)

buttonMinus = Button(window, text = '-',  command= lambda:setFunction(buttonMinus)) 
themer(buttonMinus)
buttonMinus.grid(column = 3, row = 3)

buttonPlus = Button(window, text = '+',  command= lambda:setFunction(buttonPlus)) 
themer(buttonPlus, size=False)
buttonPlus.config(width = 4, height = 5)
buttonPlus.grid(column = 3, row = 4, rowspan = 2)

window.mainloop()