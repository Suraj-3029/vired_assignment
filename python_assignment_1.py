#  In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength.
# ●       Implement a Python function called check_password_strength that takes a password string as input.
# ●       The function should check the password against the following criteria:
#   ○       Minimum length: The password should be at least 8 characters long.
#   ○       Contains both uppercase and lowercase letters.
#   ○       Contains at least one digit(0-9).
#   ○       Contains at least one special character (e.g., !, @ ,  # , $, %).
# ●       The function should return a boolean value indicating whether the password meets the criteria.
# ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
# ●       Provide appropriate feedback to the user based on the strength of the password.

def check_password_strength(input):
    # special character list
    special_char = ['.', '!', '@', '$', '%', '^', '&',
                    '(', ')', '{', '}', '[', ']', ':', ';', '<', '>', ',', '.', '?', '/', '~', '_', '+', '-', '=', '|', ]
    val = 5

    # check for minimum length of password is 8
    if len(input) < 8:
        print('length should be at least 8')
        val -= 1

    # check for atleast one digit in the password
    if not any(char.isdigit() for char in input):
        print('Password should have at least one numeral')
        val -= 1

    # check for atleast one upper character in the password
    if not any(char.isupper() for char in input):
        print('Password should have at least one uppercase letter')
        val -= 1

    # check for atleast one lower character in the password
    if not any(char.islower() for char in input):
        print('Password should have at least one lowercase letter')
        val -= 1

    # check for atleast one special character in the password
    if not any(char in special_char for char in input):
        print('Password should have at least one of the special symbols')
        val -= 1

    return f'your password stangth is {val}'


inputPass = input("Enter User name")
result = check_password_strength(inputPass)
print(result)
