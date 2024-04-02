import random

firstNumber, lastNumber = input("Enter the range of numbers you want to guess:").split()
print("First number is {} and second number is {}".format(firstNumber, lastNumber))
firstNumber = int(firstNumber) 
lastNumber = int(lastNumber)
guess = int
randomNumber = random.randint(firstNumber,lastNumber-1)
## print("random number is: ", randomNumber)

while guess != randomNumber :
    guess = int(input(f'Guess a number between {firstNumber} and {lastNumber}:'))
    if guess < randomNumber:
        print(f'{guess} is too LOW. Please guess again.')
    elif guess > randomNumber:
        print(f'{guess} is too HIGH. Please guess again.')
    else :
        print(f'Congrats! You have guessed the number {guess} correctly.')

