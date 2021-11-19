from re import match
from faker import Faker
from matplotlib import pyplot as plt

def probabilityOfSameBirthday(numPeople):
    if numPeople == 1:
        return 1
    else:
        return (365 - numPeople + 1) / 365 * probabilityOfSameBirthday(numPeople - 1)


def StoreBirthdays(fake, numPeople):
    fakeBirthdays = []
    fakeBirthdaysMatch = {}
    for i in range(numPeople):
        fakeBirthdays.append(fake.date()[5:])

    for birthday in fakeBirthdays:
        if birthday in fakeBirthdaysMatch:
            fakeBirthdaysMatch[birthday] += 1
        else:
            fakeBirthdaysMatch[birthday] = 1
    return fakeBirthdays,fakeBirthdaysMatch

def checkForMatches(fakeBirthdaysMatch):
    matches = 0
    for birthday in fakeBirthdaysMatch:
        if fakeBirthdaysMatch[birthday] > 1:
            print(birthday)
            matches += 1

def PlotProbability(probabilityOfSameBirthday):
    X = []
    Y = []
    for i in range(1, 90):
        X.append(i)
        Y.append(1 - probabilityOfSameBirthday(i))

    plt.scatter(X, Y, color='red')
    plt.xlabel("Number of people")
    plt.ylabel("Probability of the same birthday")
    plt.axis([0, 90, 0, 1])
    plt.show()



fake = Faker()

numPeople = int(input("How many people are in the room? "))
fakeBirthdays, fakeBirthdaysMatch = StoreBirthdays(fake, numPeople)

print("The probability of {} in a room having the same birthday is: {}".format(numPeople, 1 - probabilityOfSameBirthday(numPeople)))

checkForMatches(fakeBirthdaysMatch)

PlotProbability(probabilityOfSameBirthday)