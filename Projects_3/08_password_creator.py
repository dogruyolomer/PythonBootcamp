import random
import string

def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars = "{chars}{string.digits}"
    if level > 2:
        chars = "{chars}{punctuation}"
    
    for i in range(length):
        output.append(random.choice(chars))
    
    return "".join(output)

print("Password Generator")

password_length = int(input("Length: "))
password_level = int(input("Level: "))

password = generate_password(password_length, password_level)
print(f'\nYour password is: {password}')