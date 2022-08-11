def areaFromRadius(radius):
    area = radius*radius*3.14
    return area

def areaRadius(circumference):
    radius = circumference/6.28
    return areaFromRadius(radius)
def findArea(circumference1, circumference2):
    x = areaRadius(circumference1)
    y = areaRadius(circumference2)
    finalarea = x-y
    return finalarea
def findSquare(length):
    squarearea = length*length
    return squarearea-areaRadius(length/2)

print(findSquare(10))
print(findArea(10,8))
