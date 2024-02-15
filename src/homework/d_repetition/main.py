from repetition import get_factorial
from repetition import sum_odd_numbers

decision = 0

while decision != 3:
    print("Homework 3 Menu")
    print("1 - Factorial")
    print("2 - Sum Odd Numbers")
    print("3 - Exit")

    decision = int(input("What menu number do you want to select?"))

    if (decision == 1):
        userNumber = 0
        while (userNumber >= 10 or userNumber <= 0):

            userNumber = int(input("Number 1-9?"))

            if (userNumber < 10 and userNumber > 0):
                print("The factorial is", get_factorial(userNumber))
    
    elif decision == 2:
        userNumber = 0
        while (userNumber >= 100 or userNumber <= 0):

            userNumber = int(input("Number 1-99?"))

            if (userNumber > 0 and userNumber < 100):
                print("The sum of odd numbers is", sum_odd_numbers(userNumber))
    
    userContinueDecision = input("Do you want to exit? (y/n)")
    if (userContinueDecision == "y"): 
        break
