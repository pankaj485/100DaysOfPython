from game_data import data
from replit import clear
import random

person_1 = random.choice(data)
score = 0


def play_game():
    # clear()
    global person_1, score
    person_2 = random.choice(data)

    if person_1["name"] == person_2["name"] or person_1[
            "follower_count"] == person_2["follower_count"]:
        person_2 = random.choice(data)

    def print_details(person):
        name = person["name"]
        followers = person["follower_count"]
        description = person["description"]
        country = person["country"]

        return f"{name}. {description} from {country} "

    def decide_winner(first_person, second_person):
        if first_person["follower_count"] > second_person["follower_count"]:
            winner = "a"
        elif first_person["follower_count"] < second_person["follower_count"]:
            winner = "b"
        return winner

    winner = decide_winner(person_1, person_2)

    print(print_details(person_1))
    print("       vs        ")
    print(print_details(person_2))

    user_ans = input("\nType 'a' or 'b' as your answer: ").lower()

    if user_ans == winner:
        if winner == "b":
            person_1 = person_2
        score += 1
        clear()
        play_game()
    else:
        print(f"you loose. You scored {score}")


play_game()
