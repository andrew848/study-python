def findFactorial(num):
    factorial = 1
    for x in range(1, num+1):
        factorial = factorial*x 
    return factorial


print(findFactorial(8))
print(findFactorial(10))
print(findFactorial(-1))
print(findFactorial(0))
print(findFactorial(30))