import random
numberGeneratedByComputer = random.randint(1, 99)
chances = 0

while chances < 5:
    numberGuessedByUser = int(input("Guess an integer from 1 to 99: "))
    if numberGuessedByUser < numberGeneratedByComputer:
        print("the number is greater than your guess: ", numberGuessedByUser)
        chances = chances + 1
        
    elif numberGuessedByUser > numberGeneratedByComputer:
        print("the number is lower than your guess: ", numberGuessedByUser)
        chances = chances + 1
    
    elif numberGuessedByUser == numberGeneratedByComputer:
        print("you guessed it!")
        break
    else: 
        print(" ERROR! Please guess only numbers from 1 to 99!")

if not chances < 5:
    print("You Lose! The Correct Number Is ", numberGeneratedByComputer)
