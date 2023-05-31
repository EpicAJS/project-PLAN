from tkinter import *
import tkinter as tk
import array as ary
import math

# initializes variables
sum = 0
num1 = 0
num2 = 0
result = 0


def button_click(x):
    numWindow['text'] = numWindow['text'] + str(x)


def clearInput():
    numWindow['text'] = ""

    # Gets the number typed, and clears the calculator and selects the operator


def getFirstNum(operator):
    global OPERATOR
    OPERATOR = operator
    if (OPERATOR == "+"):
        bAdd.configure(bg="black", fg="white")
    elif (OPERATOR == "-"):
        bSub.configure(bg="black", fg="white")
    elif (OPERATOR == "*"):
        bMul.configure(bg="black", fg="white")
    elif (OPERATOR == "/"):
        bDiv.configure(bg="black", fg="white")
    elif (OPERATOR == "root"):
        bRoot.configure(bg="black", fg="white")
    elif (OPERATOR == "sqr"):
        bExp.configure(bg="black", fg="white")
    elif (OPERATOR == "equals"):
        bEquals.configure(bg="black", fg="white")

    if (numWindow['text'] != ""):
        num1 = float(numWindow['text'])
    else:
        numWindow['text'] = "select first number"
    global num_1
    num_1 = float(num1)
    clearInput()


# applies the operators and their functions into the math equation
def basicOperation():
    global result
    if (OPERATOR == "+" or OPERATOR == "-" or OPERATOR == "*" or OPERATOR == "/"):
        num2 = float(numWindow['text'])
        clearInput()
        if (OPERATOR == "+"):
            bAdd.configure(fg="black", bg=operatorColor)
            result = num_1 + num2
            numWindow['text'] = str(result)
        elif (OPERATOR == "-"):
            bSub.configure(fg="black", bg=operatorColor)
            result = num_1 - num2
            numWindow['text'] = str(result)
        elif (OPERATOR == "*"):
            bMul.configure(fg="black", bg=operatorColor)
            result = num_1 * num2
            numWindow['text'] = str(result)
        elif (OPERATOR == "/"):
            bDiv.configure(fg="black", bg=operatorColor)
            result = num_1 / num2
            numWindow['text'] = str(result)
    else:
        if (OPERATOR == "sqr"):
            bExp.configure(fg="black", bg=operatorColor)
            result = num_1 * num_1
            numWindow['text'] = str(result)
        elif (OPERATOR == "root"):
            bRoot.configure(fg="black", bg=operatorColor)
            result = math.sqrt(num_1)
            numWindow['text'] = str(result)


def changeBG():
    window.configure(background=changeBgColorEntry.get())

    # gets the buttons in the calculator and gives an option to change their colors from within the calculator


def changeButtonColor():
    global buttonColor
    buttonColor = changeButtonColorEntry.get()
    b1.configure(bg=buttonColor)
    b2.configure(bg=buttonColor)
    b3.configure(bg=buttonColor)
    b4.configure(bg=buttonColor)
    b5.configure(bg=buttonColor)
    b6.configure(bg=buttonColor)
    b7.configure(bg=buttonColor)
    b8.configure(bg=buttonColor)
    b9.configure(bg=buttonColor)
    b0.configure(bg=buttonColor)

    # gets the operator buttons and allows you to change their color from within the calculator


def changeOperatorColor():
    global operatorColor
    operatorColor = changeOperatorColorEntry.get()
    bPeriod.configure(bg=operatorColor)
    bEquals.configure(bg=operatorColor)
    bRoot.configure(bg=operatorColor)
    bExp.configure(bg=operatorColor)
    bClear.configure(bg=operatorColor)
    bAdd.configure(bg=operatorColor)
    bSub.configure(bg=operatorColor)
    bMul.configure(bg=operatorColor)
    bDiv.configure(bg=operatorColor)


# makes it able to change the background color from within
window = Tk()
window.title("Calculator")
window.geometry('225x400')

window.configure(background="white")
buttonColor = "white"


