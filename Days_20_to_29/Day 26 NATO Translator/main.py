import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter : row.code for (index, row) in data.iterrows()}
print(dict)

def generatephonetic():
    word = input("Say a word").upper()
    try:
        phonetic_list = [dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet (That means no spaces either)")
        generatephonetic()
    else:
        print(phonetic_list)

generatephonetic()
