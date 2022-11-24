import random

def get_computer_choice():
    rps = ["Rock", "Paper", "Scissors"]
    choice = random.choice(rps)
    return choice

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ")
    return choice