l = int(input("Enter your length here: "))
w = int(input("Enter your width here: "))
for x in range(0, l):
    for y in range(0, w):
        if x == 0 or x == l-1 or y == 0 or y == w-1:
            print(end="* ")
        else:
            print(end="  ")

    print(" ")
