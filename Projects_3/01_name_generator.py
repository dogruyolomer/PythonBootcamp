import random

def generateName():
    firstNames = ["Khaleesi", "Derek", "Elliot", "Alec", "Kyla", "Davis", "Tessa", "Alan", "Antonella"]
    lastNames = ["Powers", "Wolfe", "Waller", "Gallagher", "Barrett", "Beard", "Rasmussen", "Garcia"]
    return f'{random.choice(firstNames)} {random.choice(lastNames)}'

for i in range(5):
    print(generateName())