
def isLeapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


print(isLeapyear(2001))
print(isLeapyear(2024))
print(isLeapyear(2000))
print(isLeapyear(3000))


def lastLeapyear(years):
    leapyear = []
    currentyear = 2020
    for x in range(currentyear-years, currentyear+1):
        if isLeapyear(x):
            leapyear.append(x)
    return leapyear

print(lastLeapyear(12))
print(lastLeapyear(0))
print(lastLeapyear(4))
print(lastLeapyear(100))
print(lastLeapyear(-10))

