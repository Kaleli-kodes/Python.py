# Python quiz game
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "Which of the following elements it's a transition metal?: ",
             "How many planets are in the solar system?: ",
             "How many bones are in the human body?: ",
             "What is the hottest desert in the world?: ",)

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Oxygen","B. Sulphur","C. Magnesium","D. Uranium"),
           ("A. 5","B. 8","C. 9","D. 7"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Sahara","B. Kalahari","C. Lut","D. Namib"),)

answers = ("C", "D", "D", "B","A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    print("--------------------------------------------------------")
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,C,B,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"Please try again later, {answers[question_num]} is the correct answer</>")

    question_num += 1

print("---------------------------------------")
print("               RESULTS                 ")
print("---------------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score/ len(questions) * 100)

if score >= 90:
    print("You are a genius!")
elif score >= 80:
    print("Excellent!")
elif score >= 70:
    print("You can do better!")
elif score >=60:
    print("Awesome!")
elif score >=50:
    print("You are better!")
elif score >=40:
    print("Please revise!")
else:
    print("You need to be more serious!")

print(f"Your total score is: {score} %")








