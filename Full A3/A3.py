# Author: Eddy Qiang
# Student ID: 30058191
# CPSC 231-T01

"""
Patch History:
Date               Version                Notes
May 16, 2017       Ver. 1.0.0             initial creation
May 27, 2017       Ver. 1.0.1             added three new rooms
June 02, 2017      Ver. 1.0.2             reorganized code into functions
June 07, 2017      Ver. 1.0.3             add more functions, refined code
"""

"""
A text-based "choose your own" adventure game. There are six rooms 
in the game world, within each room the player will see a number of 
choices and the program will react to the player's decision. The goal
of this game is to try to unlock a inner door and then find paradise. 
The door will only be unlocked if the player turns the key silver lock 
in the pantry to the "right" position and the key gold lock in the kitchen 
to the "left" position. Upon opening the door, the player has to look 
around and interact with various things to find paradise. The only way
to reach paradise is to fertilize the pot of soil by feeding cheese to 
the mouse after picking up cheese, and picking up a ball of string and 
dropping it down the hole. Once the player reaches paradise the game ends 
and a congratulatory message is displayed.
"""

# display entrance options
def print_entrance_menu():
    print("You are now at the entrance room.\n")
    print("1. Try to open the door")
    print("2. Go through the left entry way")
    print("3. Go through the right entry way")
# moves player to entrance room
def move_to_entrance():
    room = "entrance"
    return room
# inner door logic
def open_inner_door(silver_lock, gold_lock):
    print("You try to open the door and...")
    if (silver_lock == "right") and (gold_lock == "left"):
        room = "living_room"
        print("The door unlocks. Congratulations!")
        print_game_intro2()
        return room
    else:
        room = "entrance"
        print("The door won't budge!\n")
        return room
# display kitchen lock position
def print_kitchen_intro(gold_lock):
    print("You are now at the kitchen, and you see a gold lock.")
    print("The gold lock is currently in the", gold_lock, "position.\n")
# display kitchen options
def print_kitchen_menu():
    print("1. Turn the gold lock to the left position")
    print("2. Turn the gold lock to the right position")
    print("3. Turn the gold lock to the center position")
    print("4. Don't change the position! Return to entrance way")
# moves player to kitchen
def move_to_kitchen():
    room = "kitchen"
    return room
# sets gold lock positions
def gold_lock_position(decision):
    if decision == 1:
        print("The gold lock is now set to the left position\n")
        gold_lock = "left"
        return gold_lock
    elif decision == 2:
        print("The gold lock is now set to the right position\n")
        gold_lock = "right"
        return gold_lock
    elif decision == 3:
        print("The gold lock is now set to the center position\n")
        gold_lock = "center"
        return gold_lock
# display pantry lock position
def print_pantry_intro(silver_lock):
    print("You are now at the pantry, and you see a silver lock.")
    print("The silver lock is currently in the", silver_lock, "position.\n")
# display pantry options
def print_pantry_menu():
    print("1. Turn the silver lock to the left position")
    print("2. Turn the silver lock to the right position")
    print("3. Turn the silver lock to the center position")
    print("4. Don't change the position! Return to entrance way")
# moves player to pantry
def move_to_pantry():
    room = "pantry"
    return room
# sets silver lock positions
def silver_lock_position(decision):
    if decision == 1:
        print("The silver lock is now set to the left position\n")
        silver_lock = "left"
        return silver_lock
    elif decision == 2:
        print("The silver lock is now set to the right position\n")
        silver_lock = "right"
        return silver_lock
    elif decision == 3:
        print("The silver lock is now set to the center position\n")
        silver_lock = "center"
        return silver_lock
# display living room options
def print_living_room_menu(ball_of_string_available):
    print("You are now at the living room.")
    if ball_of_string_available == True:
        print("You see a ball of string on the floor")
    print("1. View the pot of soil")
    print("2. Walk up stairs")
    print("3. Go through the dark entrance way")
    if ball_of_string_available == True:
        print("4. Pick up a ball of string")
# moves player to living room
def move_to_living_room():
    room = "living_room"
    return room
