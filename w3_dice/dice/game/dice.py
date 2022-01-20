import random

#Dice class used for random integers between 1 and 5
#   and to add appropriate points to score
class Dice:
    def __init__(self):
        self.points = 0
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)
        if self.value == 5:
            self.points = 50
        elif self.value == 1:
            self.points = 100
        else:
            0