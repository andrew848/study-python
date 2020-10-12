#!/usr/bin/python3
currentSum = 0
while True:
    num = input('Enter a number here: ')
    try:
        num = float(num)
    except:
        continue
    currentSum += num
    print(f'Your current sum is {currentSum}')