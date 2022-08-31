import argparse

parser = argparse.ArgumentParser(description='Rank a college')
parser.add_argument('college', type=str)
args = parser.parse_args()
colleges = {
            'princeton': 1,
            'harvard': 2,
            'mit': 3,
            'yale': 4,
            'stanford': 5,
            'uc': 6, 'up': 7,
            'cit': 8,
            'duke': 9,
            'jhu': 10,
            'nu': 11,
            'dartmouth': 12,
            'brown': 13,
            'vanderbilt': 14,
            'wu': 15,
            'cornell': 16,
            'rice': 17,
            'notre dame': 18,
            'ucla': 19,
            'emory': 20,
            'uc berkeley ': 21,
            'georgetown': 22,
            'um ann abror': 23,
            'carnegie': 24,
            'uv': 25,
            'usc': 26,
            'nyu': 27,
            'tufts': 28,
            'uc santa barbara': 28,
            'unc': 28,
            'wfu': 28,
            'ucsd': 29,
            'ur': 30,
}


def rankCollege(college):
    lower = college.lower()
    # if college.lower() == 'all':
    #     for i in colleges:
    #         print(rankCollege(i))
    if college not in colleges:
        msg = college + ' is out of range'
    else:
        msg = college.upper() + ' is ranked ' + str(colleges[lower]) + ' among all US colleges'
    return msg


def rankCollegeRecursively(college, msg):
    lower = college.lower()
    if lower not in colleges:
        if lower == 'all':
            for i in colleges:
                msg = msg + rankCollegeRecursively(i, msg) + '\n'
            return msg
        else:
            msg = college + ' is out of range'
    else:
        msg = college + ' is ranked ' + str(colleges[lower]) + ' among all US colleges'
    return msg


if args.college.lower() == 'all':
    for i in colleges:
        print(rankCollege(i))
