import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_user_choice():
    return input("Choose Rock, Paper, or Scissors: ")


def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
        
    if (computer_choice == 'Rock' and user_choice == 'Paper') \
    or (computer_choice == 'Paper' and user_choice == 'Scissors'): 
        print("You won!")
        
    if (computer_choice == 'Rock' and user_choice == 'Scissors') \
    or (computer_choice == 'Paper' and user_choice == 'Rock'):
        print("You lost")

def play():
    get_winner(get_computer_choice(), get_user_choice())

play()
