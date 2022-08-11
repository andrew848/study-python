def calc(num,num2,operator):
    result = 0
    if operator.lower() == 'addition' or '+':
        result = num+num2
    elif operator.lower() == 'subtraction' or '-':
        result = num-num2
    elif operator.lower() == 'multiplication' or '*':
        result = num*num2
    elif operator.lower() == 'division' or '/':
        result = num/num2
    elif operator.lower() == 'modulus' or '%':
        result = num%num2
    return result

print(calc(4,8,'division'))
print(calc(5,0,'division'))
print(calc(312,8,'multiplication'))
print(calc(4,4132,'addition'))