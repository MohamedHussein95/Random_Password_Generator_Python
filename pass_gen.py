import random
import string

print('*' * 15, 'Password Generator', '*' * 15)

while True:
    try:
        length = int(input('Enter the length of the password: '))
        include_upper_case_letters = input('Include Upper Case letters: "yes" or "no": ').lower()
        include_lower_case_letters = input('Include lower Case letters: "yes" or "no": ').lower()
        include_numbers = input('Include numbers: "yes" or "no": ').lower()
        include_symbols = input('Include Symbols: "yes" or "no": ').lower()
        break
    except ValueError:
        print('Invalid input! Please enter a valid number for the password length.')

password_characters = ''

if include_upper_case_letters == 'yes':
    password_characters += string.ascii_uppercase

if include_lower_case_letters == 'yes':
    password_characters += string.ascii_lowercase

if include_numbers == 'yes':
    password_characters += string.digits

if include_symbols == 'yes':
    password_characters += string.punctuation

if password_characters:
    password = ''.join(random.choice(password_characters) for _ in range(length))
    print('Generated Password:', password)
else:
    print('No character types selected. Unable to generate a password.')
