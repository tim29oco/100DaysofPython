import random

from replit import clear

from art import logo, vs
from game_data import data

#TODO

#Ensures B is not equal to A and ensures B != previous B
def generate_random_excluding(range_start, range_end, exclude_number, second_case_exclusion):
  while True:
    random_number = random.randint(range_start, range_end)
    if random_number != exclude_number and random_number != second_case_exclusion:
      return random_number

#Print Statements are Repetitive otherwise...
def printing(num, letter):
  print(
      f"Compare {letter}: \n\n{data[num]['name']}, a {data[num]['description']}, from {data[num]['country']} \nhint {data[num]['follower_count']}"
  )

def compare(num1, num2, guess):
  if data[num1]['follower_count'] > data[num2][
      'follower_count'] and guess == LETTER_A:
    return True
  elif data[num1]['follower_count'] < data[num2][
    'follower_count'] and guess == LETTER_B:
    return True
  else:
    return False


def game():
  print(logo)
  num1 = random.randint(0, len(data) - 1)
  num3 = -1
  game_continues = CONTINUE_GAME
  score = USER_SCORE
  
  while game_continues and score < 99:
    num2 = generate_random_excluding(0, len(data) - 1, num1, num3)
    printing(num1, LETTER_A)
    print(vs)
    printing(num2, LETTER_B)
    
    guess = input("\nWho has more followers? 'A' or 'B'?\n").upper()
    if compare(num1, num2, guess) and guess == LETTER_A:
      score += 1
      num3 = num2
      clear()
      print(f"{score}(S) POINTS on the board\n")
    elif compare(num1,num2,guess) and guess == LETTER_B:
      score += 1
      clear()
      num1 = num2
      print(f"{score}(S) POINTS on the board\n")
    else:
      print(f"You lost, and your score is {score}.")
      game_continues = False

USER_SCORE = 0
LETTER_A = 'A'
LETTER_B = 'B'
CONTINUE_GAME = True
play_again= True

while play_again:
  print(logo)
  choice = input("Would you like to start, 'Y' or 'N'\n").upper()
  if choice =='N':
    clear()
    play_again = False
    print("Goodbye")
  elif choice == 'Y':
    clear()
    game()
  else:
    clear()
    print("Unrecognized String\n")
