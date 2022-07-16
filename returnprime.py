def isPrime(num):
    isP = True
    for x in range(2, num):
        if num % x == 0:
            isP = False
            break
    return isP



userin = int(input("Enter a number here: "))
if isPrime(userin):
    print("the number is prime")
else:
    print("the number is not prime")
