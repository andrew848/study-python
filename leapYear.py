
def isLeapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


print(isLeapyear(2001))
print(isLeapyear(2024))
print(isLeapyear(2000))
print(isLeapyear(3000))
