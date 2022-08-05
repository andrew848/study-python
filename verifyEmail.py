def verifyEmail(email):
    invalid = '!~`#$%^&*()-+={[}]|\\:;"\'<,>?/ '
    email_parts = email.split("@")
    if len(email_parts) != 2:
        return False
    part1 = email_parts[0]
    part2 = email_parts[1]
    if len(part1) < 3:
        return False
    for char in part1:
        if char in invalid or char == '.':
            return False
    if len(part2) < 5:
        return False
    for char in part2:
        if char in invalid:
            return False
    if part2.startswith('.') or part2.endswith(".") or '.' not in part2:
        return False
    return True


print('Is this a valid email?',verifyEmail('fdsfsdfd'))
print('Is this a valid email?',verifyEmail('a.com'))
print('Is this a valid email?-Rest@gmail.co',verifyEmail('test@gmail.com'))
print('Is this a valid email?-Mycase_22@abc.com',verifyEmail('Mycase_22@abc.com'))
print('Is this a valid email?',verifyEmail('32313.312321com'))
print('Is this a valid email?-2Mycase_!2@abc.com',verifyEmail('!Mycase_22@abc.com'))



