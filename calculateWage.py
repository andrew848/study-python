
def calculatePay(hours, wage):
    overtimehours = 0
    overtime = 0
    if hours > 20:
        overtime = wage*1.20
        overtimehours = hours-20
    pay = (hours-overtimehours)*wage
    overtimepay = overtimehours*overtime
    total = pay+overtimepay
    return total


print(calculatePay(24,6))