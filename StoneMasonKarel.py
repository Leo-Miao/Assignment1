from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Karel is now standing at (1,1), after the program,
    Karel will fill up the "bridges" with beepers.
    """
    for i in range(2):
        fill_row()
        move_up1()
        fill_row()
        move_up2()
    fill_row()


def fill_row():
    if beepers_present():
        pass
    else:
        put_beeper()
    for i in range(3):
        for i in range(4):
            move()
        if beepers_present():
            pass
        else:
            put_beeper()


def move_up1():
    turn_left()
    move()
    turn_left()


def move_up2():
    turn_right()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
