#Write a program to count and print all the different ways
#there are to choose half a dozen donuts from
#3 varieties at a donut shop.
#Repeat the exercise for a full dozen with 21 varieties.


#https://byjus.com/maths/permutation-and-combination/


import itertools

def getDonutCombos(donuts, amount):
    return itertools.combinations_with_replacement(donuts, amount)


typesOfDonuts = ["Chocolate", "Strawberry", "Glazed", "Blueberry", "Powdered", "Bavarian Kreme", "Cinnamon", "Toasted Coconut",
"Jelly Stick", "Old Fashioned Cake", "Vanilla Frosted with Sprinkles", "Original Stick", "Boston Kreme", "Jelly", "Butternut",
"Double Chocolate", "Strawberry Frosted with Sprinkles", "Maple Frosted", "French Cruller","Choclate Stick","Glazed Stick"]

amountToChooseFrom = int(input("Enter the amount of donut types to choose from:" ))
donutsYouWant= int(input("Enter how many donuts you want: "))
if amountToChooseFrom > 21:
    print("Must be 1-21")
    amountToChooseFrom = int(input("Enter the amount of donuts:" ))

donutsInStock = typesOfDonuts[0:amountToChooseFrom]

donutCombos = list(getDonutCombos(donutsInStock, donutsYouWant))
print("There are {} combinations to choose from.".format(len(donutCombos)))
i = 1
for donuts in donutCombos:
    print("Combination {}: {}".format(i, donuts))
    print()
    i += 1


