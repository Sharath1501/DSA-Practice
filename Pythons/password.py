import re

def password(words):
    if len(words)<6 or len(words)>12:
        return False
    if not re.search(r'[a-z]',words):
        return False
    if not re.search(r'[A-Z]',words):
        return False
    if not re.search(r'[0-9]',words):
        return False
    if not re.search(r'[@#$]',words):
        return False
    return True    
def mai():
    passw = input("Enter the password:: ")
    if password(passw):
        print("Password valid")
    else:
        print("Password is invalid. It must meet the following criteria:")
        print("- Contain at least 1 letter between a and z")
        print("- Contain at least 1 number between 0 and 9")
        print("- Contain at least 1 letter between A and Z")
        print("- Contain at least 1 character from $, #, @")
        print("- Minimum length of password: 6")
        print("- Maximum length of password: 12")

mai()