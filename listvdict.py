fruits = ['Pear', "Apple", "Banana", "Orange"]
fruits.insert(1, "strawberry")
fruits2 = ['Watermelon', 'peach']
fruits.extend(fruits2)
fruits.sort()
fruits.sort(key=str.lower)
for a in fruits:
    if a == "Watermelon":
        print("I love " + a)
    else:
        print('I do not like ' +a)


car = {
    "brand": "acura",
    "color": "white",
    "year": 2016,
}
car["color"] = 'white'

car2 = car.copy()
car2.get('color')
car2['color'] = "red"
car2['year'] = 2005
print(car)
print(car2)