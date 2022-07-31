def perimeterArea(length, width, unit):
    area = length * width
    perimeter = 2 * (length + width)
    result = (area, 'squarex '+unit, perimeter, unit)

    return result


print(perimeterArea(10, 2, 'cm'))
print(perimeterArea(0, 2, 'inch'))
print(perimeterArea(40, 414, 'feet'))
print(perimeterArea(10312, 244, 'meters'))