# Credit card program
total_odds = 0
total_evens = 0
total = 0

credit_card_num = input("Enter your master card number: ")
credit_card_num = credit_card_num.replace("-", "")
credit_card_num = credit_card_num.replace(" ", "")
print(credit_card_num)

# step 2
for x in credit_card_num[::-1]:
    total_odds += int(x)

# step 3
for x in credit_card_num[2::2]:
    x = int(x) * 2
    if x >= 10:
        total_evens += (1 + (x % 10))
    else:
        total_evens += x
# step 4
total = total_odds + total_evens

# step 5
if total % 10 == 0:
    print("Valid!")
else:
    print("Invalid!")
















