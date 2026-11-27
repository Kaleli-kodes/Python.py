#Python Slot machine
import random

def spin_row():
    symbols = ["🍉", "🍒","🍇","🍁"]

    return [random.choice(symbols)for symbol in range(3)]

def print_row(row):
    print("************")
    print("|".join(row))
    print("************")
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍉":
            return bet * 50
        elif row[0] == "🍒":
            return bet * 100
        elif row[0] == "🍇":
            return bet * 150
        elif row[0] == "🍁":
            return bet * 200
    return 0

def main():

    balance = 1000

    print("*************************")
    print("Welcome to our slot game!")
    print("symbols:🌼🌺🌸🍉🍒🍇🍁 ")
    print("*************************")

    while balance > 0:
        print(f"Current balance:$ {balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a number")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Deposit funds")
            continue

        balance -= bet

        row = spin_row()
        print("spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Congratulations! you won: ${payout}")
        else:
            print("Sorry you lost")

        balance += payout

        try_again = input("Do you want to play again(y): ")
        if try_again != "y":
            break
        else:
            continue

        print(f"Current balance: {balance}")

if __name__ == "__main__":
    main()




