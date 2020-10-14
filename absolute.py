import random

while True:
    randomnum = range(-100, 101)
    randomnum2 = random.choice(randomnum)
    expected = abs(randomnum2) * 2
    while True:
        actual = input(f'Enter the absolute value of {randomnum2} times two: ')
        if int(actual) == expected:
            print('You are correct')
            break
        else:
            print('Try again')
            continue