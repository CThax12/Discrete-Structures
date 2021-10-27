import time

def iterativeFibonacci(terms):
    num1 = 0
    num2 = 1

    result = 0
    
    for i in range(2, terms+1):
        result = num1 + num2
        num1 = num2
        num2 = result
    
    return result

def recursiveFibonacci(terms):
    if terms <= 1:
        return terms
    else:
        return recursiveFibonacci(terms-1) + recursiveFibonacci(terms - 2)
terms = int(input("How many numbers? "))

iterativeStart = time.time()
print(iterativeFibonacci(terms))
iterativeEnd = time.time()
iterativeTime = iterativeEnd - iterativeStart
print("Time to calculate iteratively: " , iterativeTime)

recursiveStart = time.time()

print(recursiveFibonacci(terms))

recursiveEnd = time.time()
recursiveTime = recursiveEnd-recursiveStart

print("Time to calculate iteratively: " , iterativeTime)
print("Time to calculate recursively: " , recursiveTime)

if recursiveTime < iterativeTime:
    print("Recursion was faster by:", iterativeTime-recursiveTime)
else:
    print("Iteratively was faster by:", recursiveTime-iterativeTime)
