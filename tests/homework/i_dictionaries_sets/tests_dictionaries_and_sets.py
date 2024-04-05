import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget
from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog2_not_prog_1

prog1 = set(['Student1', 'Student2', 'Student3'])
prog2 = set(['Student3', 'Student4', 'Student5'])

class Test_Config(unittest.TestCase):
     
     def test_add_inventory(self):
        inventory_dictionary = {}

        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertEqual(inventory_dictionary.get("Widget1"), 10)

        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(inventory_dictionary.get("Widget1"), 35)

        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(inventory_dictionary.get("Widget1"), 25)

     def test_remove_inventory_widget(self):
       inventory_dictionary = {}
       add_inventory(inventory_dictionary, "widget1", 15)
       add_inventory(inventory_dictionary, "widget2", 30)

       remove_inventory_widget("widget1", inventory_dictionary)

       self.assertEqual(len(inventory_dictionary), 1)
       self.assertEqual(inventory_dictionary.get("widget2"), 30)

     def test_get_students_who_took_prog1_and_prog2(self):
         self.assertEqual(get_students_who_took_prog1_and_prog2(prog1, prog2), set(["Student3"]))

     def get_students_who_took_prog1_or_prog2(self):
         self.assertEqual(get_students_who_took_prog1_or_prog2(prog1, prog2), set(["Student1", "Student2", "Student3", "Student4", "Student5"]))

     def test_get_students_who_took_prog1_not_prog_2(self): 
         self.assertEqual(get_students_who_took_prog1_not_prog_2(prog1, prog2), set(["Student1", "Student2"]))
     
     def test_get_students_who_took_prog2_not_prog_1(self):   
         self.assertEqual(get_students_who_took_prog2_not_prog_1(prog1, prog2), set(["Student4", "Student5"]))