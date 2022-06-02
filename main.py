import math
import random

print("""  
  /$$$$$$   /$$$$$$  /$$        /$$$$$$  /$$   /$$ /$$        /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$       /$$__  $$| $$  | $$| $$       /$$__  $$|__  $$__//$$__  $$| $$__  $$
| $$  \__/| $$  \ $$| $$      | $$  \__/| $$  | $$| $$      | $$  \ $$   | $$  | $$  \ $$| $$  \ $$
| $$      | $$$$$$$$| $$      | $$      | $$  | $$| $$      | $$$$$$$$   | $$  | $$  | $$| $$$$$$$/
| $$      | $$__  $$| $$      | $$      | $$  | $$| $$      | $$__  $$   | $$  | $$  | $$| $$__  $$
| $$    $$| $$  | $$| $$      | $$    $$| $$  | $$| $$      | $$  | $$   | $$  | $$  | $$| $$  \ $$
|  $$$$$$/| $$  | $$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  | $$   | $$  |  $$$$$$/| $$  | $$
 \______/ |__/  |__/|________/ \______/  \______/ |________/|__/  |__/   |__/   \______/ |__/  |__/

                                                                                                   """)
print("Welcome to the Calculator App for all your needs!")
print("-------------------------------------------------- ")
print("1. + for Addition")
print("2. - for Subtraction")
print("3. * for Multiplication")
print("4. / for Division")
print("5. ** for Power")
print("6. square")
print("7. cube")
print("8. log")
print("9. ln for Natural Log")
print("10. tip for tip calculator")
print("10. RPS for Rock, Paper, Scissors game")

selected_operation = input("Enter the operation you'd like to perform: ")

if selected_operation not in ("+", "-", "*", "/", "**", "square", "cube", "log", "ln", "tip", "RPS"):
    print("Invalid Input")
    quit()

if selected_operation in ("+", "-", "*", "/", "**"):
    x = float(input("Enter first number: "))
    y = float(input("Enter Second Number: "))
    if selected_operation == "+":
        print(str(x) + " + " + str(y) + " = " + str(x + y))
    elif selected_operation == "-":
        print(str(x) + " - " + str(y) + " = " + str(x - y))
    elif selected_operation == "*":
        print(str(x) + " x " + str(y) + " = " + str(x * y))
    elif selected_operation == "/":
        print(str(x) + " / " + str(y) + " = " + str(x / y))
    elif selected_operation == "**":
        print(str(x) + "^" + str(y) + " = " + str(x ** y))

if selected_operation in ("square", "cube"):
    x = float(input("Enter number: "))
    if selected_operation == "square":
        print(str(x) + "^" + "2" " = " + str(x ** 2))
    elif selected_operation == "cube":
        print(str(x) + "^" + "3" " = " + str(x ** 3))

if selected_operation in ("log", "ln"):
    if selected_operation == "log":
        argument = float(input("Enter argument: "))
        base = float(input("Enter base: "))
        print("Log base " + str(base) + " of " + str(argument) + " = " + str(math.log(argument, base)))
    elif selected_operation == "ln":
        argument = float(input("Enter argument: "))
        print("Natural Log of " + str(argument) + " = " + str(math.log(argument)))


def tip_calculator():
    bill_amount = float(input("Enter your bill amount : "))
    tip = float(input("Enter tip percent: "))
    split = float(input("Enter how many people the bill is split amongst: "))
    total = round((bill_amount + (0.01 * tip) * bill_amount) / split, 2)
    return total


if selected_operation == "tip":
    price_after_tip = tip_calculator()
    print("Each person has to pay ${price_after_tip} amount".format(price_after_tip=price_after_tip))


def rpc_function(user_input):
    computer = ["Rock", "Paper", "Scissors"]
    computer_choice = computer[random.randint(0, 2)]
    if computer_choice == "Rock" and user_input == "R":
        winner = "Tie"
    elif computer_choice == "Paper" and user_input == "P":
        winner = "Tie"
    elif computer_choice == "Scissors" and user_input == "S":
        winner = "Tie"
    elif computer_choice == "Rock" and user_input == "S":
        winner = "Computer Wins"
    elif computer_choice == "Paper" and user_input == "R":
        winner = "Computer Wins"
    elif computer_choice == "Scissors" and user_input == "P":
        winner = "Computer Wins"
    elif computer_choice == "Scissors" and user_input == "R":
        winner = "You Win"
    elif computer_choice == "Rock" and user_input == "P":
        winner = "You Win"
    elif computer_choice == "Paper" and user_input == "S":
        winner = "You Win"

    if user_input in ("R", "P", "S"):
        print("Computer Choice: " + computer_choice)
        print("Winner: " + winner)
    else:
        print("Invalid Input")


if selected_operation == "RPS":
    user = input("Enter [R]ock, [P]aper, or [S]cissors: ")
    rpc_function(user)
