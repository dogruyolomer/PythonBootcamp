import random

user = input("'r' for rock, 's' for scissors, 'p' for paper")    
computer = random.choice(['r', 'p', 's'])
if user == computer:
    print("its a tie. lets play again.")
    user = input("'r' for rock, 's' for scissors, 'p' for paper")
    computer = random.choice(['r', 'p', 's'])

if user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'r' and computer == 'p':
    print(f'computer selected {computer}, you win.')
else:
    print(f'computer selected {computer}, Computer wins.')