def convertLength(length):
    a = length.lower()
    feet = 30.48
    if a.endswith('in'):
        new = a.strip('in')
        d = (float(new)/12)
        return d,'FT'
    elif a.endswith('ft'):
        new = a.strip('ft')
        c = (float(new) * feet)
        return c, 'CM'
    elif a.endswith('cm'):
        new = a.strip('cm')
        f = (float(new) / feet)
        return f, 'FT'


print(convertLength('10ft'))
print(convertLength('10cm'))
print(convertLength('123123cm'))
print(convertLength('10in'))