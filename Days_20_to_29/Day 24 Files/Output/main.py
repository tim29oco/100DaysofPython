# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("../Input/Names/invited_names.txt", mode='r') as f:
    for name in f:
        revised = str(name.strip("\n"))
        with open("../Input/Letters/starting_letter.txt") as s_letter:
            letter_content = s_letter.read()
            revised_letter = letter_content.replace("[name]", revised)
            with open(f"ReadyToSend/letter_for_{revised}", mode='w') as r_letter:
                r_letter.write(revised_letter)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
