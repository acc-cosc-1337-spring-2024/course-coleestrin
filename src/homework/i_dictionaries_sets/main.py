from sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog2_not_prog_1

prog1 = set(['Student1', 'Student2', 'Student3'])
prog2 = set(['Student3', 'Student4', 'Student5'])

def menu():

    print('''
          1) Students who took prog1 and prog2
          2) Students who took prog1 or prog2
          3) Students who took prog1 not prog2
          4) Students who took prog2 not prog1
          5) Exit
          ''')
    
    userChoice = int(input("Your choice? (1-5)"))

    if (userChoice == 1):
       print(get_students_who_took_prog1_and_prog2(prog1, prog2))

    elif (userChoice == 2):
      print(get_students_who_took_prog1_or_prog2(prog1, prog2))

    elif (userChoice == 3):
       print(get_students_who_took_prog1_not_prog_2(prog1, prog2))

    elif (userChoice == 4):
       print(get_students_who_took_prog2_not_prog_1(prog1, prog2))
       
    elif (userChoice == 5):
        return

    menu()

menu()





