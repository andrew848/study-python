def isPositiveNumber(num):
    if not num.isdigit():
        print("only positive numbers")
        return 1
    elif int(num) < 0:
        print("only positive numbers")
        return 1
    return int(num)


l = isPositiveNumber(input("Enter your length here: "))
w = isPositiveNumber(input("Enter your width here: "))

char = str(input("Enter your character here: "))
for x in range(0, int(l)):
    for y in range(0, int(w)):
        if int(l) < 0:
            print('enter only positive numbers')
        if x == 0 or x == int(l) - 1 or y == 0 or y == int(w) - 1:
            print(end=char + " ")
        else:
            print(end="  ")

    print(" ")
