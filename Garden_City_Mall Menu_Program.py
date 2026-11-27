# Project_3
# Countdown_Timer Project
import random

guess = input("Type your lucky number: ")

# Checking the number and converting it into integer
if guess.isdigit():
    guess = int(guess)
    if guess <= 0:
        print("Please try again using a number greater than 0")
        quit()
else:
    print("Please try using a number next time")
random_number  = random.randint(0, guess)

guesses = 0

while True:
    guesses += 1

    user_guess = input("Type your lucky number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please try again using a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

print("You got it in", guesses, "guesses!")










































































