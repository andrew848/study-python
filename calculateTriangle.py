def findPerimeter(a,b,c):
    if a+b < c or a+c<b or b + c < a or a*b*c == 0:
        return 0
    else:
        perimeter = a + b + c
    return perimeter

print(findPerimeter(1,2,3))
print(findPerimeter(0,1,3))