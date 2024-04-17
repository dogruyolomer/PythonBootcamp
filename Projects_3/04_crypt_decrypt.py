def encrypt(text, value, output=""):
    for char in text:
        output = f'{output} {chr(ord(char) + value)}'
    return output

def decrypt(text, value, output=""):
    for char in text:
        output = f'{output} {chr(ord(char) - value)}'
    return output

i = int(input("Increment value:"))

text = input("Type your text: ")
print(f'Encrypted text: {encrypt(text,i)}')

text = input("Type for decyrpt:(without spaces) ")
print(f'Decrypted text: {decrypt(text,i)}')
