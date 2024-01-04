# Password strength checker
from re import search


# Opening text
print('Check Your Password Strength')
print('Good passwords contain a combination of UPPERCASE, lowercase, numbers, special characters, and are 12 characters or longer')
print()
password = input("What password do you want to check? ")

# Define password and calculate a score for each criteria
def check_password_strength(password):
    score = 0

    # Does the password contains at least one uppercase letter?
    if search(r'[A-Z]', password):
        score += 1
    
    # Does the password contains at least one lowercase letter?
    if search(r'[a-z]', password):
        score += 1
    
    # Does the password contains at least one special character?
    if search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Does the password contains at least one number?
    if search(r'\d', password):
        score += 1
    
    # Does the password has at least 12 characters?
    if len(password) > 11:
        score += 1

    return score

result = check_password_strength(password)

# assign a response for each score 
if result == 5:
    print("Password is very strong!")
    print('Good Job, beware of phishing attempts and consider adding 2FA')
elif result == 4:
    print('Password is okay, could be better.')
    print('Good passwords contain a combination of UPPERCASE, lowercase, numbers, special characters, and are 12 characters or longer')
elif result < 4:
    print('Password is weak. Try again.')
    print('Good passwords contain a combination of UPPERCASE, lowercase, numbers, special characters, and are 12 characters or longer')
