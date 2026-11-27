# More Projects
import random

emojis = {"r": "😂"},{"s": "💲"}, {"p": "🤩"}
tries = ("r", "p","s")

def get_user_try():
    while True:
        user_try = input("Choose an option😂(r,p,s): ")

        if user_try in tries:
            return user_try
        else:
            print("Invalid attempt!")

def display_choices(user_try, comp_try):
    print(f"Your choice: {user_try}")
    print(f"Computer choice: {comp_try}")

def determine_winner(user_try, comp_try):
    if user_try == comp_try:
        print("It's a tie 😎")
    elif (
            (user_try == "r" and comp_try == "p") or
            (user_try == "s" and comp_try == "p") or
            (user_try == "r" and comp_try == "s")):
        print("You won✨✨✨")
    else:
        print("You tried😆")

def play_game():
    while True:
        user_try = get_user_try()
        comp_try = random.choice(tries)

        display_choices(user_try, comp_try)

        determine_winner(user_try, comp_try)

        try_again = input("Do you want to continue 😂😂(y/n)?: ")

        if try_again == "n":
            print("Thanks for playing😂😍✨")
            break
        elif try_again == "y":
            continue
        else:
            print("Invalid input! only y and n are allowed")

play_game()






















