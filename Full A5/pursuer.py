# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01

"""
Pursuer Class
"""
import random

# the pursuer that pursues the target
class Pursuer:
    def __init__(self):
        self.x_probability = 50
        self.y_probability = 50
        self.x_interaction = 0
        self.y_interaction = 0
        self.successful_interaction = 0
        self.fail_interaction = 0
        self.observed_x_behaviour = 0
        self.observed_y_behaviour = 0
        self.success_rate = 0

    # randomly generates behaviour based on probability
    # returns string indicating the type of behaviour
    def interact(self):
        X_BEHAVIOUR = "x"
        Y_BEHAVIOUR = "y"
        num = random.randint(1, 100)
        if num <= self.x_probability:
            self.x_interaction += 1
            result = X_BEHAVIOUR
            print("Pursuer behaviour: x", end="\t")
        else:
            self.y_interaction += 1
            result = Y_BEHAVIOUR
            print("Pursuer behaviour: y", end="\t")
        return result

    # determines if pursuer behaviour matched target behaviour
    # returns boolean expression, whether behaviours matched or not
    def display_interaction_result(self, target_behaviour, pursuer_behaviour):
        if target_behaviour == pursuer_behaviour:
            print("Matched behaviour")
            result = True
        else:
            print("Mis-Matched behavior")
            result = False
        return result

    # displays summary of results at the end of simulation
    def display_simluation_result(self, target):
        print("\nANALYSIS OF ALL THE INTERACTIONS")
        print("Target: No. of X's = %d"  %target.x_interaction, end="\t\t")
        print("No. of Y's = %d" %target.y_interaction)
        print("Pursuer: No. of X's = %d" %self.x_interaction, end="\t")
        print("No. of Y's = %d" %self.y_interaction)
        print("Number of successful matches: %d" %self.successful_interaction)
        self.success_rate = (self.successful_interaction/(self.successful_interaction+self.fail_interaction)*100)
        print("Proportion of successful matches: %.2f%%" %self.success_rate)
        if self.success_rate >= 50:
            print("Date was successful <3")
        else:
            print("Date was a dud :'(")