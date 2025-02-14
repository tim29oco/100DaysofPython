import random
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
userLives = 6
guessedLetters = []

print(f'Here is the word {chosen_word}')
#Testing code
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#Observer Method
def emptySpace():
   return "_" in display

def noLives():
    return userLives == 0 

while emptySpace() and not noLives():
    guess = input("Guess a letter: ").lower()
    if guess in guessedLetters:
        print(f"You've already guessed {', '.join(guessedLetters)}")
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(' '.join(display))
    if guess not in chosen_word and guess not in guessedLetters:
        userLives -= 1
        print(stages[userLives])
        guessedLetters.append(guess)
    elif guess in chosen_word:
        guessedLetters.append(guess)
#Win or Lose Statement
if noLives():
    print("You lose")
elif not emptySpace():
    print("You win.")


