
import random

def choice():
    player_choice = input("Choose your option: 'rock', 'paper' or 'scissors' ")
    while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        player_choice = input("Invalid input. Try again: 'rock', 'paper' or 'scissors' ")
    bot_choice = ['rock', 'paper', 'scissors']
    bot_decision = random.choice(bot_choice)
    print("Bot has chosen", bot_decision)
    check()
    replay()

def check():
    if player_choice == bot_decision:
        print("Draw!")
    elif player_choice == "rock" and bot_decision == "scissors":
        print("Win!")
    elif player_choice == "scissors" and bot_decision == "paper":
        print("Win!")
    elif player_choice == "paper" and bot_decision == "rock":
        print("Win!")
    else:
        print("You lost.")

def replay():
    retry = input("Do you want to play again? Answer y/n")
    while retry != "y" and retry != "n":
        retry = input("Do you want to play again? Answer y/n")
    if retry == "y":
        choice()

player_choice = input("Choose your option: 'rock', 'paper' or 'scissors' ")

while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        player_choice = input("Invalid input. Try again: 'rock', 'paper' or 'scissors' ")
bot_choice = ['rock', 'paper', 'scissors']
bot_decision = random.choice(bot_choice)
print("Bot has chosen", bot_decision)
check()
replay()
