import random
from art import logo

print(logo)
print("Welcome to number Guessing game😁")
print("I'm thinking a number a between 1 and 100")
level = input("Choose a difficulty. Type easy or hard: ")
if level == "easy":
    trial = 10
else:
    trial = 5

print(f"You have {trial} attempts to guess a number")
guessed_number = random.randint(1, 100)

while trial > 0:
    no = int(input("Make a guess: "))
    if no == guessed_number:
        print("You win🏆")
        break
    else:
        trial -= 1
        if no < guessed_number:
            print("Too low")
        else:
            print("Too high")
        print(f"You have {trial} attempts to guess a number")

