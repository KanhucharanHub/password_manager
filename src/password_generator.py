import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
def check_password_strength(password):
    length = len(password)
    if length < 8:
        return "Weak"
    if (any(char.islower() for char in password) and 
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in '!@#$%^&*()_+' for char in password)):
        return "Strong"
    return "Medium"
