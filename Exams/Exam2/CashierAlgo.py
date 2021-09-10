from timeit import default_timer as timer
from pprint import pprint
import tkinter
import random

def  formatInputs(total):
    total = str(total)
       
    if "." in total:
        total = int(float(total) * 100)
    return total

    
originalTotal = round(random.uniform(1, 50),2)
total = formatInputs(originalTotal)
print("Enter total:", "$" + str(originalTotal))

originalAmount = round(random.uniform(51, 100),2)
amount = formatInputs(originalAmount)
print("Enter change given: ", "$" + str(originalAmount))
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



