# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01

"""
Target Class
"""
import random

# the target being pursued by the pursuer
class Target:
    def __init__(self):
        self.x_interaction = 0
        self.y_interaction = 0
        self.x_probability = 0
        self.y_probability = 0

    # randomly generates behaviour based on probability
    # returns string indicating the type of behaviour
    def interact(self):
        X_BEHAVIOUR = "x"
        Y_BEHAVIOUR = "y"
        num = random.randint(1,100)
        if num <= self.x_probability:
            print("Target behaviour: x", end="\t")
            self.x_interaction += 1
            result = X_BEHAVIOUR
        else:
            print("Target behaviour: y", end="\t")
            self.y_interaction += 1
            result = Y_BEHAVIOUR
        return result