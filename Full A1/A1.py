# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01
# Ver. 1.0.0
# May 16, 2017

"""
A program that will calculate your term grade point based on the weights 
specified in the course admin notes. The program will prompt the user
for the grade point for each component and calculate the weighted grade
point for that component. 


Program Limitations:
This program does not check for input errors. It does not check for 
invalid types of infomation being entered.
"""

# prompt user to enter mini-assignment grades
print("Entering mini-assignments")
ma2 = float(input("Grade (0-4) for mini assignment # 2: "))
ma3 = float(input("Grade (0-4) for mini assignment # 3: "))
ma4 = float(input("Grade (0-4) for mini assignment # 4: "))
ma5 = float(input("Grade (0-4) for mini assignment # 5: "))
print()

# prompt user too enter full assignment grades
print("Entering full assignments")
fa1 = float(input("Grade (0-4) for full assignment # 1: "))
fa2 = float(input("Grade (0-4) for full assignment # 2: "))
fa3 = float(input("Grade (0-4) for full assignment # 3: "))
fa4 = float(input("Grade (0-4) for full assignment # 4: "))
fa5 = float(input("Grade (0-4) for full assignment # 5: "))
print()

# prompt user to enter enter exam grades
print("Entering examinations")
midterm = float(input("Midterm exam grade (0-4): "))
final = float(input("Final exam grade (0-4): "))
print()

# gpa calculation logic: weight * grade
gpa_ma2 = 0.005 * ma2
gpa_ma3 = 0.005 * ma3
gpa_ma4 = 0.005 * ma4
gpa_ma5 = 0.005 * ma5
gpa_fa1 = 0.04 * fa1
gpa_fa2 = 0.06 * fa2
gpa_fa3 = 0.06 * fa3
gpa_fa4 = 0.10 * fa4
gpa_fa5 = 0.07 * fa5
gpa_midterm = 0.25 * midterm
gpa_final = 0.40 * final

# weighted grades
weighted_mini = gpa_ma2 + gpa_ma3 + gpa_ma4 + gpa_ma5
weighted_full = gpa_fa1 + gpa_fa2 + gpa_fa3 + gpa_fa4 + gpa_fa5
weighted_midterm = gpa_midterm
weighted_final = gpa_final
weighted_term = weighted_mini + weighted_full + weighted_midterm + weighted_final

# display weighted grade points formatted to 3 decimal places
print("------------------------------------------------------")
print("Weighted grade points")
print("------------------------------------------------------")
print("Mini-assignments")
print("Weighted mini assignment 2 grade =", format(gpa_ma2,".3f"))
print("Weighted mini assignment 3 grade =", format(gpa_ma3,".3f"))
print("Weighted mini assignment 4 grade =", format(gpa_ma4,".3f"))
print("Weighted mini assignment 5 grade =", format(gpa_ma5,".3f"))
print()
print("Full assignments")
print("Weighted full assignment 1 grade =", format(gpa_fa1,".3f"))
print("Weighted full assignment 2 grade =", format(gpa_fa2,".3f"))
print("Weighted full assignment 3 grade =", format(gpa_fa3,".3f"))
print("Weighted full assignment 4 grade =", format(gpa_fa4,".3f"))
print("Weighted full assignment 5 grade =", format(gpa_fa5,".3f"))
print()
print("Exams")
print("Weighted midterm grade =", format(gpa_midterm,".3f"))
print("Weighted final grade =", format(gpa_final,".3f"))
print("======================================================")

# display term grade
print("Weighted term grade:", format(weighted_term,".3f"))




