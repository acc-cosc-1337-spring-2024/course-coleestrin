import random

class Die:

    _roll_value: int

    def roll(self):
        self._roll_value = random.randint(1, 6)

    def get_rolled_value(self):
        return self._roll_value
    
    def __str__(self):
        print(f"The rolled value is {self._roll_value}")
