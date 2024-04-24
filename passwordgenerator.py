import re
import random
import string

def is_strong_password(password):
    # Define regex patterns to check if the password contains at least one uppercase letter,
    # one lowercase letter, one digit, and one special character.
    patterns = [r'[A-Z]', r'[a-z]', r'\d', r'[!@#$%^&*()]']
    
    # Check if the password satisfies all patterns
    if all(re.search(pattern, password) for pattern in patterns):
        return True
    return False

def generate_strong_password(length=10):
    # Generate a strong password with a combination of uppercase letters, lowercase letters,
    # digits, and special characters.
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def replace_letters_with_special_chars(password):
    # Define a dictionary to map letters to similar special characters
    char_map = {
        'a': '@', 'A': '@',
        'e': '3', 'E': '3',
        'i': '!', 'I': '!',
        'o': '0', 'O': '0',
        's': '$', 'S': '$'
    }
    
    # Replace letters in the password with similar special characters
    new_password = ''.join(char_map[char] if char in char_map else char for char in password)
    return new_password

def password_checker():
    print("Welcome to the Password Checker & Generator!")
    while True:
        choice = input("Do you want to check a password or generate a new one? (check/generate/exit): ").strip().lower()
        
        if choice == "check":
            password = input("Enter the password to check: ")
            new_password = replace_letters_with_special_chars(password)
            print("Stronger version:", new_password)
        elif choice == "generate":
            length = int(input("Enter the length of the password to generate: "))
            new_password = generate_strong_password(length)
            print("Generated strong password:", new_password)
        elif choice == "exit":
            print("Exiting the Password Checker & Generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 'check', 'generate', or 'exit'.")

password_checker()
