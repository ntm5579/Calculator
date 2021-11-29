#theming stuff--------------------------------------------------------------
class Theme():
    def __init__(self, font = 'black', button = 'white', bg = 'lightgray', second = 'white', third =  'white'):
        self.fontColor = font
        self.buttonColor = button
        self.bgColor = bg
        self.secondaryColor = second
        self.tertiaryColor = third

themes = []
mainStandard = Theme('black', 'lightgray', 'dimgray', 'sandybrown', 'lightskyblue')
themes.append(mainStandard)
altStandard = Theme('white', 'slategray','lightgray', 'sandybrown', 'red')
themes.append(altStandard)
mainColorful = Theme('white', 'slategray', 'cornflowerblue', 'sandybrown', 'red')
themes.append(mainColorful)
altColorful = Theme('white', 'mediumslateblue', 'mediumspringgreen', 'cyan', '#89043D')
themes.append(altColorful)
neutral = Theme('saddlebrown', 'peachpuff', 'linen', 'darkturquoise', 'salmon')
themes.append(neutral)
grayscale = Theme()
themes.append(grayscale)

currentTheme = mainStandard
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
