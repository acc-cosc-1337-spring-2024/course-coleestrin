from class_a import Die

def menu():
    print("""
    1) Roll Die
    2) Exit
    """)

    choice = int(input("Your choice? (1-2)"))

    if (choice == 1):
        dice = Die()
        dice.roll()
        dice.__str__()
    elif (choice == 2):
        return
    
    menu()

menu()

    

