# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01
# Ver. 1.0.0
# June 14, 2017

"""
Adventurer class
"""

class Adventurer:
    def __init__(self):
        self.name = "nameless"
        self.health = -1

    def gain_level(self):
        self.health += 5
        print("\nCongratulations!\n")

    def display_stats(self):
        print("Your name is:", self.name)
        print("Your health is:", self.health)