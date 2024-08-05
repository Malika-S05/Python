from random import choice
from asciiart import options, options_image, letter

score = 0
def calculate_score(user_guess, computer_choice):
    global score
    print("Your chose ", user_guess)
    print("Computer chose ", computer_choice)
    if user_guess == "rock":
       if user_guess == computer_choice:
            print("Match Draw ")
       elif computer_choice == 'scissors':
            print('You win.😁')
            score += 1
       else:
           print("Computer Won")
    elif user_guess == "paper":
       if user_guess == computer_choice:
           print("Match Draw ")
       elif computer_choice == 'scissors':
           print("Computer Won")
       else:
           print('You win.😁')
           score += 1
    else:
       if user_guess == computer_choice:
           print("Match Draw ")
       elif computer_choice == 'Rock':
           print("Computer Won")
       else:
           print('You win.😁')
           score += 1

is_on = True
score = 0
print(letter)

is_on = True
while is_on:
    user_guess = input("rock/paper/scissors ?").lower()
    computer_choice = choice(options)
    print("Computer choice :")
    print(options_image[computer_choice])
    print("Your choice :")
    print(options_image[user_guess])
    calculate_score(user_guess, computer_choice)
    continue_game = input("continue ??? Yes or No ").lower()
    if continue_game == "no":
        break

print("Score  :", score)
