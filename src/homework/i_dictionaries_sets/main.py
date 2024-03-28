from dictionary import add_inventory, remove_inventory_widget

users_dict = {}

def menu():

    print('''
          1) Add/Update item
          2) Delete item
          3) Exit
          ''')
    
    userChoice = int(input("Your choice? (1-3)"))

    if (userChoice == 1):
        name = input("Widget name?")
        quantity = int(input("Quantity?"))
        add_inventory(users_dict, name, quantity)
        print('Updated dictionary')

    elif (userChoice == 2):
        name = input("Widget to delete?")
        remove_inventory_widget(name, users_dict)
        print('Updated dictionary')

    elif (userChoice == 3):
        return

    print(f'Your dictionary: {users_dict}')

    menu()

menu()





