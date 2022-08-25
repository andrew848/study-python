def printTriangle(hypotneuse):
    for i in range(0, hypotneuse):
        for x in range(0, i+1):
            if x ==0 or x == i or i == hypotneuse-1:
                print('*', end=' ')
            else:
                print('a ', end=' ')
        print()


printTriangle(6)