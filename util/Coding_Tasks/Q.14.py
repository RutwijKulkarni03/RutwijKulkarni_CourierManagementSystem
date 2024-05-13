'''14. Password Generator: Create a function that generates secure passwords for courier system
accounts. Ensure the passwords contain a mix of uppercase letters, lowercase letters, numbers, and
special characters.'''

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
secure_password = generate_password()
print("Generated Password:", secure_password)
