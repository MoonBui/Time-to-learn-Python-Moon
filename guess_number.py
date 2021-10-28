import random

number = random.randint(1, 10)
condition = True

while condition:
    userGuess = input("Guess the number between 1 and 10: ")
    if int(userGuess) > number:
        print("Too high! Guess again!")
    elif int(userGuess) < number:
        print("Too low! Guess again")
    else:
        print("You got it, the correct answer is " + userGuess)
        condition = False