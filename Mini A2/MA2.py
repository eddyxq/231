# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01
# Ver. 1.0.0
# May 16, 2017

"""
A program that will prompt the user for his/her age in years. It will 
repeatedly prompt the user (using a loop) for the age as long as the 
person enters a value less than the age cut-off (18+). If the age is 
nonsensically low (less than zero) then an error message is displayed 
before prompting the person again. Once the user enters an age that 
meets the cut-off, the program will let the user know that the age 
requirement has been met.

Limitations: This program only accepts integer input.
"""

age = 0

# loop to prompt user to enter age if under 18

while age < 18: 
        age = int(input("Enter your age in (whole) years: "))
        if age < 0:
                print("Error, in order be typing at the computer you need to have been born first. Try again.")
        elif age >= 18:
                print("Age requirement met!")