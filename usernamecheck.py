def checkUser(username):
    if len(username) < 3:
        print("eeee")
        return False
    if not username.islower():
        return False
    hasDigital = 0
    for x in username:
        if not x.isalpha():
          if x.isdigit():
            hasDigital +=1
          else:
            return False
    print("xxxxxx")

    return hasDigital > 1



userinput = input("Enter a username here: ")
if checkUser(userinput):
    print("this username is valid")
else:
    print("this username is not valid")
