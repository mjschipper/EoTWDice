#!/usr/bin/env python
from random import randint

class Die(object):
    """
    Creates a die class for use with a dice rolling utility
    """
    d_sides = None
    def __init__(self, sides = 6):
        self._sides = sides
        self._value = None
        self.roll()

    def roll(self):
        """
        Generate a random integer based off the number of sides
        """
        self._value = randint(1, self._sides)
        return self._value

    def __str__(self):
        """
        Return string containing dice sides and result
        """
        return "Die with {} sides.  Result : {}".format(self._sides, self._value)

def dice_cup(p, n, s):

    dice_roll = {}
    dice_roll[0] = [Die(6).roll() for _ in range(int(p))]
    dice_roll[1] = [Die(6).roll() for _ in range(int(n))]
    calc = calculate_results(dice_roll, s)

    return calc

def calculate_results(r, s):
    """
    - Finds first element matching on both lists for unique numbers. i.e. [4,2,3,2],[2,3,6] result: [4,2],[6]
    - Positive rolls equal to or under stat to succeed otherwise failure. i.e. if above attribute stat is 2: 1 success.
    - Left over 'len' equals stress i.e. above example is 1 stress
    """

    for i in r[0][:]:
        if i in r[1]:
            r[0].remove(i)
            r[1].remove(i)

    r[2] = sum(1 for i in r[0] if i <= s)
    r[3] = len(r[1])

    return r

def engine():
    # Asks for a number of dice and verifies that it's a number
    while True:
        try:
            s = int(input("Input Attribute Score?\n>"))
            break
        except(TypeError, ValueError):
            print("Please enter a number\n")

    while True:
        try:
            p = int(input("How many positive dice?\n>"))
            break
        except(TypeError, ValueError):
            print("Please enter a number\n")

    # Asks for a number of dice and verifies that it's a number
    while True:
        try:
            n = int(input("How many negative dice?\n>"))
            break
        except(TypeError, ValueError):
            print("Please enter a number\n")

    results = dice_cup(p, n, s)
    print(results)
    if not results[2] == 0:
        print("Success: " + str(results[2]))
    else:
        print("Failure!")
    print("Stress: " + str(results[3]))

def main():
    engine()

if __name__ == "__main__":
    main()
