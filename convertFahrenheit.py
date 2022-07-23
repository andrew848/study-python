def convertTemp(temp):
    if temp.endswith('f'):
        new = temp.strip('f')
        c = (int(new) - 32) * 5 / 9
        msg = ('The converted temperature is', c, 'C')
        return msg
    elif temp.endswith('c'):
        new = temp.strip('c')
        f = (int(new) * 9 / 5 + 32)
        msg2 = ('The converted temperature is', f, 'F')
        return msg2


print(convertTemp('30c'))
print(convertTemp('310983c'))
print(convertTemp('100f'))
print(convertTemp('31983012f'))
