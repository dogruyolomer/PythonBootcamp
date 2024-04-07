print("Welcome to my Computer Quiz")

play = input("do you want to play?")

if play.lower() != "yes":
    quit()

print("Let's play: ")
score = 0

answer = input("What does CPU stands for?")
if answer.lower() == "central processing unit":
    score += 1
    print('Correct!')
else:
    print("Incorrect")

answer = input("What does GPU stands for?")
if answer.lower() == "graphics processing unit":
    score += 1
    print('Correct!')
else:
    print("Incorrect")

answer = input("What does RAM stans for?")
if answer.lower() == "random access memory":
    score += 1
    print('Correct!')
else:
    print("Incorrect")

answer = input("What does PSU stans for?")
if answer.lower() == "power supply":
    score += 1
    print('Correct!')
else:
    print("Incorrect")

print(f'You got {score} questions correct!')
print(f'You got %{(score/4)*100}')