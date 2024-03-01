from strings import get_dna_complement, get_hamming_distance

def menu():

    print("""
    1. Hamming Distance
    2. DNA Complement
    3. Exit
    """)

    userChoice = int(input("What do you pick? (1-3)"))

    if (userChoice == 3):
        return

    if (userChoice == 2):
        inputComplement = input("What string do you want the complement of?")
        print("The complement is " + get_dna_complement(inputComplement))

    if (userChoice == 1):
        inputHamming1 = input("First string?")
        inputHamming2 = input("Second string?")
        print("The hamming distance is " + str(get_hamming_distance(inputHamming1, inputHamming2)))


    menu()

menu()