import tkinter as tk
import random
Tic = tk.Tk()

GAME_ARRAY = [['0','0','0'],['0','0','0'],['0','0','0']]

def print_array():
    for i in GAME_ARRAY:
        print(i)

def option():
    value = input("if you want to play multiplayer enter 1 else if you want to play with bot press 0: ")
    while value != '0' and value != '1':
        print("please enter a correct value")
        value = input("if you want to play multiplayer enter 1 else if you want to play with bot press 0: ")
    if value == '0':
        game_main()
    else:
        call_multiplayer()

def call_bot():
    global GAME_ARRAY
    x = random.randint(0,2)
    y = random.randint(0,2)
    while GAME_ARRAY[x][y] != '0':
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    GAME_ARRAY[x][y] = "X"

def call_multiplayer():
    return 1

def your_option():
    x = int(input("PLease enter the X co-ordinate: "))
    y = int(input("PLease enter the Y co-ordinate: "))
    while True:
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Invalid coordinates. Both coordinates must be 0, 1, or 2.")
        elif GAME_ARRAY[x][y] != '0' and GAME_ARRAY[x][y] != 'X':
            print("Sign already exists there.")
        else:
            break
        x = int(input("Please enter the X coordinate (0, 1, or 2): "))
        y = int(input("Please enter the Y coordinate (0, 1, or 2): "))
    GAME_ARRAY[x][y] = "U"

def player_one_won():

    for i in range(3):
        if all(GAME_ARRAY[i][j] == 'X' for j in range(3)):
            print("Bot win")
            return True

    for j in range(3):
        if all(GAME_ARRAY[i][j] == 'X' for i in range(3)):
            print("Bot win")
            return True

    if (GAME_ARRAY[0][0] == 'X' and GAME_ARRAY[1][1] == 'X' and GAME_ARRAY[2][2] == 'X') or \
            (GAME_ARRAY[0][2] == 'X' and GAME_ARRAY[1][1] == 'X' and GAME_ARRAY[2][0] == 'X'):
        print("Bot win")
        return True

    return False


def bot_won():
    for i in range(3):
        if all(GAME_ARRAY[i][j] == 'U' for j in range(3)):
            print("You win")
            return True

    for j in range(3):
        if all(GAME_ARRAY[i][j] == 'U' for i in range(3)):
            print("You win")
            return True

    if (GAME_ARRAY[0][0] == 'U' and GAME_ARRAY[1][1] == 'U' and GAME_ARRAY[2][2] == 'U') or \
            (GAME_ARRAY[0][2] == 'U' and GAME_ARRAY[1][1] == 'U' and GAME_ARRAY[2][0] == 'U'):
        print("You0 win")
        return True

    return False

def game_main():
    print_array()
    while player_one_won() == False and bot_won() == False:
        print("its your turn")
        your_option()
        print_array()
        print("")
        print("its bot's turn")
        call_bot()
        print_array()
        print("")

option()
