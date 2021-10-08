import math
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
def isNumberPrime(testNumber):

    for i in range(2, int(math.sqrt(testNumber)+1)):
        if (testNumber % i == 0):
            isPrime = False
            return isPrime
        else:
            isPrime = True

    return True



def amountOfPrimes(num):
    count = 0
    start = time.time()
    for i in range(2,num):
        if isNumberPrime(i):

            count +=1
    end = time.time()
    print("To check for the amount of primes under {}, it took {}".format(num,end-start))
    return count


numsToCheck = [10, 100, 1000, 10000, 100000, 1000000]




y = [amountOfPrimes(10), amountOfPrimes(100), amountOfPrimes(1000), amountOfPrimes(10000), amountOfPrimes(100000), amountOfPrimes(1000000)]

for i in range (0, len(numsToCheck)):
    print("The amount of primes under {} is: {}".format(numsToCheck[i], y[i]))

plt.xlabel('Range')
plt.ylabel('Amount of primes')
plt.step(numsToCheck, y)

plt.show()