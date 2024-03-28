import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

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