import random

def get_computer_choice():
    rps = ["rock", "paper", "scissors"]
    choice = random.choice(rps)
    return choice

def get_user_choice():
    choice = input("Choose Paper, or Scissors: ")
    return choice



