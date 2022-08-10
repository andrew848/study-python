def decimalHours(time):
    measurements = time.split(':')
    hours = measurements[0]
    minutes = measurements[1]
    seconds = measurements[2]
    secondshours = int(seconds)/3600
    minuteshours = int(minutes)/60
    hours = int(hours)
    totalhours = hours+secondshours+minuteshours
    return totalhours

values = ('10:22:3', '10:0:0', '0:0:0', '12:59:59', '100:0:10')
for v in values:
    print(decimalHours(v))





