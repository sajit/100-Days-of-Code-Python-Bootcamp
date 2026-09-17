import random
def play_game(mode):
    max_attempts = 0
    if mode == "easy":
        max_attempts = 10
    elif mode == "hard":
        max_attempts = 5
        # Implement hard mode logic here
    else:
        print("Invalid mode selected. Please choose 'easy' or 'hard'. No attempts")
    attempts = 0
    number = random.randint(1, 100)
    while attempts < max_attempts:
        guess = int(input("Make a guess for a number between 1 and 100: "))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number}.")
            break
        print(f"You have {max_attempts - attempts - 1} attempts remaining to guess the number.")
        attempts += 1
        if attempts < max_attempts:
            print("Guess again.")
        else:
            print(f"You've run out of guesses. The answer was {number}.")

game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
play_game(game_mode)