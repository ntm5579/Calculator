import tkinter as tk
from tkinter import *

#graphic calculator 3d slots

#theming stuff--------------------------------------------------------------
class Theme():
    def __init__(self, font = 'black', button = 'white', bg = 'lightgray', second = 'white', third =  'white'):
        self.fontColor = font
        self.buttonColor = button
        self.bgColor = bg
        self.secondaryColor = second
        self.tertiaryColor = third

mainDark = Theme('black', 'lightgray', 'dimgray', 'sandybrown', 'lightskyblue')
altDark = Theme('white', 'slategray','lightgray', 'sandybrown', 'red')
mainColorful = Theme('white', 'slategray', 'cornflowerblue', 'sandybrown', 'red')
altColorful = Theme('white', 'mediumslateblue', 'mediumspringgreen', 'cyan', '#89043D')
neutral = Theme('saddlebrown', 'peachpuff', 'linen', 'darkturquoise', 'salmon')
grayscale = Theme()

currentTheme = mainDark

elementList = []

def themer(button, color = True, size= True, theme = currentTheme, alignment = True):
    if color:
        button.config(fg = theme.fontColor, bg = theme.buttonColor)
    if size:
        button.config(width= 4, height= 2)
    button.config(font= ("Courier New", 20, "bold"))
    if alignment:
        button.grid(padx= 5, pady= 5)
    button.config(relief = 'solid', activebackground=theme.bgColor)
    if(elementList.count(button) < 1):
        elementList.append(button)

def changeTheme(theme, elements):
    for element in elements:
        themer(element, theme = theme)

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
    displayContents = displayLabel.cget("text")
    if displayContents.count('=') < 1:
        num2 = displayContents
    else:
        print('um')
    
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
    #num2 = None
    return result
#------------------------------------------------------------------------------
window = tk.Tk()
window.title("Calculator")
window.geometry('500x620')
window.config(bg= currentTheme.bgColor)
window.resizable(False, False)

alignFrame = Frame(window, bg= currentTheme.bgColor)
alignFrame.pack()
elementList.append(alignFrame)

clicked = StringVar()
clicked.set('mainDark')
drop = OptionMenu(window, clicked, 'mainDark', 'altDark', 'maincolorful', 'altColorful', 'neutral')
themer(drop, alignment=False, size = False)
drop.config(font= ("Courier New", 11, "bold"), padx = 5, height = 1)
drop.pack()
dropButton = Button(window)
themer(dropButton, alignment=False, size = False)
dropButton.config(font= ("Courier New", 11, "bold"), padx = 5, height = 1)
dropButton.pack()


def initThemeChange(clicked):
    pass

#might want to change this to a text field?
displayLabel = Label(alignFrame, text = '', width = 23, height = 2, bg = 'white', font = ("Courier New", 20, "bold"), relief='solid')
displayLabel.grid(column= 0, row = 0, padx = 15, pady = 15, columnspan= 4)

buttonAllClear = Button(alignFrame, text= 'Ac', command=allClear)
themer(buttonAllClear, color= False)
buttonAllClear.config(fg= currentTheme.fontColor, bg = currentTheme.secondaryColor)
buttonAllClear.grid(column= 0, row = 1)

buttonExp = Button(alignFrame, text= 'x\u207F', command=lambda:setFunction(buttonExp))
themer(buttonExp)
buttonExp.grid(column= 1, row = 1)

buttonTBD2 = Button(alignFrame, text= 'TBD2')
themer(buttonTBD2)
buttonTBD2.grid(column= 2, row = 1)

buttonDiv = Button(alignFrame, text= '/', command= lambda:setFunction(buttonDiv))
themer(buttonDiv)
buttonDiv.grid(column= 3, row = 1)

button7 = Button(alignFrame, text = "7",  command= lambda:numButton(button7)) 
themer(button7)
button7.grid(column= 0, row = 2)

button8 = Button(alignFrame, text = "8",  command= lambda:numButton(button8)) 
themer(button8)
button8.grid(column= 1, row = 2)

button9 = Button(alignFrame, text = "9",  command= lambda:numButton(button9)) 
themer(button9)
button9.grid(column= 2, row = 2)

button4 = Button(alignFrame, text = "4",  command= lambda:numButton(button4)) 
themer(button4)
button4.grid(column= 0, row = 3)

button5 = Button(alignFrame, text = "5",  command= lambda:numButton(button5)) 
themer(button5)
button5.grid(column= 1, row = 3)

button6 = Button(alignFrame, text = "6",  command= lambda:numButton(button6)) 
themer(button6)
button6.grid(column= 2, row = 3)

button1 = Button(alignFrame, text = "1",  command= lambda:numButton(button1)) 
themer(button1)
button1.grid(column= 0, row = 4)

button2 = Button(alignFrame, text = "2",  command= lambda:numButton(button2)) 
themer(button2)
button2.grid(column= 1, row = 4)

button3 = Button(alignFrame, text = "3",  command= lambda:numButton(button3)) 
themer(button3)
button3.grid(column= 2, row = 4)

button0 = Button(alignFrame, text = "0",  command= lambda:numButton(button0)) 
themer(button0)
button0.grid(column= 0, row = 5)

buttonDot = Button(alignFrame, text = ".",  command= lambda:numButton(buttonDot)) 
themer(buttonDot)
buttonDot.grid(column= 1, row = 5)
#--------------------------------------------------------------------------------
#right side function buttons
buttonEquals = Button(alignFrame, text = "=",  command= lambda:equals()) 
buttonEquals.config(fg = currentTheme.fontColor ,bg = currentTheme.tertiaryColor)
themer(buttonEquals, color= False)
buttonEquals.grid(column= 2, row = 5)

buttonMult = Button(alignFrame, text = 'x',  command= lambda:setFunction(buttonMult)) 
themer(buttonMult)
buttonMult.grid(column = 3, row = 2)

buttonMinus = Button(alignFrame, text = '-',  command= lambda:setFunction(buttonMinus)) 
themer(buttonMinus)
buttonMinus.grid(column = 3, row = 3)

buttonPlus = Button(alignFrame, text = '+',  command= lambda:setFunction(buttonPlus)) 
themer(buttonPlus, size=False)
buttonPlus.config(width = 4, height = 5)
buttonPlus.grid(column = 3, row = 4, rowspan = 2)

window.mainloop()