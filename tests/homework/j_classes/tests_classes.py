import unittest
from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_die_roll(self):
        test_die = Die()
        
        for _ in range(3):
            test_die.roll()
            self.assertTrue(test_die.get_rolled_value() >= 1 and test_die.get_rolled_value() <= 6)

