def rateTemp(temp):
    if temp <= 0:
        return 'Extremely Cold'
    elif temp <= 20:
        return 'Very cold'
    elif temp <= 40:
        return 'Cold'
    elif temp <= 60:
        return 'Cool'
    elif temp <= 80:
        return 'Warm'
    elif temp <= 100:
        return 'Hot'
    elif temp <= 120:
        return 'Very hot'
    else:
        return 'Extremely hot'


temp = float(input("Enter your temperature here: "))
print(rateTemp(temp))