# gives the instructions to use the calculator
def open_popup():
    top = Toplevel(window)
    top.geometry("550x250")
    top.title("Instructions")
    i1 = Label(top, text="First Customize your Calculator Colors", font=('Mistral 18 bold'))
    i1.place(x=5, y=50)
    i2 = Label(top, text="Enter the first number using buttons", font=('Mistral 18 bold'))
    i2.place(x=5, y=80)
    i3 = Label(top, text="Click on operator", font=('Mistral 18 bold'))
    i3.place(x=5, y=110)
    i3 = Label(top, text="Enter second number and click =", font=('Mistral 18 bold'))
    i3.place(x=5, y=140)
    i4 = Label(top, text="Click CLEAR and Repeat", font=('Mistral 18 bold'))
    i4.place(x=5, y=170)


# Code that creates and initializes the buttons and operators
b1 = Button(window, text="1", width=3, command=lambda: button_click(1))
b1.grid(row=1, column=0)

b2 = Button(window, text="2", width=3, command=lambda: button_click(2))
b2.grid(row=1, column=1)

b3 = Button(window, text="3", width=3, command=lambda: button_click(3))
b3.grid(row=1, column=2)

b4 = Button(window, text="4", width=3, command=lambda: button_click(4))
b4.grid(row=2, column=0)

b5 = Button(window, text="5", width=3, command=lambda: button_click(5))
b5.grid(row=2, column=1)

b6 = Button(window, text="6", width=3, command=lambda: button_click(6))
b6.grid(row=2, column=2)

b7 = Button(window, text="7", width=3, command=lambda: button_click(7))
b7.grid(row=3, column=0)

b8 = Button(window, text="8", width=3, command=lambda: button_click(8))
b8.grid(row=3, column=1)

b9 = Button(window, text="9", width=3, command=lambda: button_click(9))
b9.grid(row=3, column=2)

bPeriod = Button(window, text=".", width=3, command=lambda: button_click("."))
bPeriod.grid(row=4, column=0)

b0 = Button(window, text="0", width=3, command=lambda: button_click(0))
b0.grid(row=4, column=1)

bEquals = Button(window, text="=", width=3, command=basicOperation)
bEquals.grid(row=4, column=2)

bAdd = Button(window, text="+", width=3, command=lambda: getFirstNum("+"))
bAdd.grid(row=1, column=3)

bSub = Button(window, text="-", width=3, command=lambda: getFirstNum("-"))
bSub.grid(row=2, column=3)

bMul = Button(window, text="x", width=3, command=lambda: getFirstNum("*"))
bMul.grid(row=3, column=3)

bDiv = Button(window, text="÷", width=3, command=lambda: getFirstNum("/"))
bDiv.grid(row=4, column=3)

bRoot = Button(window, text="√", width=3, command=lambda: getFirstNum("root"))
bRoot.grid(row=5, column=0)

bExp = Button(window, text="x²", width=3, command=lambda: getFirstNum("sqr"))
bExp.grid(row=5, column=1)

bClear = Button(window, text="CLEAR", width=9, command=clearInput)
bClear.grid(row=5, column=2, columnspan=2)

# instructions on setting colors for the calculator
customizeColorMessage1 = Label(window, text="Customize background, number,")
customizeColorMessage1.place(x=5, y=255)

customizeColorMessage1 = Label(window, text="and operator colors below ↓↓↓")
customizeColorMessage1.place(x=5, y=275)

changeBgColorEntry = Entry(window, width=6, bg="white")
changeBgColorEntry.place(x=5, y=295)

submitBgColor = Button(window, text="Submit", width=3, command=changeBG)
submitBgColor.place(x=5, y=315)

changeButtonColorEntry = Entry(window, width=6, bg="white")
changeButtonColorEntry.place(x=65, y=295)

submitButtonColor = Button(window, text="Submit", width=3, command=changeButtonColor)
submitButtonColor.place(x=65, y=315)

changeOperatorColorEntry = Entry(window, width=6, bg="white")
changeOperatorColorEntry.place(x=125, y=295)

submitOperatorColor = Button(window, text="Submit", width=3, command=changeOperatorColor)
submitOperatorColor.place(x=125, y=315)

numWindow = Label(window, text="", width=20, height=2, font=10)
numWindow.place(x=5, y=205)

instructionButton = Button(window, text="Instructions!", width=10, command=open_popup)
instructionButton.grid(row=0, column=0, columnspan=2)

window.mainloop()

