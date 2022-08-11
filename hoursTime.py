import math
def hoursTime(hours):
    hour = math.floor(hours/1)
    minute = math.floor((hours-hour)*60)
    second = math.floor((((hours-hour)*60)-minute)*60)
    return str(hour)+'hours '+str(minute)+'minutes '+str(second)+'seconds'

print(hoursTime(12.89))
