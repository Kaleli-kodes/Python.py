name = input("Please enter your name: ")

print("Welcome", name, "to your new challenge🥰")

response = input("Which destination would you like to visit, china or states: ").lower()

if response == "china":

    response = input("Which career would you like to pursue; kungfu or karate: ").lower()

    if response == "kungfu":
        print("Seems you've watched Kungfu panda!")
    elif response == "karate":
        print("You are a warrior!")
    else:
        print("Invalid option!")

elif response == "states":

    response = input("Which career would you like to pursue, football or web developer?").lower()

    if response == "football":
        print("******************")
        print("You support Messi👽!")
        print("******************")
    elif response == "web developer":
        print("**************")
        print("You like bugs🤩")
        print("**************")
    else:
        print("Invalid option!")
else:
    print("Please enter a valid option")

