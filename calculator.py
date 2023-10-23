from tkinter import *

m = ""
def equals():
    global equationText
    
    try:
        total = str(eval(equationText))
        equationText = total
        equationLabel.set(equationText)
    except SyntaxError:
        equationLabel.set("syntax error")
    except ZeroDivisionError:
        equationLabel.set("zero division error")
    except ValueError:
        equationLabel.set("value error")
    except TypeError:
        equationLabel.set("type error")

def clear():
    global equationText
    equationLabel.set("")
    equationText = ""

def bcksp():
    global equationText
    equationText = equationText[:-1]
    equationLabel.set(equationText)


def buttonPress(num):
    global equationText
    equationText += str(num)
    equationLabel.set(equationText)


def sqrt():
    global equationText
    try:
        sqrt = float(equationText) ** 0.5
        equationText = str(sqrt)
        equationLabel.set(equationText)
    except ValueError:
        equationLabel.set("value error")

def percent():
    global equationText
    try:
        percent = int(equationText) / 100
        equationText = str(percent)
        equationLabel.set(equationText)
    except ValueError:
        equationLabel.set("value error")

def memoryLoad():
    global equationText
    global m

    if m != "":
        equationText = m
        equationLabel.set(equationText)
    else:
        equationLabel.set("memory empty")

def memorySave():
    global equationText
    global m
    m = equationText



window = Tk()
window.title("Python Calculator")
window.geometry("400x650")
window.resizable(False, False)
window.config(bg="#000000")

equationText = ""
equationLabel = StringVar()

label = Label(window, textvariable=equationLabel, font=('Calibri',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

class Buttons:

    button7 = Button(frame, text=7, width=7, height=4, font=35, command=lambda:buttonPress(7))
    button7.grid(row=0, column=0)

    button8 = Button(frame, text=8, width=7, height=4, font=35, command=lambda:buttonPress(8))
    button8.grid(row=0, column=1)

    button9 = Button(frame, text=9, width=7, height=4, font=35, command=lambda:buttonPress(9))
    button9.grid(row=0, column=2)

    button4 = Button(frame, text=4, width=7, height=4, font=35, command=lambda:buttonPress(4))
    button4.grid(row=1,column=0)

    button5 = Button(frame, text=5, width=7, height=4, font=35, command=lambda:buttonPress(5))
    button5.grid(row=1,column=1)

    button6 = Button(frame, text=6, width=7, height=4, font=35, command=lambda:buttonPress(6))
    button6.grid(row=1,column=2)

    button1 = Button(frame, text=1, width=7, height=4, font=35, command=lambda:buttonPress(1))
    button1.grid(row=2,column=0)

    button2 = Button(frame, text=2, width=7, height=4, font=35, command=lambda:buttonPress(2))
    button2.grid(row=2,column=1)

    button3 = Button(frame, text=3, width=7, height=4, font=35, command=lambda:buttonPress(3))
    button3.grid(row=2,column=2)

    button0 = Button(frame, text=0, width=7, height=4, font=35, command=lambda:buttonPress(0))
    button0.grid(row=3,column=0)

    buttonDec = Button(frame, text=".", width=7, height=4, font=35, command=lambda:buttonPress("."))
    buttonDec.grid(row=3,column=1)

    equalsBtn = Button(frame, text="=", width=7, height=4, font=100, command=equals)
    equalsBtn.grid(row=3,column=2)

    plusBtn = Button(frame, text="+", width=7, height=4, font=35, command=lambda:buttonPress("+"))
    plusBtn.grid(row=3,column=3)

    minusBtn = Button(frame, text="-", width=7, height=4, font=35, command=lambda:buttonPress("-"))
    minusBtn.grid(row=2,column=3)

    timesBtn = Button(frame, text="*", width=7, height=4, font=35, command=lambda:buttonPress("*"))
    timesBtn.grid(row=1,column=3)

    divBtn = Button(frame, text="/", width=7, height=4, font=35, command=lambda:buttonPress("/"))
    divBtn.grid(row=0,column=3)

    cBtn = Button(window, text="C", width=14, height=4, font=70, command=clear)
    cBtn.pack()

    bckspBtn = Button(window, text = "←", width = 14, height=4, font=70,command=bcksp)
    bckspBtn.pack()

    sqrtBtn = Button(frame, text = "√", width = 7, height=4, font=35, command=sqrt)
    sqrtBtn.grid(row=0, column=4)

    percBtn = Button(frame, text = "%", width=7, height=4, font=35, command=percent)
    percBtn.grid(row=1, column=4)

    bracket1Btn = Button(frame, text = "(", width=7, height=4,font=35, command= lambda:buttonPress("("))
    bracket1Btn.grid(row = 2, column=4)

    bracket2Btn = Button(frame, text = ")", width=7, height=4,font=35, command= lambda:buttonPress(")"))
    bracket2Btn.grid(row = 3, column=4)

    memoryLoadBtn = Button(frame, text = "ML", width=7, height=4, font=35, command=memoryLoad)
    memoryLoadBtn.grid(row=4,column=4)

    memorySaveBtn = Button(frame, text = "MS", width=7, height=4, font=35, command=memorySave)
    memorySaveBtn.grid(row=4,column=3)

    floor = Button(frame, text = "//", width=7, height=4, font=35, command=lambda: buttonPress("//"))
    floor.grid(row=4,column=2)

    power = Button(frame, text = "**", width=7, height=4, font=35, command=lambda: buttonPress("**"))
    power.grid(row=4,column=1)

    mod = Button(frame, text = "% (mod)", width=7, height=4, font=35, command=lambda: buttonPress("%"))
    mod.grid(row=4,column=0)

window.mainloop()