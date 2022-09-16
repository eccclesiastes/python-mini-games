# Rock, paper, scissors

# Importing required packages

import random

# Defining all valid options

options=["rock", "paper", "scissors"]

# Asking for user choice

userOption=input("Rock, paper or scissors? ")

# Computer choice

randomNumber=random.randint(0, 2)

computerOption=options[randomNumber]

# Ends game if user choice isn't in options

if userOption not in options:
    print("Please choose either 'rock', 'paper' or 'scissors' next time!")
    exit()

# Ends game if both choices are the same

if computerOption == userOption: 
    print("Draw!")
    exit()

# Decides who wins

if computerOption == "rock" and userOption == "paper" or computerOption == "scissors" and userOption == "rock" or computerOption == "paper" and userOption == "scissors":
    print("User wins! The computer picked", computerOption + ".")
else: 
    print("Computer wins! The computer picked", computerOption + ".")