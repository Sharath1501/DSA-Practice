def check(inputstr):
    vowel = "aeiouAEIOU"
    result = ""
    for char in inputstr:
        if not  char in vowel:
            result +=char
    return result
inputstr = input("Enter the sentence:")
ink = check(inputstr)
print(ink)