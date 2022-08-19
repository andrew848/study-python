nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


def FiveLittleducks(ducks):
    verse = ducks + ' little ducks went out one day, over the hills and far away. Mother duck said, "Quack, Quack, Quack, Quack" but only ' + remain + ' ducks came back.'
    return verse


for i in range(5, 0, -1):
    remain = i-1
    remain = nums[remain]
    print(FiveLittleducks(nums[i]))
print('Sad mother duck went out one day, over the hills and far away, Mother Duck said, “Quack, Quack, Quack, Quack,” and five little ducks came back.')

