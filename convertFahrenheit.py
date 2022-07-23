def convertTemp(temp):
    for x in temp:
        if 'f' in temp:
            new = temp.strip('f')
            c = (int(new) - 32) * 5 / 9
            return c, "C"
        elif 'c' in temp:
            new = temp.strip('c')
            f = (int(new) * 9 / 5 + 32)
            return f, "C"


print(convertTemp('30c'))
print(convertTemp('310983c'))
print(convertTemp('100f'))
print(convertTemp('31983012f'))
