cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo

print(logo)
def deal_card():
    """Returns a random card from the deck."""
    import random
    return random.choice(cards)

def is_blackjack(hand):
    """Returns True if the hand is a blackjack, False otherwise."""
    return sum(hand) == 21 and len(hand) == 2

def calculate_score(hand):
    total = sum(hand)

    for card in hand:
         if card == 11 and total > 21:
             total -= 10 
                     
    return total

def play_game():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    if is_blackjack(computer_cards):
        print(f"Computer has a blackjack! {computer_cards} You lose.")
        return

    if is_blackjack(user_cards):
        print(f"You have a blackjack! {user_cards} You win.")
        return 
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    draw_or_pass = 'y'
    while draw_or_pass == 'y':
        draw_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_or_pass == 'n':
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
        else:
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}")
            if user_score > 21:
                  print(f"You went over. {user_score} You lose.")
                  return
                
                        
    print("Final Results")
    print(f"Your cards: {user_cards}")
    print(f"Computer's cards: {computer_cards}")    
    if computer_score > user_score and computer_score <= 21:
        print(f"Computer's cards: {computer_cards} Computer wins.")
    elif computer_score < user_score and user_score <= 21:
        print(f"Computer's cards: {computer_cards} You win.")
    else:
        print(f"Computer's cards: {computer_cards} It's a draw.")
        

print("Welcome to Blackjack!!")
play_game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play_game_choice == 'y':
    print("\n" * 100)
    play_game()
    play_game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


