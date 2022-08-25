nums = {1: 'one ', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
on = {1: 'on my thumb',2: 'on my shoe', 3: 'on my knee', 4: 'on my door', 5: 'on my hive', 6: 'on my sticks', 7: 'up in heaven', 8: 'on my gate', 9: 'on my spine', 10: 'again'}


def ThisOldMan(played):
    verse = 'This old man, he played ' + played + ' He played ' + location + ' with a knick-knack paddywhack, Give the dog a bone, This old man came rolling home.'
    return verse


for i in range(1, 11):
    location = on[i]
    print(ThisOldMan(nums[i]))
