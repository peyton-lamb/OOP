import random

class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4

    def set_lof(self):
        self.flight_len = random.randint(0, 10)

    def get_lof(self):
        return self.flight_len