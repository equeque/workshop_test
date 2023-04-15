import datetime
from dateutil.relativedelta import relativedelta
import random


def game():
    print("Input 'play' to play a round, or input 'quit' to stop")

    player_decision = input()
    while player_decision != "play" and player_decision != "quit":
        print("Input 'play' to play a round, or input 'quit' to stop")
        player_decision = input()

    if player_decision == "play":
        player_choice = input("Choose your option: 'rock', 'paper' or 'scissors' ")
        while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
            player_choice = input("Invalid input. Try again: 'rock', 'paper' or 'scissors' ")
        bot_choice = ['rock', 'paper', 'scissors']
        bot_decision = random.choice(bot_choice)
        print("Bot has chosen", bot_decision)
        
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

        retry = input("Do you want to play again? Answer y/n")
        while retry != "y" and retry != "n":
            retry = input("Do you want to play again? Answer y/n")

        if retry == "y":
            game()


price=0
year = int(input('Enter your year of birth '))
month = int(input('Enter your month of birth '))
day = int(input('Enter you day of birth '))
date_of_birth = datetime.date(year, month, day)

now = datetime.datetime.now()
date_current = datetime.date.today()

customer_age = relativedelta(date_current, date_of_birth).years
print(customer_age)

pass_type = input("Which pass do you prefer? 'wkd' for Weekday pass or 'wknd' for Weekend pass")
while pass_type != "wkd" and pass_type != "wknd":
    pass_type = input("Invalid input. Please input 'wkd' or 'wknd'")

if pass_type == "wkd":
    if customer_age < 5:
        price = 30
    elif customer_age >= 5 and customer_age <= 50:
        price = 50
    else:
        price = 45

if pass_type =="wknd":
    if customer_age < 5:
        price = 40
    elif customer_age >= 5 and customer_age <= 50:
        price = 60
    else:
        price = 55

upgrade= input("Do you want to upgrade your ticket? Please input 'y' or 'n'")
while upgrade != "y" and upgrade != "n":
    upgrade = input("Invalid input.Please input 'y' or 'n'")
if upgrade == "y" and pass_type=="wkd":
    price = price+20
elif upgrade == "y" and pass_type == "wknd":
    price = price+30

print("Total cost of your ticket is: $", price)

current_month = date_current.month
present_list= ['Popcorn box', 'Lollypop', 'Fancy T-shirt', 'Free Lunch']
if month == current_month:
    present = random.choice(present_list)
    print("Congratulations! You have won: ", present)


print("Now you will face our AI in Rock, Paper, Scissors game!")
game()


