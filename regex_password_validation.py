
# use shebang as mentioned in gitpython.py

import re

# Its a good thing to create separate function for password validation
# TODO: naming could've been better. is_valid_password...
# by reading `is` we would get the insight that the function will return either true or false
def password_validation(password):

    # TODO : you are just return true if condition evaluates to true
    # one-liner
    # return (len(password)>=6 and  (re.search("[a-z]", password)) and  (re.search("[A-Z]", password)) and  (re.search("[0-9]", password)) and  (re.search("[.@#$&*]", password)))
    if (len(password)>=6 and  (re.search("[a-z]", password)) and  (re.search("[A-Z]", password)) and  (re.search("[0-9]", password)) and  (re.search("[.@#$&*]", password))):
        return True
    else:
        return False


def main():
    print("The special character set can include { . @ #$ & * }")
    # TODO: use getpass instead of input(), it does not echo the typed password
    # https://docs.python.org/2/library/getpass.html
    password = input("Enter a password you want to check: ")

    a = password_validation(password)

    if (a == True):
        print("Password is valid")
    else:
        # TODO: instead, you should've printed the valid password criteria. Makes more easy for user to get it correct next time
        # ie password should contain `at least one capital letter and so on`
        print("Password is invalid")


if __name__ == "__main__":
    main()
