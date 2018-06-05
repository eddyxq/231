# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01

"""
Patch History:
Date               Version                Notes
June 16, 2017      Ver. 1.0.0             created the Target and Pursuer class
June 18, 2017      Ver. 1.0.1             defined methods that allows interaction
"""

"""
This program is a dating simulator between two fictional life forms called "The Tims". There are two types of Tims in
this simulation: a "Target" and a "Pursuer". The target is the object of the pursuer's desire. The behaviour of both 
types of Tims is purely random. The date consists of a number of social interactions between two Tims broken down into 
discrete time units. Each type of Tim will engage in one of two types of interactions: type X-behaviour and type
Y-behaviour. If the two Tims engage in the same type of interaction then that interaction is deemed as successful,
otherwise the interaction is deemed as a failure. A summary report will be generated after each interaction briefly 
showing the result of the interaction for that time unit. At the end of the simulation a more detailed report will show 
the overall results.
"""
import pursuer as p
import target as t
import random

# gets user input
# accepts integer input
# returns integer 
def get_interaction():
    try:
        num = int(input("Enter the number of interactions (1 or greater): "))
        if num > 0:
            return num
        else:
            print("Do not enter non-numeric values")
            num = get_interaction()
            return num
    except ValueError:
        print("Do not enter non-numeric values")
        num = get_interaction()
        return num

# gets user input
# accepts integer input
# returns integer 
def get_probability():
    try:
        num = int(input("Enter the percentage # of 'X' interactions for target (whole numbers from 0 - 100): "))
        if num in range(0, 101):
            return num
        else:
            print("Do not enter non-numeric values")
            num = get_probability()
            return num
    except ValueError:
        print("Do not enter non-numeric values")
        num = get_probability()
        return num


# manager function
def main():
    X_BEHAVIOUR = "x"
    Y_BEHAVIOUR = "y"
    # create instances of target and pursuer
    pursuer = p.Pursuer()
    target = t.Target()

    # get user input
    num = get_interaction()
    target.x_probability = get_probability()

    # pursuer and target interacting
    for x in range(num):
        target_behaviour = target.interact()
        pursuer_behaviour = pursuer.interact()

        # determine and display result of interaction
        result = pursuer.display_interaction_result(target_behaviour, pursuer_behaviour)
        if result == True:
            pursuer.successful_interaction += 1
        elif result == False:
            pursuer.fail_interaction += 1

        # pursuer learns about the target
        if target_behaviour == X_BEHAVIOUR:
            pursuer.observed_x_behaviour += 1
        elif target_behaviour == Y_BEHAVIOUR:
            pursuer.observed_y_behaviour += 1

        # pursuer AI adapts to match the target
        pursuer.x_probability = pursuer.observed_x_behaviour/(pursuer.observed_x_behaviour + pursuer.observed_y_behaviour)*100
        pursuer.y_probability = 100 - pursuer.x_probability

    # display final results after all interactions
    pursuer.display_simluation_result(target)

main()