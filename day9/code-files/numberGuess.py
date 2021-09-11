import random

print("You have to guess a number between 1 and 100")

picked_level = input("choose difficulty level. 'easy' or 'hard': ").lower()
num_to_guess = random.randint(1, 100)
attempts_left = 10
attempts_took = 0
start_game = True

if picked_level == "easy":
    attempts_left = 10
elif picked_level == "hard":
    attempts_left = 5
else:
    start_game = False
    print("valid input expected")

if start_game:
    print(
        f"you choosed {picked_level} difficulty. You have {attempts_left} attempts left."
    )

    while attempts_left > 0:
        user_won = False
        guessed_number = int(input("guess the number: "))

        if guessed_number > num_to_guess:
            attempts_left -= 1
            attempts_took += 1
            print(f"guessed number is too large!")

        elif guessed_number < num_to_guess:
            attempts_left -= 1
            attempts_took += 1
            print(f"guessed nummber is too small!")

        elif guessed_number == num_to_guess:
            attempts_left = 0
            user_won = True
            print(
                f"\nyou guessed it right!\nThe num is {guessed_number}. \nYou guessed it in {attempts_took} attempts"
            )

        if attempts_left > 0:
            print(f"{attempts_left} attempts left\n")

        elif attempts_left == 0 and not user_won:
            print("you loose, no attemps left")
