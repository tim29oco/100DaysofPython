import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = True

print("Welcome to Blackjack")
while continue_game:
    continue_rules = True
    user_response = input("Would you like to play? y/n\n")
    if user_response == 'n':
        continue_game = False
        continue_rules = False
    elif user_response == 'y':
        print("--Rules and Info--")
        print("1.) Get to 21 or as close as you can without going over")
        print("2.) The Deck is unlimited in size.")
        print("3.) The Jack/Queen/King all count as 10.")
        print("4.) The Ace can count as 11 or 1 for Player only.")
        print("5.) All cards have equal probability of being drawn.")
        print("6.) Computer will always hit if the sum of cards is <17.\n")
        while continue_rules:
            user_response = input("Would you still like to play?\n")
            if user_response == 'n':
                continue_rules = False
                continue_game = False
            elif user_response == 'y':
                new_card_loop = True
                player_cards = []
                computer_cards = []
                computer_cards.append(cards[random.randint(0, 12)])
                for _ in range(2):
                    player_cards.append(cards[random.randint(0,12)])
                #CHECK IF PLAYER GETS 21 TO BEGIN GAME
                if sum(player_cards) == 21:
                    print(player_cards)
                    print("YOU WIN!\n")
                    continue_rules = False
                #CHECKS TO SEE IF BOTH CARDS ARE 11
                elif sum(player_cards) == 22:
                    index_of_first_11 = player_cards.index(11)
                    player_cards[index_of_first_11] = 1
                else:
                    print(f"\n" * 10)
                    print("Fantastic! Let's begin.")
                    print(f"Your Cards {player_cards}\n")
                    print(f"Computer's Card {computer_cards}")

                    #ASK USER IF THEY WANT ANOTHER CARD
                    while new_card_loop:
                        user_response = input("Would you like another card? y/n\n")
                        #CASE WHEN USER SAYS NO
                        if user_response == 'n':
                            print("\n" * 10)
                            keep_dealing = True
                            while keep_dealing:
                                if sum(computer_cards) < 17:
                                    computer_cards.append(cards[random.randint(0,12)])
                                # IF CPU HAS 21
                                elif sum(computer_cards) == 21:
                                    print(f"CPU Wins {computer_cards}")
                                    print(sum(computer_cards))
                                    print(f"\nPlayer Loses {player_cards}")
                                    print(sum(player_cards))
                                    keep_dealing = False
                                    new_card_loop = False
                                    continue_rules = False
                                # IF CPU HAS >21
                                elif sum(computer_cards) > 21:
                                    print(f"CPU Loses {computer_cards}")
                                    print(sum(computer_cards))
                                    print(f"\nPlayer Wins {player_cards}")
                                    print(sum(player_cards))
                                    keep_dealing = False
                                    new_card_loop = False
                                    continue_rules = False
                                #WHICH TOTAL IS HIGHER?
                                elif sum(computer_cards) > sum(player_cards):
                                    print(f"CPU Wins {computer_cards}")
                                    print(sum(computer_cards))
                                    print(f"\nPlayer Loses {player_cards}")
                                    print(sum(player_cards))
                                    new_card_loop = False
                                    continue_rules = False
                                    keep_dealing = False
                                elif sum(computer_cards) < sum(player_cards):
                                    print(f"Player Wins {player_cards}")
                                    print(sum(player_cards))
                                    print(f"\nCPU Loses {computer_cards}")
                                    print(sum(computer_cards))
                                    keep_dealing = False
                                    new_card_loop = False
                                    continue_rules = False
                                else:
                                    print("Unique Case, Needs Fixing. Please Report")
                        # CASE WHEN USER SAYS YES
                        elif user_response == 'y':
                            player_cards.append(cards[random.randint(0, 12)])
                            count_11 = player_cards.count(11)
                            #PLAYER WINS == 21
                            if sum(player_cards) == 21:
                                print(f"CPU Loses {computer_cards}")
                                print(sum(computer_cards))
                                print(f"\nPlayer Wins {player_cards}")
                                print(sum(player_cards))
                                new_card_loop = False
                                continue_rules = False
                            #Changes ACE (11) to an ACE (1)
                            elif sum(player_cards) > 21 and count_11 >= 1:
                                index_of_first_11 = player_cards.index(11)
                                player_cards[index_of_first_11] = 1
                                print(player_cards)
                            #Player BUSTS >21
                            elif sum(player_cards) > 21:
                                print(f"CPU Wins {computer_cards}")
                                print(f"\nPlayer Busts {player_cards}")
                                print(sum(player_cards))
                                new_card_loop = False
                                continue_rules = False
                            elif sum(player_cards) < 21:
                                print(player_cards)
                                print(f"sum: {sum(player_cards)}")
                        else:
                            print("Invalid")
            else:
                print("Invalid!")
    else:
        print("Invalid!")
print("Goodbye.")