from timeit import default_timer as timer
from pprint import pprint
import tkinter

def  formatInputs():
    total = input()
       
    if "$" in total:
        total = total.replace("$", "")
    if "." in total:
        total = int(float(total) * 100)
    return total

    
print("Enter total:")
total = formatInputs()
print("Enter change given: ")
amount = formatInputs()

change = total - amount

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

startTime = timer()




def getChange(change):
    if (change == 0):
        return
    for key in changeValues.keys():
        if (change >= key):
            
            changeAmount[changeValues[key]] += 1
            change -= key
            break
    getChange(change)
    
    
endTime = timer()

def print_inventory(dct):
    print("Change Amounts:")
    for item, amount in dct.items():
        print("{}: {}".format(item, amount))

getChange(amount - total)


print_inventory(changeAmount)



