# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01
# Ver. 1.0.0
# May 30, 2017

"""
A program that will ask the user for a number and double it and
print out that number.
"""

# functions

def start():
        number = getInput()
        doubledNumber = double(number)
        display(doubledNumber)

def getInput():
        enteredNum = float(input("Please enter a number: "))
        return enteredNum

def double(num):
        doubled = num * 2
        return doubled

def display(output):
        print(output)

start()