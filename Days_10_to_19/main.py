from contextlib import nullcontext

from logo import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a Number between 1 and 100")

#Intialize Variables

keep_asking = True
num_of_guesses = 5
secret_number = 101

def stop_asking():
    secret_number = random.randint(1, 100)
    keep_asking = False
    return secret_number, keep_asking

def invalid_input(num_of_guesses):
    num_of_guesses -= 1
    print(f"{num_of_guesses} Lives Remaining\n")
    return num_of_guesses

def life_taken(num_of_guesses):
    num_of_guesses -= 1
    print(f"{num_of_guesses} Lives Remaining\n")
    if num_of_guesses == 0:
        print("You Died")
    return num_of_guesses

def too_low(num_of_guesses, guess):
    print(f"{guess} is too low.")
    return life_taken(num_of_guesses=num_of_guesses)

def too_high(num_of_guesses, guess):
    return life_taken(num_of_guesses=num_of_guesses)

#Choose Difficulty
while keep_asking:
    difficulty_rating = input("Choose a difficulty. Type 'easy' or 'hard'")
    if difficulty_rating.lower() == 'easy':
        num_of_guesses = 10
        secret_number, keep_asking = stop_asking()
    elif difficulty_rating.lower() == 'hard':
        num_of_guesses = 5
        secret_number, keep_asking = stop_asking()
    else:
        print("Please select Difficulty")

print(f"\n{secret_number} <-- Hint")
print(f"{num_of_guesses} Lives Remaining\n")

while num_of_guesses >= 1:
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == secret_number:
            print(f"Correct! {guess}")
            print(f"You Won with {num_of_guesses} Lives Remaining!")
            break
        elif guess > secret_number:
            num_of_guesses = too_high(num_of_guesses=num_of_guesses, guess=guess)
        elif guess < secret_number:
            num_of_guesses = too_low(num_of_guesses=num_of_guesses, guess=guess)
    else:
        num_of_guesses = invalid_input(num_of_guesses)




