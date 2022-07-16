def getFactors(num):
    factors = []
    for x in range(1, num + 1):
        if num % x == 0:


    return factors


num = int(input("Enter a number here: "))
print(getFactors(num))