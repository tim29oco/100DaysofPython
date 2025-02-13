rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computerChoice = random.randint(0,2)
#User throws Rock
if user_choice == "0" and computerChoice == 0:
    print(f"You chose {rock} and the computer chose {rock}. It's a draw.")
elif user_choice == "0" and computerChoice == 1:
    print(f"You chose {rock} and the computer chose {paper}. You lose.")
elif user_choice == "0" and computerChoice == 2:
    print(f"You chose {rock} and the computer chose {scissors}. You win.")

#User Throws Paper
elif user_choice == "1" and computerChoice == 0:
    print(f"You chose {paper} and the computer chose {rock}. You win.")
elif user_choice =="1" and computerChoice == 1:
    print(f"You chose {paper} and the computer chose {paper}. It's a draw.")
elif user_choice == "1" and computerChoice == 2:
    print(f"You chose {paper} and the computer chose {scissors}. You lose.")

#User throws Scissors
elif user_choice == "2" and computerChoice == 0:
    print(f"You chose {scissors} and the computer chose {rock}. You lose.")
elif user_choice == "2" and computerChoice == 1:
    print(f"You chose {scissors} and the computer chose {paper}. You win.")
elif user_choice == "2" and computerChoice == 2:
    print(f"You chose {scissors} and the computer chose {scissors}. It's a draw.")
else: 
    print("You typed an invalid number, you lose!")
          
