def upperVowel(phrase):
    new = ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            new = new + letter.upper()
        else:
            new = new + letter.lower()
    return new


print(upperVowel('fuewfsdjfksdfjsdjfksdjfls'))
print(upperVowel('FSHJFJHDSFDHFDEWEQWEQWEQdjkdjk12'))
print(upperVowel('fmwfemwflmwelfmwefewf123'))
print(upperVowel('abcdefghijklmnopqrstuv'))

