import random

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card == 'A':
            num_aces += 1
            value += 11
        elif card in ['K', 'Q', 'J']:
            value += 10
        else:
            value += int(card)

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def play_blackjack(balance):
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("WELCOME TO THE BLACKJACK GAME!")
    print(f"Player Hand: {player_hand}, Sum: {calculate_hand_value(player_hand)}")
    print(f"Dealer Hand: [X, {dealer_hand[1]}]")

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value == 21 and dealer_value <= 21:
        print("BLACKJACK! You won.")
        balance += bet

        return balance

    elif dealer_value == 21 and player_value <= 21:
        print("Dealer got BLACKJACK! You lost.")
        balance -= bet

        return balance

    else:
        while True:
            action = input("Press 'C' to request card, 'S' to stay also 'D' to doubled: ").upper()  # double çalışmadı

            if action == 'C':
                player_hand.append(deck.pop())
                player_value = calculate_hand_value(player_hand)
                print(f"Player Hand: {player_hand}, Sum: {player_value}")

                if player_value > 21:
                    print("The player hand exceeded 21. You lost!")
                    balance -= bet  # o
                    break
            elif action == 'S':
#dealer_value
                while dealer_value < 17:
                    dealer_hand.append(deck.pop())
                    dealer_value = calculate_hand_value(dealer_hand)
                print(f"Dealer Hand: {dealer_hand}, Sum: {dealer_value}")

                if dealer_value > 21 or player_value > dealer_value:
                    print("Congratulations, you won!")
                    balance += bet  #
                elif player_value == dealer_value:
                    print("Draw!")
                else:
                    print("Sorry, you lost!")
                    balance -= bet  #

                break
# double eklenecek alan
            elif action == 'D':
                player_hand.append(deck.pop())
                player_value = calculate_hand_value(player_hand)
                print(f"Player Hand: {player_hand}, Sum: {player_value}")

                if player_value > 21:
                    print("The player hand exceeded 21. You lost!")
                    balance -= bet*2  #
                    break

                while dealer_value < 17:
                    dealer_hand.append(deck.pop())
                    dealer_value = calculate_hand_value(dealer_hand)
                print(f"Dealer Hand: {dealer_hand}, Sum: {dealer_value}")
                if dealer_value > 21 or player_value > dealer_value:
                    print("Congratulations, you won!")
                    balance += bet*2
                elif player_value > 21:
                    print("The player hand exceeded 21. You lost!")
                    balance -= bet*2  #
                elif player_value == dealer_value:
                    print("Draw!")
                else:
                    print("Sorry, you lost!")
                    balance -= bet*2
                break
            else:
                print("Invalid input. Type 'C', 'S' or 'D'!")

        return balance

player_name = input("Username: ")
age = int(input("Age: "))
balance = 50  # Başlangıç bakiyesi
bet = 0
if age >= 18:
    while True:
        print(f"Current balance: ${balance}")
        play_again = input("Do you want to play a game? (Y/N): ").upper()
        if play_again == 'Y':
            bet = int(input("Bet:"))
            balance = play_blackjack(balance)
            if balance <= 0:
                print("You're out of money! Game over.")
                break
        elif play_again == 'N':
           print("Thanks for playing! Your final balance:", balance)
           if balance <= 100:
            print("Why did u come here?")
           elif balance > 100 and balance <= 200:
            print("You won the your taxi payment:D")
           elif balance > 200 and balance <= 400:
            print("You are lucky.")
           elif balance > 400 and balance <= 600:
            print("You should go to VEGASSSS!")
           elif balance > 600:
            print("Okey... I think you are a cheater. I am calling the police! :o")
            print("*********************************************************************************")
            print("- 9 1 1. What's your emergency?")
           break
        else:
             print("Invalid input. Type 'Y' or 'N'!")
elif age < 18:
  print("Get older, child!")