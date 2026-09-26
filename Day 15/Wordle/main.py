from words import word_list
import random
import string

chosen = random.choice(word_list)
attempts = 0
guesses = []
chars_not_in_word = []

def process_guess(word):
    result = ""
    for i,w_char in enumerate(word):
        if w_char == chosen[i]:
            result += str(w_char).upper()
        elif w_char in chosen:
            result += w_char
        else:
            result += "_"
            chars_not_in_word.append(w_char)
    return result

def print_guesses(guess_list):
    for guess in guess_list:
        print(guess)

def print_chars():
    remaining = [letter for letter in string.ascii_lowercase if letter not in chars_not_in_word]
    print(f"Remaining chars {remaining}")
    print(f"Unused characters {chars_not_in_word}")

while attempts < 6:

    guess = input("Guess a word.\n")
    
    result = process_guess(guess)
    if result.lower() == chosen:
        print(f"You won. Word was {chosen}")
        exit(0)
    else:
        guesses.append(result)
        print_guesses(guesses)
        print_chars()
    attempts +=1 

print(f"Word was {chosen}")
exit(0)