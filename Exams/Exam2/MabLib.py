import tkinter
from tkinter.constants import BOTH, TOP, LEFT, RIGHT, INSERT
from unittest.mock import right
from tkinter import Text
changeAmount = {
    "twentyDollars" : 0,
    "tenDollars" : 0,
    "fiveDollars" : 0,
    "oneDollars" : 0,
    "quarters" : 0,
    "dimes" : 0,
    "nickels" : 0,
    "pennies" : 0
}

changeValues = {
     2000 :"twentyDollars",
     1000 :"tenDollars",
     500 :"fiveDollars",
     100 :"oneDollars",
     25 : "quarters",
     10 : "dimes",
     5 : "nickels",
     1 : "pennies",  
    }
window = tkinter.Tk()
greeting = tkinter.Label(text="Cashier's Algorithm", background = "red", foreground = "black")


greeting.pack()
tot = tkinter.StringVar(window)
totLabel = tkinter.Label(text="Enter total:")

totalEntry = tkinter.Entry(window)
amtLabel = tkinter.Label(text="Enter amount given:")
amountEntry = tkinter.Entry(window)

def getChangeAmount():
    total = totalEntry.get()
    if "$" in total:
        total = total.replace("$", "")
    total = int(float(total) * 100)
    
    amount = amountEntry.get()
    if "$" in amount:
        amount = amount.replace("$", "")
    amount = int(float(amount) * 100)
    change = int(amount - total)
    
    getChange(change)
result = Text(window)

def getChange(change):
    a = tkinter.Label()
    if (change == 0):
        a.destroy()
        for key, value in changeAmount.items():
            a = tkinter.Label(text = "{} : {}".format(key, value))
            a.pack()
            
        for key, value in changeAmount.items():
            changeAmount[key] = 0
        return
    for key in changeValues.keys():
        if (change >= key):
            
            changeAmount[changeValues[key]] += 1
            change -= key
            break
    getChange(change)
    

submit = tkinter.Button(window, text = "submit", command = getChangeAmount)
totLabel.pack() 
totalEntry.pack()
amtLabel.pack()
amountEntry.pack()
submit.pack()


window.mainloop()