# pot of soil logic and win condition
def check_win_condition(pot_of_soil_dry):
    print("You view the pot of soil...")
    if pot_of_soil_dry == True:
        room = "living_room"
        print("The pot of soil looks dry\n")
        return room
    else:
        print("A vine grows out of the pot and takes you to paradise.")
        print("Congratulations!")
        game_won = True
# display attic options
def print_attic_menu(have_cheese):
    print("You are now in the attic.\n")
    print("You see cheese on the ground as well as a hole in the ground.")
    print("1. Pick up cheese")
    if have_cheese == True:
        print("2. Drop cheese down the hole")
    print("3. Walk down the stairs")
# moves player to attic
def move_to_attic():
    room = "attic"
    return room
# picking up cheese
def pick_up_cheese():
    print("You picked up some cheese\n")
    have_cheese = True
    return have_cheese
# dropping cheese
def drop_cheese(have_cheese):
    print("You attempt to drop cheese down the hole and you find that")
    if have_cheese == True:
        print("The cheese is too big\n")
    else:
        print("You do not have any cheese on you")
# display bedroom desciption
def print_bedroom_intro(string_dropped):
    print("You are now at the bedroom.")
    if string_dropped == True:
        print("The cat has left the room due to the large distraction motion of the string,\nand you see a mouse")
    else:
        print("You noticed there is a mouse in the mouse hole and you see a cat watching the mouse hole\n")
# moves player to bedroom
def move_to_bedroom():
    room = "bedroom"
    return room
# display bedroom options
def print_bedroom_menu(have_ball_of_string, string_dropped, have_cheese):
    print("1. Go back through the dark entrance way")
    if (have_ball_of_string == True) and (string_dropped == False):
        print("2. Play with the cat using the string")
    if (have_ball_of_string == False) and (string_dropped == True) and (have_cheese == True):
        print("3. Feed cheese to the mouse")
# play with cat
def interact_with_cat():
    print("The cat briefly looks at you and then goes back to watching the mouse hole\n")
# feed mouse
def feed_mouse():
    print("You fed the mouse some cheese, the mouse leaves the room and returns after a moment\n")
    pot_of_soil_dry = False
    return pot_of_soil_dry
# prompt user for input
def ask_for_input():
    decision = int(input("What would you like to do? Enter choice number: \n"))
    return decision
# display input error
def display_error():
    print("Invalid entry, please enter again.\n")
# displays  part one game introduction
def print_game_intro():
    print("""
You have just stepped into the entrance room through the outer door.
The door you came through magically vanishes behind you. In front of
you there is a inner door, one room to your left, and one room to your
right.\n""")
# displays part two game introduction
def print_game_intro2():
    print("""
You have just stepped through the inner door taking you from the entrance 
room through to the living room. The door you came through magically vanishes 
behind you. In the living room you see a pot of soil, stairs going up, and
a dark entrance way.\n""")
# entrance room option selection
def entrance(silver_lock, gold_lock):
    OPEN_DOOR = 1
    MOVE_TO_KITCHEN = 2
    MOVE_TO_PANTRY = 3
    # input validation loop
    try:
        validity = False
        while validity == False:
            print_entrance_menu()
            decision = ask_for_input()
            if decision in range(1, 4):
                validity = True
            else:
                display_error()
        # decision logic
        if decision == OPEN_DOOR:
            room = open_inner_door(silver_lock, gold_lock)
            return room
        elif decision == MOVE_TO_KITCHEN:
            room = move_to_kitchen()
            return room
        elif decision == MOVE_TO_PANTRY:
            room = move_to_pantry()
            return room
        else:
            display_error()
    except ValueError:
        display_error()
# pantry room option selection
def pantry():
    # input validation loop
    try:
        validity = False
        while validity == False:
            print_pantry_menu()
            decision = ask_for_input()
            if decision in range(1, 5):
                validity = True
                return decision
            else:
                display_error()
    except ValueError:
        display_error()
# kitchen room option selection
def kitchen():
    # input validation loop
    try:
        validity = False
        while validity == False:
            print_kitchen_menu()
            decision = ask_for_input()
            if decision in range(1, 5):
                validity = True
                return decision
            else:
                display_error()
    except ValueError:
        display_error()
# living room option selection
def living_room():
    # input validation loop
    try:
        validity = False
        while validity == False:
            decision = ask_for_input()
            if decision in range(1, 6):
                validity = True
                return decision
            else:
                display_error()
    except ValueError:
        display_error()
