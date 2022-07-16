def sortChar(string):
    v = []
    c = []
    o = []
    n = []
    for x in string:
        if x.isdigit():
            n.append(x)
        elif not x.isalpha():
            o.append(x)
        elif x in "aeiouAEIOU":
            v.append(x)
        else:
            c.append(x)

    return [v,c,o,n]


print(sortChar('fkjdsffksd'))
print(sortChar('32392139384392'))
print(sortChar('abdbasdabd2312'))
print(sortChar('dakdaksjda!@!@!@'))
print(sortChar('jekejwqle@#@#@!#23123123'))



