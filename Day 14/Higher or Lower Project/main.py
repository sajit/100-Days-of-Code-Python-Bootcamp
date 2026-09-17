from typing import Protocol

import random
from art import logo
from game_data import data
class HLService(Protocol):
    """
    An interface to get HL data
    """



    def generate_options(self) -> tuple:
        """
        Generate two random options from the dataset
        :return: A tuple containing two random entries from the dataset
        """
        ...
class LocalHLService:
    
    """
    A local implementation of HLService that uses a predefined dataset.
    """

    def __init__(self):
        self.data = data


    def generate_options(self) -> tuple:
        option1 = random.choice(self.data)
        option2 = random.choice(self.data)
        return option1, option2

def play_game(service: HLService):
    """
    Play the Higher or Lower game using the provided service to get data.
    :param service: An instance of HLService to fetch data
    """
    # Example usage of the service to get details for a specific name
    score = 0
    end_game = False
    while not end_game:
        a, b = service.generate_options()
        print(f"Who has more followers? A: {a['name']} or B: {b['name']}")
        user_guess = input("Type 'A' or 'B': ").strip().upper()
        if user_guess == 'A':
            if a['follower_count'] > b['follower_count']:
                score += 1
                print(f"Correct! Your score is {score}.")
            else:
                end_game = True
        elif user_guess == 'B':
            if b['follower_count'] > a['follower_count']:
                score += 1
                print(f"Correct! Your score is {score}.")
            else:
                end_game = True
        else:
            print("Invalid input. Please type 'A' or 'B'.")
        print(f"A: {a['name']}, Followers: {a['follower_count']}")
        print(f"B: {b['name']}, Followers: {b['follower_count']}")
    print(f"Wrong! Your final score is {score}.")


play_game(LocalHLService())

    
