# scissors paper rock project 
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
import random

user_input = input("pick your choice \"scissors\", \"paper\" or \"rock\": ")

system_choices = ["scissors", "paper", "rock"]
system_input = random.choice(system_choices)

if user_input == "scissors":
    print(scissors)
    if system_input == "scissors":
        print(scissors)
        print("Draw !!")
    elif system_input == "paper":
        print(paper)
        print("you won !")
    else:
        print(rock)
        print("you lost !")

elif user_input == "paper":
    print(paper)
    if system_input == "scissors":
        print(scissors)
        print("you lost !")
    elif system_input == "paper":
        print(paper)
        print("Draw !!")
    else:
        print(rock)
        print("you won !")

elif user_input == "rock":
    print(rock)
    if system_input == "scissors":
        print(scissors)
        print("you won !")
    elif system_input == "paper":
        print(paper)
        print("you lost !")
    else:
        print(rock)
        print("Draw !!")

else:
    print("wrong input !!")