# attic option selection
def attic(have_ball_of_string, have_cheese):
    # input validation loop
    try:
        validity = False
        while validity == False:
            print_attic_menu(have_cheese)
            if have_ball_of_string == True:
                print("4. Drop the string down the hole")
            decision = ask_for_input()
            if decision in range(1, 5):
                validity = True
                return decision
            else:
                display_error()
    except ValueError:
        display_error()
# bedroom option selection
def bedroom(have_ball_of_string, string_dropped, have_cheese):
    # input validation loop
    try:
        validity = False
        while validity == False:
            print_bedroom_menu(have_ball_of_string, string_dropped, have_cheese)
            decision = ask_for_input()
            if decision in range(1, 4):
                validity = True
                return decision
            else:
                display_error()
    except ValueError:
        display_error()

# starting function
def main():
    print_game_intro()
    # initialize game settings and variable
    room = "entrance"
    gold_lock = "left"
    silver_lock = "right"
    inner_door_locked = True
    ball_of_string_available = True
    pot_of_soil_dry = True
    have_ball_of_string = False
    have_cheese = False
    string_dropped = False
    path_to_paradise = False
    game_won = False
    MOVE_TO_ENTRANCE = 4
    VIEW_SOIL = 1
    MOVE_TO_ATTIC = 2
    MOVE_TO_BEDROOM = 3
    PICK_UP_STRING =4
    DROP_STRING = 4
    PICK_UP_CHEESE = 1
    DROP_CHEESE = 2
    MOVE_TO_LIVING_ROOM = 3
    MOVE_BACK = 1
    INTERACT_WITH_CAT = 2
    FEED_MOUSE = 3

    # main game loop
    while game_won == False:
        # entrance room
        if room == "entrance":
            room = entrance(silver_lock, gold_lock)
        # pantry
        elif room == "pantry":
            print_pantry_intro(silver_lock)
            decision = pantry()
            if decision in range(1,4):
                silver_lock = silver_lock_position(decision)
            elif decision == MOVE_TO_ENTRANCE:
                room = move_to_entrance()
            else:
                display_error()
        # kitchen
        elif room == "kitchen":
            print_kitchen_intro(gold_lock)
            decision = kitchen()
            if decision in range(1,4):
                gold_lock = gold_lock_position(decision)
            elif decision == MOVE_TO_ENTRANCE:
                room = move_to_entrance()
            else:
                display_error()
        # living
        elif room == "living_room":
            print_living_room_menu(ball_of_string_available)
            decision = living_room()
            if decision == VIEW_SOIL:
                room = check_win_condition(pot_of_soil_dry)
            elif decision == MOVE_TO_ATTIC:
                room = move_to_attic()
            elif decision == MOVE_TO_BEDROOM:
                room = move_to_bedroom()
            elif decision == PICK_UP_STRING:
                if ball_of_string_available == True:
                    print("You picked up the ball of string\n")
                    ball_of_string_available = False
                    have_ball_of_string = True
                else:
                    display_error()
            else:
                display_error()
        # attic
        elif room == "attic":
            decision = attic(have_ball_of_string, have_cheese)
            if decision == PICK_UP_CHEESE:
                have_cheese = pick_up_cheese()
            elif (decision == DROP_CHEESE) and (have_cheese == True):
                drop_cheese(have_cheese)
            elif decision == MOVE_TO_LIVING_ROOM:
                room = move_to_living_room()
            elif (decision == DROP_STRING) and (have_ball_of_string == True):
                print("You dropped the string down the hole\n")
                have_ball_of_string = False
                string_dropped = True
            else:
                display_error()
        # bedroom
        elif room == "bedroom":
            print_bedroom_intro(string_dropped)
            decision = bedroom(have_ball_of_string, string_dropped, have_cheese)
            if decision == MOVE_BACK:
                room = move_to_living_room()
            elif (decision == INTERACT_WITH_CAT) and (have_ball_of_string == True):
                interact_with_cat()
            elif (decision == FEED_MOUSE) and (have_cheese == True) and (string_dropped == True):
                pot_of_soil_dry = feed_mouse()
            else:
                display_error()

main()