# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

def password_validator(some_password: str) -> str:
    error_list = []
    if len(some_password) < 6 or len(some_password) > 10:
        error_list.append("Password must be between 6 and 10 characters")

    if not some_password.isalnum():
        error_list.append("Password must consist only of letters and digits")

    digit_counter = 0
    for item in password:
        if item.isnumeric():
            digit_counter += 1

    if digit_counter < 2:
        error_list.append("Password must have at least 2 digits")

    if not error_list:
        return "Password is valid"

    return "\n".join(error_list)


password = input()
print(password_validator(password))
