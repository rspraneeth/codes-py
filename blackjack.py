import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
play_again = True
while play_again:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    black_jack = 21

    def deal_card(deck):
        return deck[random.randint(0, len(deck) - 1)]

    def calculate_score(player_cards):
        if 11 in player_cards and sum(player_cards) > 21:
            player_cards.remove(11)
            player_cards.append(1)

        return sum(player_cards)

    def compare(u_score, c_score):
        if u_score == c_score:
            print("Draw")
        elif comp_score == 21:
            print("Dealer wins")
        elif user_score == 21:
            print("User wins")
        elif user_score > 21:
            print("Dealer wins")
        elif comp_score > 21:
            print("User wins")
        elif user_score > comp_score:
            print("User wins")
        elif comp_score > user_score:
            print("Dealer wins")

    user_cards = [deal_card(cards), deal_card(cards)]
    comp_cards = [deal_card(cards), deal_card(cards)]
    is_user_game_over = False
    is_comp_game_over = False
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)

    print(f"Your cards {user_cards}, your score is {user_score}")
    print(f"Dealers first card is {comp_cards[0]}")

    while not is_user_game_over:
        if comp_score == 21 or user_score == 21 or user_score > 21:
            compare(user_score, comp_score)
            is_comp_game_over = True
            is_user_game_over = True

        else:
            choice = input("Do you want to draw another card y/n: ").lower()
            if choice == 'y':
                user_cards.append(deal_card(cards))
                user_score = calculate_score(user_cards)
                print(f"Your cards {user_cards}, your score is {user_score}")

            elif choice == 'n':
                is_user_game_over = True

    while is_user_game_over and not is_comp_game_over:
        if comp_score == 21 or comp_score > 16:
            compare(user_score, comp_score)
            is_comp_game_over = True
        elif comp_score < 17:
            comp_cards.append(deal_card(cards))
            comp_score = calculate_score(comp_cards)

    print(f"Dealer cards are {comp_cards} and dealer score is {comp_score}")

    if input("Do you want to play again y/n: ").lower() == 'y':
        play_again = True
    else:
        play_again = False
