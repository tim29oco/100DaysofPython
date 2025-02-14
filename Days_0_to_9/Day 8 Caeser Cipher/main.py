from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

leave = False

def caeser(caeser_text, shift_amount):
    new_text = []
    new_letter = ''
    global leave
    for char in caeser_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'decode':
                new_position = (position - shift_amount) % 26
            elif direction == 'encode':
                new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            new_text.append(new_letter)
        else:
            new_text.append(char)
    new_text = ''.join(new_text)
    print(f"The {direction}d message is {new_text}")
    again = input("Would you like to go again? y or n\n").lower()
    if again == 'n':
        leave = True
        print("Goodbye\n")
    
print(logo)

while not leave:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(caeser_text = text, shift_amount = shift)
