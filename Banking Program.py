# Cooperative M-Banking Program
def display_balance(balance):
    print(f"Balance: $ {balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount< 0:
        print("Please enter a positive amount: ")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount < 0:
        print("************************")
        print("Please enter a positive amount: ")
        print("*************************")
        return 0
    elif amount > balance:
        print("********************")
        print("Insufficient funds: ")
        print("********************")
        return 0
    else:
        return amount

def transfer(balance):
    amount = float(input("Enter amount to transfer: "))
    if amount < 0:
        print("***************")
        print("Please enter a positive amount")
        print("***************")
        return 0
    elif amount > balance:
        print("******************")
        print("Insufficient funds")
        print("******************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_operating = True

    while is_operating:
        print("**********************************")
        print("<<<<<<<Equity Banking Program>>>>>")
        print("**********************************")
        print("1.balance")
        print("**********")
        print("2.deposit")
        print("**********")
        print("3.withdraw")
        print("**********")
        print("4.transfer")
        print("**********")
        print("5:Exit")
        print("**********")

        user_choice = input("Enter your choice(1-5): ")

        if user_choice == "1":
            display_balance(balance)
        elif user_choice == "2":
            balance += deposit()
        elif user_choice == "3":
            balance -= withdraw(balance)
        elif user_choice == "4":
            balance -= transfer(balance)
        elif user_choice == "5":
            is_operating = False
        else:
            print("***************************")
            print("Please enter a valid option")
            print("***************************")

    print("*************************")
    print("Thank you! Enjoy your day")
    print("*************************")

if __name__ == "__main__":
    main()











