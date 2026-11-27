import random

while True:
    user_spin = input("Do you want to spin(x/z)?: ").lower()

    if user_spin == "x":
        spin1 = random.randint(1,10)
        spin2 = random.randint(1,10)
        print(spin1, spin2)
    elif user_spin == "z":
        break
    else:
        print("Please enter either x or z")




