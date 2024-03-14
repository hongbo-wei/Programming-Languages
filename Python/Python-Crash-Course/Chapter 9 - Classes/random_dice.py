# exercise 9-13 Dice
from random import randint

class Dice:
    def __init__(self):
        self.sides = 6
        self.count = 1
    def roll_dice(self):
        for i in range(10):
            print(self.count, randint(1,self.sides))
            self.count += 1

dice = Dice()
dice.roll_dice()

dice.sides = 10
dice.roll_dice()

dice.sides = 20
dice.roll_dice()
