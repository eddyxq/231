# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01

"""
Patch History:
Date               Version                Notes
June 08, 2017      Ver. 1.0.0             initialized game: added functions initialize(), readFromFile(), display() 
June 09, 2017      Ver. 1.0.1             added game menu and cheat menu
June 11, 2017      Ver. 1.0.2             implemented student movement features
June 13, 2017      Ver. 1.0.3             added pavol and taminator events
June 14, 2017      Ver. 1.0.4             implemented path finding and taminator movement
"""

"""
This is a program that simulates the life of a student. The simulated world is represented by a 2D Python list of
single character strings. A student 'S' can either choose to maximize their fun times 'f' during the term or the person
can choose to expend time working 'w' in order to maximize the term grade point (GPA) and letter graded awarded. In this
simulation there is not only a direct but a perfect correlation between time spent working and the grade awarded. Like a 
semester in "real life" there is only a finite amount of time during a term and the simulation will run for a maximum of 
13 turns (weeks). Each time that the user is prompted to move the student (or if the choice is given up) a time unit 
will be expended. The initial starting positions will be read in from a text file whose name is specified as the program 
is started. The student's 'score' (fun and grade points earned along with the term letter grade) is saved to another 
text file 'scores.txt'. Only one set of scores are retained, each time that the simulation runs previous scores are 
overwritten.
"""

import random
debug_mode_on = False
SIZE = 10
# displays the contents of the game world, written by James Tam
def display(world, turn, fun_points, gpa):
    print("\nCurrent turn:", turn)
    print("Fun points:", fun_points, "\t", "GPA:", gpa)
    for r in range(0, SIZE, 1):
        for i in range(0, SIZE, 1):
            print(" -", end="")
        print()
        for c in range(0, SIZE, 1):
            print("|" + world[r][c], end="")
        print("|")
    for i in range(0, SIZE, 1):
        print(" -", end="")
    print()

# creates a 2d list with an area of SIZE x SIZE, written by James Tam
def initialize():
    world = []
    for r in range(0, SIZE, 1):
        world.append([])
        for c in range(0, SIZE, 1):
            world[r].append("!")
    return (world)

# reads starting locations from file, written by James Tam
def readFromFile():
    world = initialize()
    inputFilename = input("Name of input file: ")
    try:
        inputFile = open(inputFilename, "r")
        r = 0
        for line in inputFile:
            c = 0
            for ch in line:
                if (c < SIZE):
                    world[r][c] = ch
                    c = c + 1
            r = r + 1
        inputFile.close()
    except IOError:
        print("Error reading from " + inputFilename)
    return world

# prompts user for input
def movement_options():
    validity = False
    while validity == False:
        display_movement_menu()
        try:
            decision = int(input("Movement Selection: "))
            if decision in range(0, 10):
                validity = True
                return decision
            else:
                print("\n<!> Invalid input, please enter a valid menu option <!>\n")
        except ValueError:
            print("\n<!> Invalid input, please enter a valid menu option <!>\n")

# displays menu of movement options
def display_movement_menu():
    print("MOVEMENT OPTIONS")
    for row in range(7, 0, -3):
        for col in range(row, row + 3):
            print(col, end="  ")
        print()
    print("Type a number on the key pad to indicate direction of movement")
    print("Type 5 to pass on movement")

# displays cheat menu options
def display_cheat_menu():
    validity = False
    while validity == False:
        print("Cheat menu options")
        print("(t)oggle debug mode on/off")
        print("(m)ake the Taminator appear")
        print("(p)avol manifests itself")
        print("(q)uit cheat menu")
        try:
            cheat_command = str(input("Cheat menu selection: "))
            if cheat_command in ("t", "m", "p", "q"):
                validity = True
                return cheat_command
            else:
                print("\n<!> Invalid input, please enter a valid menu option <!>\n")
        except ValueError:
            print("\n<!> Invalid input, please enter a valid menu option <!>\n")

# instantly summon pavol
def manifest_pavol(turn):
    turn -= 1
    print("\n-Pavol manifests itself and stops time for a turn-")
    return turn

# calculate letter grade
def gpa_convert(gpa):
    if gpa == 4:
        letter_grade = "A"
    elif gpa == 3:
        letter_grade = "B"
    elif gpa == 2:
        letter_grade = "C"
    elif gpa == 1:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

