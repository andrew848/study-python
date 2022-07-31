def convertTemp(temp):
    a = temp.lower()
    if a.endswith('f'):
        new = a.strip('f')
        c = (float(new) - 32) * 5 / 9
        return c, 'C'
    elif a.endswith('c'):
        new = a.strip('c')
        f = (float(new) * 9 / 5 + 32)
        return f, 'F'


values = ('10f', '20c', '30F', '40C', '0f', '0C', '-10f', '-20C', '104f', '98f', '100.4f')
for v in values:
    converted = convertTemp(v)
    print(f'Converted {v} -> {converted}')

# print('The original temperature is 310f, The converted temperature is', convertTemp('310f'))
# print('The original temperature is 1f, The converted temperature is', convertTemp('1c'))
# print('The original temperature is -100f, The converted temperature is', convertTemp('-100f'))
