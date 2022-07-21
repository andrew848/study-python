def findSmallest(numList):
    odds = []
    for x in numList:
        if not x % 2 == 0:
            odds.append(x)
    odds.sort()
    return odds[0]


def smallestOdd(numlist):
    small = 0
    for x in (numlist):
        if not x % 2 == 0:
            if x<small or small == 0:
                small = x
    return small

def smallestEven(numlist):
    smal = 1
    for x in numlist:
        if x % 2 == 0:
            if x<smal or smal == 1:
                smal = x
    return smal
numList = [0,-2, 3, 4, 5, 9, ]
num2 = [2,3,45,1,3]
print(smallestEven(numList))
test = findSmallest(numList)
print(test)
print(smallestOdd(numList))
print(findSmallest(num2))
print(smallestOdd(num2))
print(smallestEven(num2))

