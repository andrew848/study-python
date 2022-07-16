def rateTemp(temp):
    if temp < 0:
        return 'Extremely Cold'
    elif 0 < temp < 20:
        return 'Very cold'
    elif 20 < temp < 40:
        return 'Cold'
    elif 40 < temp < 60:
        return 'Cool'
    elif 60 < temp < 80:
        return 'Warm'
    elif 80 < temp < 100:
        return 'Hot'
    elif 100 < temp < 120:
        return 'Very hot'
    else:
        return 'Extremely hot'


temp = float(input("Enter your temperature here: "))
print(rateTemp(temp))