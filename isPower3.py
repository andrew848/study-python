def cuberoot(x):
    a = abs(x)
    b = a**(1/3)
    if b.is_integer():
        cube = int(a**(1/3))

        return cube
    else:
        return 0


print(cuberoot(10))
print(cuberoot(1))
print(cuberoot(8))
print(cuberoot(256))

