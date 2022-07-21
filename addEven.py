def addEven(nums):
    result = 0
    for x in nums:
        if x % 2 == 0:
            result += x
    return result


numlist = [1, 2, 3, 4, 5, 6]
n = [5,44,2,423,4]
nu = [6,3242,42,45,5]
num = [1,1,1,1,1,1,1]

print(addEven(numlist))
print(addEven(n))
print(addEven(nu))
print(addEven(num))

