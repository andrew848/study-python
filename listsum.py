def listsum(listofnum):
    for num in listofnum:
        num = int(num) + int(num)
    print(num)


while True:
    question = input('Enter a list here: ')
    t = question.split()
    listsum(question)
