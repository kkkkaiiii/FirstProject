"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beeper()
    move_back()
    go_home()

def double_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()

def turn_around():
    turn_left()
    turn_left()

def move_back():
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        pick_beeper()
        turn_around()()
        move()

def go_home():
    turn_around()()
    move()
    move()
    turn_around()















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)