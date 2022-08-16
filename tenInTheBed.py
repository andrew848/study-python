
nums = {2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}


def tenIntheBed(num):
    lyrics = 'There were '+ num + ' in the bed and the little one said, Roll over! Roll over! So they all rolled over and one fell out'
    return lyrics


for i in range(10, 1, -1):
    print(tenIntheBed(nums[i]))
print('There were one in the bed and the little one said, Alone at last! Good night!')