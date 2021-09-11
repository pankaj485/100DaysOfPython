import random

user_input = input("Heads or Tails ?")
decider = random.randint(0, 1)
computer_input = "Heads"

if decider == 1:
    computer_input = "Tails"

if (user_input == "Heads"):
    if user_input == computer_input:
        print("you won, that's Heads!")
    else:
        print("you loose, that was Tails!")
elif user_input == "Tails":
    if user_input == computer_input:
        print("you won, that's Tails!")
    else:
        print("you loose, that was Heads!")
else:
    print("wrong input, try again!")
