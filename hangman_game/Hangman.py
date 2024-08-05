import hangman_art as A
from hangman_gane.Hangman_words import word_list
import random


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(A.logo)
display = []
found = False

for _ in range(word_length):
  display+= "_"

end_of_game = False
lives = 6


while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You ahve already guessed {guess}")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        found = True
  print(f"{' '.join(display)}")
  if not found:
    print(f"You guessed letter {guess}, that's not in the word ,You lose a life ")
    lives -= 1
    print(A.stages[lives])
  found = False
  if lives == 0:
    end_of_game = True
    print("You Lose")
  if '_' not in display:
    print("You win🏆")
    end_of_game = True

print("chosen word is", chosen_word)
