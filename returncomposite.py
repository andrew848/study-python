def isComposite(num):
    isC = False
    for x in range(2, num):
        if num % x == 0:
            isC = True
    return isC



userin = int(input("Enter a number here: "))
if isComposite(userin):
    print("The number is composite")
else:
    print("the number is prime")