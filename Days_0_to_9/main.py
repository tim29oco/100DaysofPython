from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

bids = {}
game_continues = True

print(logo)
print("Welcome to the secret auction program.")

while game_continues:
  name = input("What is your name?\n")
  bid = int(input("What is your bid amount?\n"))
  bids[name] = bid
  
  more_players = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if more_players == 'no':
    game_continues = False
  clear()
    
max_bid = 0
max_key = None

for name, bid in bids.items():
  if bid > max_bid:
    max_bid = bid
    winner = name
print(f"The winner is {winner} with a bid of ${max_bid}.")
    
    
  
  