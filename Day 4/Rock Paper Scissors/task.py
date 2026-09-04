import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

guess = input('Enter your choice: ')
options = ['rock', 'paper', 'scissors']
computer = random.choice(options)

print(f"You chose: {guess}. Computer chose: {computer}")
if computer == 'rock':
    if guess == 'rock':
        print('Draw')
    elif guess == 'paper':
        print('You win')
    else:
        print('You lose')

if computer == 'paper':
    if guess == 'paper':
        print('Draw')
    elif guess == 'scissors':
        print('You win')
    else:
        print('You lose')

if computer == 'scissors':
    if guess == 'scissors':
        print('Draw')
    elif guess == 'rock':
        print('You win')
    else:
        print('You lose')