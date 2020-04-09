import re

def password_validation(password):

    if (len(password)>=6 and  (re.search("[a-z]", password)) and  (re.search("[A-Z]", password)) and  (re.search("[0-9]", password)) and  (re.search("[.@#$&*]", password))):
        return True
    else:
        return False


def main():
    print("The special character set can include { . @ #$ & * }")
    password = input("Enter a password you want to check: ")

    a = password_validation(password)

    if (a == True):
        print("Password is valid")
    else:
        print("Password is invalid")


if __name__ == "__main__":
    main()
