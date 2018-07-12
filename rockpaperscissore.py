# rock paper scissors
import random

while True:

    choices = ['rock','paper','scissors']
    print("Welcome to rock paper and scissors game:\n")
    user = input("Enter your choice among these\n 1. rock \n2. paper \n3. scissors\n ")
    bot = random.choice(choices)

    # print(bot)
    if user == 'rock' and bot == 'rock' or user == 'paper' and bot == 'paper' or user == 'scissors' and bot == 'scissors':
        print("Draw")
    elif user == 'rock' and bot == 'paper' or user == 'paper' and bot == 'scissors' or user == 'scissors' and bot == 'rock' :
        print("Bot wins and You Lose")
    elif bot == 'rock' and user == 'paper' or bot == 'paper' and user == 'scissors' or bot == 'scissors' and user == 'rock' :
        print("Bot lost and You Win")
    else :
        print("Wrong option detected... exiting program")
    break
