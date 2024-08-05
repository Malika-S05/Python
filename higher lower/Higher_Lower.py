from art import logo, vs
from random import choice
from game_data import data


def check(first,second):
  if first['follower_count'] > second['follower_count']:
    win = 'A'
  else:
    win = 'B'
  return win
def generaterandom():
  return choice(data)



def game():
  end_game = False
  score = 0
  first = generaterandom()
  second = generaterandom()
  while not end_game:
    print(logo)
    first = second
    second = generaterandom()
    while first == second:
      second = generaterandom()
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}.")
    print(vs)
    print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}.")
    test = input("Who has more followers? Type 'A' or 'B': ")
    win = check(first,second)
    if win == test:
      score += 1
      print(f"You're right! Current Score : {score}")
    else:
      end_game = True
      print(f"Sorry, that's wrong. Final score: {score}")

game()