# game ending message
def end_game(letter_grade, fun_points, gpa):
    print("\nThe simulation has ended, it has been 13 turns!")
    print("You have scored %d Fun points and a GPA of %d" % (fun_points, gpa))
    print("Converting GPA to letter grade...")
    print("Your final letter grade is", letter_grade)

# finds location of the student
def find_student(world, STUDENT, EMPTY):
    for row in range(len(world)):
        for col in range(len(world)):
            if world[row][col] == STUDENT:
                student_row = row
                student_column = col
                world[student_row][student_column] = EMPTY
                return student_row, student_column

# debugging menu
def debug_mode(debug_mode_on, pavol, tam, student_row, student_column, taminator_exist, tam_row,
               tam_column):
    if debug_mode_on:
        print("\n\t**DEBUG**")
        print("<<< Pavol RNG =", pavol, "    >>>")
        print("<<< Taminator RNG =", tam, ">>>\n")
        print("Student location: [%d][%d]" % (student_row, student_column))
        if taminator_exist:
            print("Taminator location: [%d][%d]\n" % (tam_row, tam_column))
        else:
            print("Taminator location: [N/A]\n")

# writes final scores and grade to file
def write_to_file(letter_grade, fun_points, gpa):
    try:
        fun_points = str(fun_points)
        gpa = str(gpa)
        output_file = open("stats.txt", "w")
        output_file.write("Fun points:" + " " + fun_points + "\n")
        output_file.write("GPA:" + " " + gpa + "\n")
        output_file.write("Letter grade:" + " " + letter_grade + "\n")
        output_file.close()
    except IOError:
        print("File Error")

# instantly spawns the taminator
def spawn_taminator(student_row, student_column):
    tam_row = int(input("Enter row(0-9) #:"))
    tam_column = int(input("Enter column(0-9) #:"))
    while tam_row > 9 or tam_row < 0 or tam_column > 9 or tam_column < 0 or \
            (tam_row == student_row and tam_column == student_column):
        print("Error, the row and column must be between 0 and 9. "
              "Also you cannot spawn him directly on top of the student.")
        tam_row = int(input("Enter row(0-9) #:"))
        tam_column = int(input("Enter column(0-9) #:"))
    print("\nA wild Taminator has appeared\n")
    return tam_row, tam_column

# path finding logic for the taminator
def taminator_chase(tam_row, tam_column, student_row, student_column):
    row_distance = tam_row - student_row
    col_distance = tam_column - student_column
    if row_distance > 2:
        tam_row -= 2 
    elif row_distance > 1: 
        tam_row -= 1 
    if row_distance < -2: 
        tam_row += 2
    elif row_distance < -1: 
        tam_row += 1
    if col_distance > 2: 
        tam_column -= 2
    elif col_distance > 1: 
        tam_column -= 1
    if col_distance < -2: 
        tam_column += 2
    elif col_distance < -1: 
        tam_column += 1
    return tam_row, tam_column

# determines if taminator has caught student
def student_taminator_distance(tam_row, tam_column, student_row, student_column, turn):
    if (abs(tam_row - student_row) < 2) and (abs(tam_column - student_column) < 2):
        # remove taminator from field
        print("\nThe Taminator caught has caught you and wasted two of your turns!\n")
        turn += 2
    return turn

# moves the student
def move_student(choice, student_row, student_column):
    MOVE_DIAGONAL_DOWN_LEFT = 1
    MOVE_DOWN = 2
    MOVE_DIAGONAL_DOWN_RIGHT = 3
    MOVE_LEFT = 4
    NO_MOVEMENT = 5
    MOVE_RIGHT = 6
    MOVE_DIAGONAL_UP_LEFT = 7
    MOVE_UP = 8
    MOVE_DIAGONAL_UP_RIGHT = 9
    if choice == MOVE_DIAGONAL_DOWN_LEFT and student_row != 9 and student_column != 0:
        student_row += 1
        student_column -= 1
    elif choice == MOVE_DOWN and student_row != 9:
        student_row += 1
    elif choice == MOVE_DIAGONAL_DOWN_RIGHT and student_row != 9 and student_column != 9:
        student_row += 1
        student_column += 1
    elif choice == MOVE_LEFT and student_column != 0:
        student_column -= 1
    elif choice == NO_MOVEMENT:
        pass
    elif choice == MOVE_RIGHT and student_column != 9:
        student_column += 1
    elif choice == MOVE_DIAGONAL_UP_LEFT and student_row != 0 and student_column != 0:
        student_row -= 1
        student_column -= 1
    elif choice == MOVE_UP and student_row != 0:
        student_row -= 1
    elif choice == MOVE_DIAGONAL_UP_RIGHT and student_row != 0 and student_column != 9:
        student_row -= 1
        student_column += 1
    else:
        print("\nStop wasting your turns trying to go through the wall!")
    return student_row, student_column

