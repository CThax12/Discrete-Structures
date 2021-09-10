sentence = input()
sentence = sentence.lower()
sentence = ''.join(sentence.split())
backwards = sentence[::-1]

if sentence == backwards:
    print("This is a palindrome")
else:
    print("Not a palindrome")


#Algorithm starts by taking the first index and the last index. They both work towards the middle
#until it can tell if it is an palindrome or not.
def isPalindrome(sentence):
    firstChar = 0
    lastChar = len(sentence) - 1
    while firstChar < lastChar:
        if (sentence[firstChar] != sentence[lastChar]):
            print("This is not a palindrome.")
            return False
        else:
            firstChar +=1
            lastChar -= 1
    print("This is a palindrome")
    return True

isPalindrome(sentence)
