# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01
# Ver. 1.0.0
# May 16, 2017

"""
A text-based "choose your own" adventure game. There are three rooms 
in the game world, within each room the player will see a number of 
choices and the program will react to the player's decision. The goal
of this game is to try to unlock the inner door. The door will only be 
unlocked if the player turns the key silver lock in the pantry to the 
"right" position and the key gold lock in the kitchen to the "left"
position. Upon opening the door, the main loop ends and a congratulatory
message is displayed.
"""

print("""
You have just stepped into the entrance room through the outer door.
The door you came through magically vanishes behind you. In front of
you there is a inner door, one room to your left, and one room to your
right.
""")

# initialize game settings, create variables

room = "entrance"
gold_lock = "center"
silver_lock = "center"
inner_door_locked = True

# main game loop

while inner_door_locked == True:

    # entrance room logic

    if room == "entrance":
        print("You are now at the entrance room.")

        # input validation loop

        try:

            validity = False
            while validity == False:
                print("1. Try to open the door")
                print("2. Go through the left entry way")
                print("3. Go through the right entry way")
                movement = int(input("What would you like to do? Enter choice number: "))
                print()
                if movement in range(1,4):
                    validity = True
                else:
                    print("Invalid entry, please enter again.")

            # movement logic

            if movement == 1:
                print("You try to open the door and...")

                # win condition

                if ((silver_lock == "right" and gold_lock == "left")):
                    inner_door_locked = False
                    print("The door unlocks. Congratulations!")
                else:
                    print("The door won't budge!")
                    print()
            elif movement == 2:
                room = "kitchen"
            elif movement == 3:
                room = "pantry"
            else:
                print("Invalid entry, please enter again.")

        except ValueError:
            print("Invalid entry, please enter again.")
            print()
            
    # pantry room logic

    elif room == "pantry":
        print("You are now at the pantry, and you see a silver lock.")
        print("The silver lock is currently in the", silver_lock, "position.")

        # input validation loop

        try:

            validity = False
            while validity == False:
                print("1. Turn the silver lock to the left position")
                print("2. Turn the silver lock to the right position")
                print("3. Turn the silver lock to the center position")
                print("4. Don't change the position! Return to entrance way")
                silver_position = int(input("What would you like to do? Enter choice number: "))
                print()
                if silver_position in range(1,5):
                    validity = True
                else:
                    print("Invalid entry, please enter again.")

            # silver lock logic

            if silver_position == 1:
                print("The silver lock is now set to the left position")
                silver_lock = "left"
                print()
            elif silver_position == 2:
                print("The silver lock is now set to the right position")
                silver_lock = "right"
                print()
            elif silver_position == 3:
                print("The silver lock is now set to the center position")
                silver_lock = "center"
                print()
            elif silver_position == 4:
                room = "entrance"
                print("You return to the entrance room.")
                print()
            else:
                print("Invalid entry, please enter again.")

        except ValueError:
            print("Invalid entry, please enter again.")
            print()



    # kitchen room logic

    elif room == "kitchen":
        print("You are now at the kitchen, and you see a gold lock.")
        print("The gold lock is currently in the", gold_lock, "position.")

        # input validation loop

        try:

            validity = False
            while validity == False:
                print("1. Turn the gold lock to the left position")
                print("2. Turn the gold lock to the right position")
                print("3. Turn the gold lock to the center position")
                print("4. Don't change the position! Return to entrance way")
                gold_position = int(input("What would you like to do? Enter choice number: "))
                print()
                if gold_position in range(1,5):
                    validity = True
                else:
                    print("Invalid entry, please enter again.")

            # gold lock logic

            if gold_position == 1:
                print("The gold lock is now set to the left position")
                gold_lock = "left"
                print()
            elif gold_position == 2:
                print("The gold lock is now set to the right position")
                gold_lock = "right"
                print()
            elif gold_position == 3:
                print("The gold lock is now set to the center position")
                gold_lock = "center"
                print()
            elif gold_position == 4:
                room = "entrance"
                print("You return to the entrance room.")
                print()
            else:
                print("Invalid entry, please enter again.")

        except ValueError:
            print("Invalid entry, please enter again.")
            print()