# toggles debug mode on/off
def toggle_debug_mode():
    global debug_mode_on
    if debug_mode_on:
        debug_mode_on = False
    else:
        debug_mode_on = True

# removes taminator
def remove_taminator(world, TAMINATOR, EMPTY):
    for row in range(len(world)):
        for col in range(len(world)):
            if world[row][col] == TAMINATOR:
                world[row][col] = EMPTY

# start function
def main():
    STUDENT = "S"
    TAMINATOR = "T"
    WORK = "w"
    FUN = "f"
    EMPTY = " "
    taminator_exist = False
    turn = 1
    fun_points = 0
    gpa = 0
    tam_life = 0
    pavol = 0
    tam = 0
    CHEAT_MENU = 0
    tam_row = "[N/A]"
    tam_column = "[N/A]"
    world = readFromFile()
    while turn <= 13:
        display(world, turn, fun_points, gpa)
        student_row, student_column = find_student(world, STUDENT, EMPTY)
        debug_mode(debug_mode_on, pavol, tam, student_row, student_column, taminator_exist, tam_row, tam_column)
        if taminator_exist:
            if ((abs(tam_row - student_row) < 2) and (abs(tam_column - student_column) < 2)) or tam_life == 0:
                world[tam_row][tam_column] = EMPTY
                taminator_exist = False
        choice = movement_options()
        if choice == CHEAT_MENU:
            cheat_command = display_cheat_menu()
            if cheat_command == "t":
                toggle_debug_mode()
            elif cheat_command == "m":
                if taminator_exist:
                    print("You cannot invoke the Taminator again before it has vanished")
                else:
                    tam_row, tam_column = spawn_taminator(student_row, student_column)
                    world[tam_row][tam_column] = TAMINATOR
                    world[student_row][student_column] = STUDENT
                    display(world, turn, fun_points, gpa)
                    tam_life = 3
                    taminator_exist = True
            elif cheat_command == "p":
                if taminator_exist == False:
                    turn = manifest_pavol(turn)
                else:
                    print("You cannot invoke Pavol until Taminator has vanished")
            elif cheat_command == "q":
                print("Going back to main menu\n")
        elif choice in range(1, 10):
            student_row, student_column = move_student(choice, student_row, student_column)
        if world[student_row][student_column] == WORK:
            gpa += 1
        if world[student_row][student_column] == FUN:
            fun_points += 1
        world[student_row][student_column] = STUDENT
        if taminator_exist:
            world[tam_row][tam_column] = EMPTY
            tam_row, tam_column = taminator_chase(tam_row, tam_column, student_row, student_column)
            world[tam_row][tam_column] = TAMINATOR
            turn = student_taminator_distance(tam_row, tam_column, student_row, student_column, turn)
        # randomly generating pavol and taminator events
        if taminator_exist == False:
            pavol = random.randint(1, 10)
            if pavol == 1:
                turn -= 1
                print("\n-Pavol manifests itself and stops time for a turn-")
            else:
                tam = random.randint(1, 4)
                if tam == 1:
                    validity = False
                    while validity == False:
                        tam_row = random.randint(0, 9)
                        tam_column = random.randint(0, 9)
                        if tam_row != student_row and tam_column != student_column:
                            validity = True
                    world[tam_row][tam_column] = TAMINATOR
                    print("\nA wild Taminator has appeared\n")
                    tam_life = 3
                    taminator_exist = True
        if tam_life > 0:
            tam_life -= 1
        else:
            remove_taminator(world, TAMINATOR, EMPTY)
            taminator_exist = False
        turn += 1
    letter_grade = gpa_convert(gpa)
    end_game(letter_grade, fun_points, gpa)
    write_to_file(letter_grade, fun_points, gpa)
main()