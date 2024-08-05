
from bidding_art import logo
print(logo)
def calc (bids):
  """  It calculates the bid amount and tells who is the winner
  """
  max = 0
  for i in bids:
    if int(bids[i])>max:
      max = int(bids[i])
      winner = i
  print(f"The winner is {winner} with a bid of ${max}")

bids={}
bidding_finished = False
while not bidding_finished:
  name = input("What is your name  ")
  bid = input("What is your bid $")
  bids[name]=bid
  should_continue = input("""Are there any other bidders? Type 'yes ' or 'no'.\n""")
  if should_continue == "yes":
    bidding_finished = False
  else:
    bidding_finished = True
calc(bids)