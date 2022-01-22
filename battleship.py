from math import ceil # # # Imported ceil to round the damage percentage into an estimate.
from time import sleep # # # Imported sleep from time to pause between actions.

ships = { # # # A dictionary to map ship choices to their lengths.
    "DESTROYER": "2",
    "SUBMARINE": "3",
    "CRUISER": "3",
    "BATTLESHIP": "4",
    "CARRIER": "5"
}

letter_to_num = { # # # A dictionary to map letters to their numbers
    "A": "1",
    "B": "2",
    "C": "3",
    "D": "4",
    "E": "5",
    "F": "6",
    "G": "7",
    "H": "8",
    "I": "9",
    "J": "10",
}
ships_used = [] # # # A list to hold ships used for player one, ships_used2 is the same for player two.
ships_used2 = []
ships_avail = ['Destroyer (2)', 'Submarine (3)', 'Cruiser (3)', 'Battleship (4)', 'Carrier (5)'
               ] # # # A list used to display the ship selection menu, ship_choice is removed from this when successful placement occurs. ships_avail2 is the same for player two.
ships_avail2 = ['Destroyer (2)', 'Submarine (3)', 'Cruiser (3)', 'Battleship (4)', 'Carrier (5)'
                ]
ship_length = 0 # # # Stores the length of the selected ship for determining placement.
p1_health = 17 # # # Player one health, the total number of ship spaces taken up when all are placed is 17, and when all of yours are hit you run out of health. (The same for p2_health)
p2_health = 17
current_player = 1 # # # Used to determine whose turn it is.
up_down_left_right = '' # # # Used to store the direction the current player wants the ship to go in from their given starting position.
loc1 = 0 # # # The first value taken from their given position, can be one of the ten rows. (Translated from letter to number.)
loc2 = 0 # # # The second value taken from their given position, can be one of ten columns. (The number value in 'A1')
ship_choice = '' # # # Stores the ship chosen by the player.

# -------------------------------------------------------------------------------------------------------------------- #
# # # These four lists store the boards for... 

    # player one's ships, 
b_p = [
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
]
    # player one's hits/misses, 
m_p = [
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
]
    # player two's ships, and 
b_p2 = [
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
]
    # player two's hits/misses respectively.
m_p2 = [
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
    ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
]
# -------------------------------------------------------------------------------------------------------------------- #


# # # Prints player one's ship board in a viewer friendly manner.
def print_bp():
    global b_p
    print(
        f'  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| \n'
        f'A | {b_p[0][0]} | {b_p[0][1]} | {b_p[0][2]} | {b_p[0][3]} | {b_p[0][4]} | {b_p[0][5]} | {b_p[0][6]} | {b_p[0][7]} | {b_p[0][8]} | {b_p[0][9]} |\n'
        f'B | {b_p[1][0]} | {b_p[1][1]} | {b_p[1][2]} | {b_p[1][3]} | {b_p[1][4]} | {b_p[1][5]} | {b_p[1][6]} | {b_p[1][7]} | {b_p[1][8]} | {b_p[1][9]} |\n'
        f'C | {b_p[2][0]} | {b_p[2][1]} | {b_p[2][2]} | {b_p[2][3]} | {b_p[2][4]} | {b_p[2][5]} | {b_p[2][6]} | {b_p[2][7]} | {b_p[2][8]} | {b_p[2][9]} |\n'
        f'D | {b_p[3][0]} | {b_p[3][1]} | {b_p[3][2]} | {b_p[3][3]} | {b_p[3][4]} | {b_p[3][5]} | {b_p[3][6]} | {b_p[3][7]} | {b_p[3][8]} | {b_p[3][9]} |\n'
        f'E | {b_p[4][0]} | {b_p[4][1]} | {b_p[4][2]} | {b_p[4][3]} | {b_p[4][4]} | {b_p[4][5]} | {b_p[4][6]} | {b_p[4][7]} | {b_p[4][8]} | {b_p[4][9]} |\n'
        f'F | {b_p[5][0]} | {b_p[5][1]} | {b_p[5][2]} | {b_p[5][3]} | {b_p[5][4]} | {b_p[5][5]} | {b_p[5][6]} | {b_p[5][7]} | {b_p[5][8]} | {b_p[5][9]} |\n'
        f'G | {b_p[6][0]} | {b_p[6][1]} | {b_p[6][2]} | {b_p[6][3]} | {b_p[6][4]} | {b_p[6][5]} | {b_p[6][6]} | {b_p[6][7]} | {b_p[6][8]} | {b_p[6][9]} |\n'
        f'H | {b_p[7][0]} | {b_p[7][1]} | {b_p[7][2]} | {b_p[7][3]} | {b_p[7][4]} | {b_p[7][5]} | {b_p[7][6]} | {b_p[7][7]} | {b_p[7][8]} | {b_p[7][9]} |\n'
        f'I | {b_p[8][0]} | {b_p[8][1]} | {b_p[8][2]} | {b_p[8][3]} | {b_p[8][4]} | {b_p[8][5]} | {b_p[8][6]} | {b_p[8][7]} | {b_p[8][8]} | {b_p[8][9]} |\n'
        f'J | {b_p[9][0]} | {b_p[9][1]} | {b_p[9][2]} | {b_p[9][3]} | {b_p[9][4]} | {b_p[9][5]} | {b_p[9][6]} | {b_p[9][7]} | {b_p[9][8]} | {b_p[9][9]} |\n')


# # # Prints player two's ship board in a viewer friendly manner.
def print_bp2():
    global b_p2
    print(
        f'  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| \n'
        f'A | {b_p2[0][0]} | {b_p2[0][1]} | {b_p2[0][2]} | {b_p2[0][3]} | {b_p2[0][4]} | {b_p2[0][5]} | {b_p2[0][6]} | {b_p2[0][7]} | {b_p2[0][8]} | {b_p2[0][9]} |\n'
        f'B | {b_p2[1][0]} | {b_p2[1][1]} | {b_p2[1][2]} | {b_p2[1][3]} | {b_p2[1][4]} | {b_p2[1][5]} | {b_p2[1][6]} | {b_p2[1][7]} | {b_p2[1][8]} | {b_p2[1][9]} |\n'
        f'C | {b_p2[2][0]} | {b_p2[2][1]} | {b_p2[2][2]} | {b_p2[2][3]} | {b_p2[2][4]} | {b_p2[2][5]} | {b_p2[2][6]} | {b_p2[2][7]} | {b_p2[2][8]} | {b_p2[2][9]} |\n'
        f'D | {b_p2[3][0]} | {b_p2[3][1]} | {b_p2[3][2]} | {b_p2[3][3]} | {b_p2[3][4]} | {b_p2[3][5]} | {b_p2[3][6]} | {b_p2[3][7]} | {b_p2[3][8]} | {b_p2[3][9]} |\n'
        f'E | {b_p2[4][0]} | {b_p2[4][1]} | {b_p2[4][2]} | {b_p2[4][3]} | {b_p2[4][4]} | {b_p2[4][5]} | {b_p2[4][6]} | {b_p2[4][7]} | {b_p2[4][8]} | {b_p2[4][9]} |\n'
        f'F | {b_p2[5][0]} | {b_p2[5][1]} | {b_p2[5][2]} | {b_p2[5][3]} | {b_p2[5][4]} | {b_p2[5][5]} | {b_p2[5][6]} | {b_p2[5][7]} | {b_p2[5][8]} | {b_p2[5][9]} |\n'
        f'G | {b_p2[6][0]} | {b_p2[6][1]} | {b_p2[6][2]} | {b_p2[6][3]} | {b_p2[6][4]} | {b_p2[6][5]} | {b_p2[6][6]} | {b_p2[6][7]} | {b_p2[6][8]} | {b_p2[6][9]} |\n'
        f'H | {b_p2[7][0]} | {b_p2[7][1]} | {b_p2[7][2]} | {b_p2[7][3]} | {b_p2[7][4]} | {b_p2[7][5]} | {b_p2[7][6]} | {b_p2[7][7]} | {b_p2[7][8]} | {b_p2[7][9]} |\n'
        f'I | {b_p2[8][0]} | {b_p2[8][1]} | {b_p2[8][2]} | {b_p2[8][3]} | {b_p2[8][4]} | {b_p2[8][5]} | {b_p2[8][6]} | {b_p2[8][7]} | {b_p2[8][8]} | {b_p2[8][9]} |\n'
        f'J | {b_p2[9][0]} | {b_p2[9][1]} | {b_p2[9][2]} | {b_p2[9][3]} | {b_p2[9][4]} | {b_p2[9][5]} | {b_p2[9][6]} | {b_p2[9][7]} | {b_p2[9][8]} | {b_p2[9][9]} |\n')


# # # Prints player one's hit/miss board in a viewer friendly manner.
def print_bp_mp():
    global b_p, m_p, m_p2
    print(
        f'               Your Ships                     |                   Your Shots                 \n'
        f'-------------------------------------------   |   -------------------------------------------\n'
        f'  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|   |     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|\n'
        f'A | {b_p[0][0]} | {b_p[0][1]} | {b_p[0][2]} | {b_p[0][3]} | {b_p[0][4]} | {b_p[0][5]} | {b_p[0][6]} | {b_p[0][7]} | {b_p[0][8]} | {b_p[0][9]} |   |   A | {m_p[0][0]} | {m_p[0][1]} | {m_p[0][2]} | {m_p[0][3]} | {m_p[0][4]} | {m_p[0][5]} | {m_p[0][6]} | {m_p[0][7]} | {m_p[0][8]} | {m_p[0][9]} |\n'
        f'B | {b_p[1][0]} | {b_p[1][1]} | {b_p[1][2]} | {b_p[1][3]} | {b_p[1][4]} | {b_p[1][5]} | {b_p[1][6]} | {b_p[1][7]} | {b_p[1][8]} | {b_p[1][9]} |   |   B | {m_p[1][0]} | {m_p[1][1]} | {m_p[1][2]} | {m_p[1][3]} | {m_p[1][4]} | {m_p[1][5]} | {m_p[1][6]} | {m_p[1][7]} | {m_p[1][8]} | {m_p[1][9]} |\n'
        f'C | {b_p[2][0]} | {b_p[2][1]} | {b_p[2][2]} | {b_p[2][3]} | {b_p[2][4]} | {b_p[2][5]} | {b_p[2][6]} | {b_p[2][7]} | {b_p[2][8]} | {b_p[2][9]} |   |   C | {m_p[2][0]} | {m_p[2][1]} | {m_p[2][2]} | {m_p[2][3]} | {m_p[2][4]} | {m_p[2][5]} | {m_p[2][6]} | {m_p[2][7]} | {m_p[2][8]} | {m_p[2][9]} |\n'
        f'D | {b_p[3][0]} | {b_p[3][1]} | {b_p[3][2]} | {b_p[3][3]} | {b_p[3][4]} | {b_p[3][5]} | {b_p[3][6]} | {b_p[3][7]} | {b_p[3][8]} | {b_p[3][9]} |   |   D | {m_p[3][0]} | {m_p[3][1]} | {m_p[3][2]} | {m_p[3][3]} | {m_p[3][4]} | {m_p[3][5]} | {m_p[3][6]} | {m_p[3][7]} | {m_p[3][8]} | {m_p[3][9]} |\n'
        f'E | {b_p[4][0]} | {b_p[4][1]} | {b_p[4][2]} | {b_p[4][3]} | {b_p[4][4]} | {b_p[4][5]} | {b_p[4][6]} | {b_p[4][7]} | {b_p[4][8]} | {b_p[4][9]} |   |   E | {m_p[4][0]} | {m_p[4][1]} | {m_p[4][2]} | {m_p[4][3]} | {m_p[4][4]} | {m_p[4][5]} | {m_p[4][6]} | {m_p[4][7]} | {m_p[4][8]} | {m_p[4][9]} |\n'
        f'F | {b_p[5][0]} | {b_p[5][1]} | {b_p[5][2]} | {b_p[5][3]} | {b_p[5][4]} | {b_p[5][5]} | {b_p[5][6]} | {b_p[5][7]} | {b_p[5][8]} | {b_p[5][9]} |   |   F | {m_p[5][0]} | {m_p[5][1]} | {m_p[5][2]} | {m_p[5][3]} | {m_p[5][4]} | {m_p[5][5]} | {m_p[5][6]} | {m_p[5][7]} | {m_p[5][8]} | {m_p[5][9]} |\n'
        f'G | {b_p[6][0]} | {b_p[6][1]} | {b_p[6][2]} | {b_p[6][3]} | {b_p[6][4]} | {b_p[6][5]} | {b_p[6][6]} | {b_p[6][7]} | {b_p[6][8]} | {b_p[6][9]} |   |   G | {m_p[6][0]} | {m_p[6][1]} | {m_p[6][2]} | {m_p[6][3]} | {m_p[6][4]} | {m_p[6][5]} | {m_p[6][6]} | {m_p[6][7]} | {m_p[6][8]} | {m_p[6][9]} |\n'
        f'H | {b_p[7][0]} | {b_p[7][1]} | {b_p[7][2]} | {b_p[7][3]} | {b_p[7][4]} | {b_p[7][5]} | {b_p[7][6]} | {b_p[7][7]} | {b_p[7][8]} | {b_p[7][9]} |   |   H | {m_p[7][0]} | {m_p[7][1]} | {m_p[7][2]} | {m_p[7][3]} | {m_p[7][4]} | {m_p[7][5]} | {m_p[7][6]} | {m_p[7][7]} | {m_p[7][8]} | {m_p[7][9]} |\n'
        f'I | {b_p[8][0]} | {b_p[8][1]} | {b_p[8][2]} | {b_p[8][3]} | {b_p[8][4]} | {b_p[8][5]} | {b_p[8][6]} | {b_p[8][7]} | {b_p[8][8]} | {b_p[8][9]} |   |   I | {m_p[8][0]} | {m_p[8][1]} | {m_p[8][2]} | {m_p[8][3]} | {m_p[8][4]} | {m_p[8][5]} | {m_p[8][6]} | {m_p[8][7]} | {m_p[8][8]} | {m_p[8][9]} |\n'
        f'J | {b_p[9][0]} | {b_p[9][1]} | {b_p[9][2]} | {b_p[9][3]} | {b_p[9][4]} | {b_p[9][5]} | {b_p[9][6]} | {b_p[9][7]} | {b_p[9][8]} | {b_p[9][9]} |   |   J | {m_p[9][0]} | {m_p[9][1]} | {m_p[9][2]} | {m_p[9][3]} | {m_p[9][4]} | {m_p[9][5]} | {m_p[9][6]} | {m_p[9][7]} | {m_p[9][8]} | {m_p[9][9]} |\n'
        f'-------------------------------------------   |   -------------------------------------------\n')


# # # Prints player two's hit/miss board in a viewer friendly manner.
def print_bp_mp2():
    global b_p2, m_p2, m_p
    print(
        f'               Your Ships                     |                   Your Shots                 \n'
        f'-------------------------------------------   |   -------------------------------------------\n'
        f'  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|   |     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|\n'
        f'A | {b_p2[0][0]} | {b_p2[0][1]} | {b_p2[0][2]} | {b_p2[0][3]} | {b_p2[0][4]} | {b_p2[0][5]} | {b_p2[0][6]} | {b_p2[0][7]} | {b_p2[0][8]} | {b_p2[0][9]} |   |   A | {m_p2[0][0]} | {m_p2[0][1]} | {m_p2[0][2]} | {m_p2[0][3]} | {m_p2[0][4]} | {m_p2[0][5]} | {m_p2[0][6]} | {m_p2[0][7]} | {m_p2[0][8]} | {m_p2[0][9]} |\n'
        f'B | {b_p2[1][0]} | {b_p2[1][1]} | {b_p2[1][2]} | {b_p2[1][3]} | {b_p2[1][4]} | {b_p2[1][5]} | {b_p2[1][6]} | {b_p2[1][7]} | {b_p2[1][8]} | {b_p2[1][9]} |   |   B | {m_p2[1][0]} | {m_p2[1][1]} | {m_p2[1][2]} | {m_p2[1][3]} | {m_p2[1][4]} | {m_p2[1][5]} | {m_p2[1][6]} | {m_p2[1][7]} | {m_p2[1][8]} | {m_p2[1][9]} |\n'
        f'C | {b_p2[2][0]} | {b_p2[2][1]} | {b_p2[2][2]} | {b_p2[2][3]} | {b_p2[2][4]} | {b_p2[2][5]} | {b_p2[2][6]} | {b_p2[2][7]} | {b_p2[2][8]} | {b_p2[2][9]} |   |   C | {m_p2[2][0]} | {m_p2[2][1]} | {m_p2[2][2]} | {m_p2[2][3]} | {m_p2[2][4]} | {m_p2[2][5]} | {m_p2[2][6]} | {m_p2[2][7]} | {m_p2[2][8]} | {m_p2[2][9]} |\n'
        f'D | {b_p2[3][0]} | {b_p2[3][1]} | {b_p2[3][2]} | {b_p2[3][3]} | {b_p2[3][4]} | {b_p2[3][5]} | {b_p2[3][6]} | {b_p2[3][7]} | {b_p2[3][8]} | {b_p2[3][9]} |   |   D | {m_p2[3][0]} | {m_p2[3][1]} | {m_p2[3][2]} | {m_p2[3][3]} | {m_p2[3][4]} | {m_p2[3][5]} | {m_p2[3][6]} | {m_p2[3][7]} | {m_p2[3][8]} | {m_p2[3][9]} |\n'
        f'E | {b_p2[4][0]} | {b_p2[4][1]} | {b_p2[4][2]} | {b_p2[4][3]} | {b_p2[4][4]} | {b_p2[4][5]} | {b_p2[4][6]} | {b_p2[4][7]} | {b_p2[4][8]} | {b_p2[4][9]} |   |   E | {m_p2[4][0]} | {m_p2[4][1]} | {m_p2[4][2]} | {m_p2[4][3]} | {m_p2[4][4]} | {m_p2[4][5]} | {m_p2[4][6]} | {m_p2[4][7]} | {m_p2[4][8]} | {m_p2[4][9]} |\n'
        f'F | {b_p2[5][0]} | {b_p2[5][1]} | {b_p2[5][2]} | {b_p2[5][3]} | {b_p2[5][4]} | {b_p2[5][5]} | {b_p2[5][6]} | {b_p2[5][7]} | {b_p2[5][8]} | {b_p2[5][9]} |   |   F | {m_p2[5][0]} | {m_p2[5][1]} | {m_p2[5][2]} | {m_p2[5][3]} | {m_p2[5][4]} | {m_p2[5][5]} | {m_p2[5][6]} | {m_p2[5][7]} | {m_p2[5][8]} | {m_p2[5][9]} |\n'
        f'G | {b_p2[6][0]} | {b_p2[6][1]} | {b_p2[6][2]} | {b_p2[6][3]} | {b_p2[6][4]} | {b_p2[6][5]} | {b_p2[6][6]} | {b_p2[6][7]} | {b_p2[6][8]} | {b_p2[6][9]} |   |   G | {m_p2[6][0]} | {m_p2[6][1]} | {m_p2[6][2]} | {m_p2[6][3]} | {m_p2[6][4]} | {m_p2[6][5]} | {m_p2[6][6]} | {m_p2[6][7]} | {m_p2[6][8]} | {m_p2[6][9]} |\n'
        f'H | {b_p2[7][0]} | {b_p2[7][1]} | {b_p2[7][2]} | {b_p2[7][3]} | {b_p2[7][4]} | {b_p2[7][5]} | {b_p2[7][6]} | {b_p2[7][7]} | {b_p2[7][8]} | {b_p2[7][9]} |   |   H | {m_p2[7][0]} | {m_p2[7][1]} | {m_p2[7][2]} | {m_p2[7][3]} | {m_p2[7][4]} | {m_p2[7][5]} | {m_p2[7][6]} | {m_p2[7][7]} | {m_p2[7][8]} | {m_p2[7][9]} |\n'
        f'I | {b_p2[8][0]} | {b_p2[8][1]} | {b_p2[8][2]} | {b_p2[8][3]} | {b_p2[8][4]} | {b_p2[8][5]} | {b_p2[8][6]} | {b_p2[8][7]} | {b_p2[8][8]} | {b_p2[8][9]} |   |   I | {m_p2[8][0]} | {m_p2[8][1]} | {m_p2[8][2]} | {m_p2[8][3]} | {m_p2[8][4]} | {m_p2[8][5]} | {m_p2[8][6]} | {m_p2[8][7]} | {m_p2[8][8]} | {m_p2[8][9]} |\n'
        f'J | {b_p2[9][0]} | {b_p2[9][1]} | {b_p2[9][2]} | {b_p2[9][3]} | {b_p2[9][4]} | {b_p2[9][5]} | {b_p2[9][6]} | {b_p2[9][7]} | {b_p2[9][8]} | {b_p2[9][9]} |   |   J | {m_p2[9][0]} | {m_p2[9][1]} | {m_p2[9][2]} | {m_p2[9][3]} | {m_p2[9][4]} | {m_p2[9][5]} | {m_p2[9][6]} | {m_p2[9][7]} | {m_p2[9][8]} | {m_p2[9][9]} |\n'
        f'-------------------------------------------   |   -------------------------------------------\n')


# # # Takes the direction chosen by the current player, and uses global variables loc1, loc2, and ship_choice to
    # determine whether their move is legal, if it is not, it returns the "True" value.
    # An illegal move is one that tries to cross outside of the playable bounds, or one that tries to intersect another ship.
def illegal_move(up_down_left_right): 
    global loc1, loc2, ship_choice, current_player

    # # # If user-chosen direction is down, check for ship pieces blocking the way. [loc1 + x] to check the given column
    if up_down_left_right == 'DOWN':
        if current_player == 1: # # # If it's player one's turn, check their board in the down direction for as many
                                # spaces as their ship is long. If any of those spaces is equal to '>' (ship piece)
                                # move is illegal, return true.
            for x in range(ship_length):
                if b_p[loc1 + x][loc2] == '>':
                    return True
        else:                   # # # If it's not player one's turn, check the same for player two.
            for x in range(ship_length):
                if b_p2[loc1 + x][loc2] == '<':
                    return True
    # # # Does the same as the 'DOWN' check, but in the 'UP' direction. ([loc1 - x] to check column in 'UP' direction.)
    elif up_down_left_right == 'UP':
        if current_player == 1:
            for x in range(ship_length):
                if b_p[loc1 - x][loc2] == '>':
                    return True
        else:
            for x in range(ship_length):
                if b_p2[loc1 - x][loc2] == '<':
                    return True
    # # # Does the same as the 'DOWN' check, but in the 'RIGHT' direction. ([loc1] is not longer begin checked,
    # as we're checking rows, not columns. Thus, [loc2 + x] for the 'RIGHT' direction.)
    elif up_down_left_right == 'RIGHT':
        if current_player == 1:
            for x in range(loc2 - ship_length):
                print(loc1, loc2, x)
                if b_p[loc1][loc2 + x] == '>':
                    return True
        else:
            for x in range(loc2 - ship_length):
                print(loc1, loc2, x)
                if b_p2[loc1][loc2 + x] == '<':
                    return True
    # # # Does the same as the 'DOWN' check, but in the 'LEFT' direction. ([loc1] is not longer begin checked,
    # as we're checking rows, not columns. Thus, [loc2 - x] for the 'LEFT' direction.)
    elif up_down_left_right == 'LEFT':
        if current_player == 1:
            for x in range(ship_length):
                if b_p[loc1][loc2 - x] == '>':
                    return True
        else:
            for x in range(ship_length):
                if b_p2[loc1][loc2 - x] == '<':
                    return True
    # # # If the ship is the destroyer (2 spaces long) and is in row A or J, or in column 1 or 10, AND the direction is
    # not allowed for that position, return True for illegal_move
    if ship_length == 2:
        if loc1 == 0 and up_down_left_right == 'UP':
            return True
        if loc1 == 9 and up_down_left_right == 'DOWN':
            return True
        if loc2 == 0 and up_down_left_right == 'LEFT':
            return True
        if loc2 == 9 and up_down_left_right == 'RIGHT':
            return True

    # # # If the ship is the cruiser or submarine (3 spaces long) and is in row A, B, I, or J, or in column 1, 2, 9,
    # or 10, AND the direction is not allowed for that position, return True for illegal_move
    if ship_length == 3:
        if loc1 == 0 and up_down_left_right == 'UP' or loc1 == 1 and up_down_left_right == 'UP':
            return True
        if loc1 == 9 and up_down_left_right == 'DOWN' or loc1 == 8 and up_down_left_right == 'DOWN':
            return True
        if loc2 == 0 and up_down_left_right == 'LEFT' or loc2 == 1 and up_down_left_right == 'LEFT':
            return True
        if loc2 == 9 and up_down_left_right == 'RIGHT' or loc2 == 8 and up_down_left_right == 'RIGHT':
            return True

    # # # If the ship is the battleship (4 spaces long) and is in row A, B, C, H, I, or J, or in column 1, 2, 3, 8, 9,
    # or 10, AND the direction is not allowed for that position, return True for illegal_move
    if ship_length == 4:
        if loc1 == 0 and up_down_left_right == 'UP' or loc1 == 1 and up_down_left_right == 'UP' or loc1 == 2 and up_down_left_right == 'UP':
            return True
        if loc1 == 9 and up_down_left_right == 'DOWN' or loc1 == 8 and up_down_left_right == 'DOWN' or loc1 == 7 and up_down_left_right == 'DOWN':
            return True
        if loc2 == 0 and up_down_left_right == 'LEFT' or loc2 == 1 and up_down_left_right == 'LEFT' or loc2 == 2 and up_down_left_right == 'LEFT':
            return True
        if loc2 == 9 and up_down_left_right == 'RIGHT' or loc2 == 8 and up_down_left_right == 'RIGHT' or loc2 == 7 and up_down_left_right == 'RIGHT':
            return True

    # # # If the ship is the carrier (5 spaces long) and is in row A, B, C, D, G, H, I, or J, or in column 1, 2, 3, 4,
    # 7, 8, 9, or 10, AND the direction is not allowed for that position, return True for illegal_move
    if ship_length == 5:
        print(up_down_left_right)
        if loc1 == 0 and up_down_left_right == 'UP' or loc1 == 1 and up_down_left_right == 'UP' or loc1 == 2 and up_down_left_right == 'UP' or loc1 == 3 and up_down_left_right == 'UP':
            print("up")
            return True
        if loc1 == 9 and up_down_left_right == 'DOWN' or loc1 == 8 and up_down_left_right == 'DOWN' or loc1 == 7 and up_down_left_right == 'DOWN' or loc1 == 6 and up_down_left_right == 'DOWN':
            print("down")
            return True
        if loc2 == 0 and up_down_left_right == 'LEFT' or loc2 == 1 and up_down_left_right == 'LEFT' or loc2 == 2 and up_down_left_right == 'LEFT' or loc2 == 3 and up_down_left_right == 'LEFT':
            print("left")
            return True
        if loc2 == 9 and up_down_left_right == 'RIGHT' or loc2 == 8 and up_down_left_right == 'RIGHT' or loc2 == 7 and up_down_left_right == 'RIGHT' or loc2 == 6 and up_down_left_right == 'RIGHT':
            print("right")
            return True


# # # Resets the shared variables. Usually called at the end of each turn.
def reset_vars():
    global b_p, ship_length, up_down_left_right, loc1, loc2, ships, ships_used, ship_choice

    up_down_left_right = ''
    loc1 = 0
    loc2 = 0
    ship_choice = ''


# # # Called when the screen needs cleared. Spams blank lines 35 times to give appropriate space between different events.
def cls():
    for x in range(35):
        print("")


# # # The main game mechanics, asks for ship_choice, up_down_left_right, and calculates loc1/loc2 based off of unfin_pos.
def game_mechanics():
    global b_p, ship_length, up_down_left_right, loc1, loc2, ships, ships_used, ship_choice, letter_to_num, current_player

    # # # str(len(ships_used)) gets the number of ships that have been used, and converts it to a string to be displayed.
    print("\nYou've placed " + str(len(ships_used)) + "/5 ships."
                                                      "\nYour turn will end when you place your last ship, then player 2 will then decide where to place theirs.\n")
    if len(ships_used) == 5: # # # If the number of ships_used is 5 (the maximum amount) switch to player two's turn to place ships.
        print("Switching to player2...")
        current_player = 2
        sleep(5)
        cls()
        game_mechanics2()
    reset_vars()
    print_bp()

    ships_remaining = '' # # # Initialize ships_remaining, which is used to display which ships are still available.
    for x in ships_avail:# in list ships_available add to ships_remaining with a dash in between each entry. (Readability)
        ships_remaining += x + ' - '

    # # # Take input for ship_choice, asking which ship they'd like to place.
    ship_choice = input(
        f"Which ship would you like to place?\n{str(ships_remaining)}\n> ").upper()

    for x in ships_used: # # # If ship_choice is one of the ships that were already used, restart game_mechanics so that they may rechoose.
        if ship_choice == x:
            print("You've already used that ship.")
            sleep(3)
            cls()
            game_mechanics()

    try: # # # Attempt to get the length of the ship, if an exception occurs the user likely did something incorrectly in choosing. Return to game_mechanics
        ship_length = int(ships[ship_choice])
    except (ValueError, TypeError, KeyError, IndexError):
        print("That was not a valid ship, choose again.")
        game_mechanics()

    # # # Take the unpolished starting position for ship placement. ('A1')
    unfin_pos = input("What position would you like to place this ship at?\n>  ").upper()
    pos_holder = [] # # # initialize empty list for transitioning unfin_pos to polished state.

    # # # For every character in unfin_pos, check if the character is a space. if it is a space, ignore it and move on to the next character.
    # If unfin_pos was entered correctly pos_holder will look something like this: ['A', '1']
    for char in unfin_pos:
        if char.isspace():
            None
        else:
            try:
                pos_holder += char
            except (ValueError, TypeError, KeyError, IndexError):
                None
    try: # # # Attempt to make xpos the number value of pos_holder, if an exception occurs, return to game_mechanics.
        xpos = pos_holder[1]
    except (ValueError, TypeError, KeyError, IndexError):
        print("That was not a valid position.\n")
        sleep(1)
        game_mechanics()
    ypos = pos_holder[0] # # # Add the letter value to ypos.

    try:
        ypos = letter_to_num[f"{ypos}"] # # # Attempt to translate ypos to it's number variant.
                                        # If exception, unfin_pos was entered incorrectly, return to game_mechanics.
    except (ValueError, TypeError, KeyError, IndexError):
        print("Your position was not valid.")
        sleep(1)
        game_mechanics()

    # Attempts to add the third char to the second char in the case of there being extra (e.g. A10)
    try:
        if pos_holder[2] == '0':
            third_char = pos_holder[2]
            xpos = xpos + third_char
    except (ValueError, TypeError, KeyError, IndexError): # # # If the second value of unfin_pos was an intentional 10,
        None                                                # check to see if pos_holder has a zero in the third position of the list.
                                                            # If not, ignore the third character as it is likely a mistake.


    loc1 = int(ypos) - 1 # # # Translate the integer value of ypos to the ship board's position (which is one less than the perceived value, since it counts from zero.
    try:
        loc2 = int(xpos) - 1 # # # Do the same for xpos' value, if an exception occurs, return to game_mechanics
    except (ValueError, TypeError, KeyError, IndexError):
        print("Your position was not valid.")
        sleep(1)
        game_mechanics()
    
    # # # Take user input for direction to go from starting position
    up_down_left_right = input("[Up], [Down], [Left], or [Right] from this position?\n> ").upper()

    if up_down_left_right == 'DOWN':
        None
    elif up_down_left_right == 'UP':
        None
    elif up_down_left_right == 'RIGHT':
        None
    elif up_down_left_right == 'LEFT':
        None
    else: # # # If up_down_left_right is not equal to any direction, it was an invalid choice, return to game_mechanics.
        print("You didn't choose a proper direction.") 
        sleep(1)
        game_mechanics()

    # # # Call illegal_move to check if their starting position, ship_choice, and direction all add up to make
    # a legitimate option. If it returns True, print INVALID MOVE and return to game_mechanics.
    if illegal_move(up_down_left_right):
        print(
            '██╗███╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░        ███╗░░░███╗░█████╗░██╗░░░██╗███████╗\n'
            '██║████╗░██║██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗        ████╗░████║██╔══██╗██║░░░██║██╔════╝\n'
            '██║██╔██╗██║╚██╗░██╔╝███████║██║░░░░░██║██║░░██║        ██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░\n'
            '██║██║╚████║░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║        ██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░\n'
            '██║██║░╚███║░░╚██╔╝░░██║░░██║███████╗██║██████╔╝        ██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗\n'
            '╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░        ╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝\n')
        sleep(2)
        cls()
        game_mechanics()

    # # # If their choices make it past all of the checks, their ship_choice gets added to ships_used,
    ships_used.append(ship_choice)
    # and then removed from their ships_avail list.
    if ship_choice == 'DESTROYER':
        ships_avail[0] = ''
    elif ship_choice == 'SUBMARINE':
        ships_avail[1] = ''
    elif ship_choice == 'CRUISER':
        ships_avail[2] = ''
    elif ship_choice == 'BATTLESHIP':
        ships_avail[3] = ''
    elif ship_choice == 'CARRIER':
        ships_avail[4] = ''
    # # # After adding ship_choice to ships_used, and removing it from ships_avail, we move from game_mechanics to place_ship.
    place_ship()


def place_ship():
    global b_p, ship_length, up_down_left_right, loc1, loc2, ships, ships_used

    # # # After all checks in game_mechanics have been passed, place_ship uses up_down_left_right to change the values
    # of the necessary positions on the ship_board to ship pieces, representing your given ship.
    if up_down_left_right == 'DOWN':
        for x in range(ship_length): # # # For as many spaces as your ship occupies, go in the proper direction and change the value to ship piece.
            b_p[loc1 + x][loc2] = '>'

    elif up_down_left_right == 'UP':
        for x in range(ship_length):
            b_p[loc1 - x][loc2] = '>'

    elif up_down_left_right == 'RIGHT':
        for x in range(ship_length):
            b_p[loc1][loc2 + x] = '>'

    elif up_down_left_right == 'LEFT':
        for x in range(ship_length):
            b_p[loc1][loc2 - x] = '>'
    else: # # # If you some how made it past all of the other checks without an error and get here then you've seriously messed up.
        print("ship could not be placed")
    cls()
    game_mechanics() # # # After ship placement, return to game_mechanics for your next ship.


def game_mechanics2(): # # # // Replace with commented version
    global b_p2, ship_length, up_down_left_right, loc1, loc2, ships, ships_used2, ship_choice, letter_to_num

    # # # str(len(ships_used)) gets the number of ships that have been used, and converts it to a string to be displayed.
    print("\nYou've placed " + str(len(ships_used2)) + "/5 ships."
                                                       "\nYour turn will end when you place your last ship, then player 1 will decide where to shoot.\n")
    if len(ships_used2) == 5: # # # If the number of ships_used is 5 (the maximum amount) switch to player two's turn to place ships.
        print("Switching to player1...")
        sleep(5)
        cls()
        p1_turn()
    reset_vars()
    print_bp2()

    ships_remaining = '' # # # Initialize ships_remaining, which is used to display which ships are still available.
    for x in ships_avail2:# in list ships_available add to ships_remaining with a dash in between each entry. (Readability)
        ships_remaining += x + ' - '

    # # # Take input for ship_choice, asking which ship they'd like to place.
    ship_choice = input(
        f"Which ship would you like to place?\n{ships_remaining}\n> ").upper()

    for x in ships_used2: # # # If ship_choice is one of the ships that were already used, restart game_mechanics2 so that they may rechoose.
        if ship_choice == x:
            print("You've already used that ship.")
            sleep(3)
            cls()
            game_mechanics2()

    try: # # # Attempt to get the length of the ship, if an exception occurs the user likely did something incorrectly in choosing. Return to game_mechanics2
        ship_length = int(ships[ship_choice])
    except (ValueError, TypeError, KeyError, IndexError):
        print("That was not a valid ship, choose again.")
        game_mechanics2()

    # # # Take the unpolished starting position for ship placement. ('A1')
    unfin_pos = input("What position would you like to place this ship at?\n>  ").upper()
    pos_holder = [] # # # initialize empty list for transitioning unfin_pos to polished state.

    # # # For every character in unfin_pos, check if the character is a space. if it is a space, ignore it and move on to the next character.
    # If unfin_pos was entered correctly pos_holder will look something like this: ['A', '1']
    for char in unfin_pos:
        if char.isspace():
            None
        else:
            try:
                pos_holder += char
            except (ValueError, TypeError, KeyError, IndexError):
                None
    try: # # # Attempt to make xpos the number value of pos_holder, if an exception occurs, return to game_mechanics2.
        xpos = pos_holder[1]
    except (ValueError, TypeError, KeyError, IndexError):
        print("That was not a valid position.\n")
        sleep(1)
        game_mechanics2()
    ypos = pos_holder[0] # # # Add the letter value to ypos.

    try:
        ypos = letter_to_num[f"{ypos}"] # # # Attempt to translate ypos to it's number variant.
                                        # If exception, unfin_pos was entered incorrectly, return to game_mechanics2.
    except (ValueError, TypeError, KeyError, IndexError):
        print("Your position was not valid.")
        sleep(1)
        game_mechanics2()

    # Attempts to add the third char to the second char in the case of there being extra (e.g. A10)
    try:
        if pos_holder[2] == '0':
            third_char = pos_holder[2]
            xpos = xpos + third_char
    except (ValueError, TypeError, KeyError, IndexError): # # # If the second value of unfin_pos was an intentional 10,
        None                                                # check to see if pos_holder has a zero in the third position of the list.
                                                            # If not, ignore the third character as it is likely a mistake.

    loc1 = int(ypos) - 1 # # # Translate the integer value of ypos to the ship board's position (which is one less than the perceived value, since it counts from zero.
    try:
        loc2 = int(xpos) - 1 # # # Do the same for xpos' value, if an exception occurs, return to game_mechanics2
    except (ValueError, TypeError, KeyError, IndexError):
        print("Your position was not valid.")
        sleep(1)
        game_mechanics2()

    # # # Take user input for direction to go from starting position
    up_down_left_right = input("[Up], [Down], [Left], or [Right] from this position?\n> ").upper()

    if up_down_left_right == 'DOWN':
        None
    elif up_down_left_right == 'UP':
        None
    elif up_down_left_right == 'RIGHT':
        None
    elif up_down_left_right == 'LEFT':
        None
    else: # # # If up_down_left_right is not equal to any direction, it was an invalid choice, return to game_mechanics2.
        print("You didn't choose a proper direction.")
        sleep(1)
        game_mechanics2()

    # # # Call illegal_move to check if their starting position, ship_choice, and direction all add up to make
    # a legitimate option. If it returns True, print INVALID MOVE and return to game_mechanics2.
    if illegal_move(up_down_left_right):
        print(
            '██╗███╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░        ███╗░░░███╗░█████╗░██╗░░░██╗███████╗\n'
            '██║████╗░██║██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗        ████╗░████║██╔══██╗██║░░░██║██╔════╝\n'
            '██║██╔██╗██║╚██╗░██╔╝███████║██║░░░░░██║██║░░██║        ██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░\n'
            '██║██║╚████║░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║        ██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░\n'
            '██║██║░╚███║░░╚██╔╝░░██║░░██║███████╗██║██████╔╝        ██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗\n'
            '╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░        ╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝\n')
        sleep(2)
        cls()
        game_mechanics2()

    # # # If their choices make it past all of the checks, their ship_choice gets added to ships_used,
    ships_used2.append(ship_choice)
    # and then removed from their ships_avail list.
    if ship_choice == 'DESTROYER':
        ships_avail2[0] = ''
    elif ship_choice == 'SUBMARINE':
        ships_avail2[1] = ''
    elif ship_choice == 'CRUISER':
        ships_avail2[2] = ''
    elif ship_choice == 'BATTLESHIP':
        ships_avail2[3] = ''
    elif ship_choice == 'CARRIER':
        ships_avail2[4] = ''
    # # # After adding ship_choice to ships_used, and removing it from ships_avail, we move from game_mechanics2 to place_ship.
    place_ship2()


def place_ship2():
    global b_p2, ship_length, up_down_left_right, loc1, loc2, ships, ships_used2

    # # # After all checks in game_mechanics have been passed, place_ship uses up_down_left_right to change the values
    # of the necessary positions on the ship_board to ship pieces, representing your given ship.
    if up_down_left_right == 'DOWN':
        for x in range(ship_length): # # # For as many spaces as your ship occupies, go in the proper direction and change the value to ship piece.
            b_p2[loc1 + x][loc2] = '<'

    elif up_down_left_right == 'UP':
        for x in range(ship_length):
            b_p2[loc1 - x][loc2] = '<'

    elif up_down_left_right == 'RIGHT':
        for x in range(ship_length):
            b_p2[loc1][loc2 + x] = '<'

    elif up_down_left_right == 'LEFT':
        for x in range(ship_length):
            b_p2[loc1][loc2 - x] = '<'
    else: # # # If you some how made it past all of the other checks without an error and get here then you've seriously messed up.
        print("ship could not be placed")
    cls()
    game_mechanics2() # # # After ship placement, return to game_mechanics2 for your next ship.


def p1_turn():
    global p2_health, m_p, m_p2, b_p, b_p2

    print_bp_mp() # # # calls the function to print the ship board AND the H/M board.
    # # # Everything between these lines serves virtually the same function as is commented in game_mechanics to gather and translate positions.
    # ---------------------------------------------------------------------------------------------------------------- #
    unfin_pos = input("What position would you like to fire upon?\n>  ").upper()
    pos_holder = []

    for char in unfin_pos:
        if char.isspace():
            None
        else:
            try:
                pos_holder += char
            except (ValueError, TypeError, KeyError, IndexError):
                None
    try:
        xpos = pos_holder[1]
    except (ValueError, TypeError, KeyError, IndexError):
        print("That was not a valid position.\n")
        sleep(1)
        p1_turn()
    ypos = pos_holder[0]

    try:
        ypos = letter_to_num[f"{ypos}"]
    except (ValueError, TypeError, KeyError, IndexError):
        print("Your position was not valid.")
        sleep(1)
        p1_turn()
    # Attempts to add the third char to the second char in the case of there being extra (e.g. A10)
    try:
        if pos_holder[2] == '0':
            third_char = pos_holder[2]
            xpos = xpos + third_char
    except (ValueError, TypeError, KeyError, IndexError):
        None

    floc1 = int(ypos) - 1
    try:
        floc2 = int(xpos) - 1
    except (ValueError, TypeError, KeyError, IndexError):
        print("Your position was not valid.")
        sleep(1)
        p1_turn()
    # ---------------------------------------------------------------------------------------------------------------- #

    if b_p2[floc1][floc2] == '<': # # # If the position chosen is a ship piece on the enemies' board, it's a HIT.
        m_p[floc1][floc2] = 'H' # # # Add hit marker to player one's H/M Board at position
        b_p2[floc1][floc2] = 'H' # # # Change marker on enemies' board to hit marker at position

        p2_health -= 1 # # # Decrease opponent's health by one.
        health_percentage = (p2_health / 17) * 100 # # # Convert opponent's current health to a percentage.
        ceil(health_percentage) # # # Round percentage up for estimate.

        if p2_health == 0: # # # Check if that hit was a game winning hit
            print("Player 1 wins! All of Player 2's ships have been sunk.")
            sleep(3)
            return 0

        cls()

        print(unfin_pos + " was a HIT!")
        print("Player 2 took " + str(100 - int(health_percentage)) + "% damage to their ships.") # # # Reverse health percentage for damage percentage.
        print("Switching to player 2...")
        sleep(5)

        cls()
        p2_turn()

    elif b_p2[floc1][floc2] == 'H': # # # If given position was already shot at, return to beginning of turn.
        print("You've already shot at this position.")
        reset_vars() # # # May be unnecessary, did it as a precaution.
        sleep(1)
        cls()
        p1_turn()

    else: # # # If it's neither of the above, it's a miss.
        m_p[floc1][floc2] = 'M' # # # Change position at H/M board to miss marker.
        b_p2[floc1][floc2] = 'M' # # # Change position on enemies' ship board to miss marker

        cls()

        health_percentage = (p2_health / 17) * 100 # # # Take percentage of current health of the opponent.
        ceil(health_percentage) # # # Round health percentage up for estimate

        print(unfin_pos + " was a MISS!")
        print("Player 2 has taken " + str(100 - int(health_percentage)) + "% damage to their ships so far.") # # # Convert to damage taken
        print("Switching to player 2...")
        sleep(5)

        cls()
        p2_turn()


def p2_turn(): # # # // Add from p1_turn
    global p1_health, m_p, m_p2, b_p, b_p2

    print_bp_mp2() # # # calls the function to print the ship board AND the H/M board.
    # # # Everything between these lines serves virtually the same function as is commented in game_mechanics to gather and translate positions.
    # ---------------------------------------------------------------------------------------------------------------- #
    unfin_pos = input("What position would you like to fire upon?\n>  ").upper()
    pos_holder = []

    for char in unfin_pos:
        if char.isspace():
            None
        else:
            try:
                pos_holder += char
            except (ValueError, TypeError, KeyError, IndexError):
                None
    try:
        xpos = pos_holder[1]
    except (ValueError, TypeError, KeyError, IndexError):
        print("That was not a valid position.")
        sleep(1)
        p2_turn()
    ypos = pos_holder[0]

    try:
        ypos = letter_to_num[f"{ypos}"]
    except (ValueError, TypeError, KeyError, IndexError):
        print("Your position was not valid.")
        sleep(1)
        p2_turn()

    # Attempts to add the third char to the second char in the case of there being extra (e.g. A10)
    try:
        if pos_holder[2] == '0':
            third_char = pos_holder[2]
            xpos = xpos + third_char
    except (ValueError, TypeError, KeyError, IndexError):
        None

    floc1 = int(ypos) - 1
    try:
        floc2 = int(xpos) - 1
    except (ValueError, TypeError, KeyError, IndexError):
        print("Your position was not valid.")
        sleep(1)
        p2_turn()
    # ---------------------------------------------------------------------------------------------------------------- #

    if b_p[floc1][floc2] == '>': # # # If the position chosen is a ship piece on the enemies' board, it's a HIT.
        m_p2[floc1][floc2] = 'H' # # # Add hit marker to player one's H/M Board at position
        b_p[floc1][floc2] = 'H' # # # Change marker on enemies' board to hit marker at position

        p1_health -= 1 # # # Decrease opponent's health by one.
        health_percentage = (p1_health / 17) * 100 # # # Convert opponent's current health to a percentage.
        ceil(health_percentage) # # # Round percentage up for estimate.

        if p1_health == 0: # # # Check if that hit was a game winning hit
            print("Player 2 wins! All of Player 1's ships have been sunk.")
            sleep(3)
            return 0

        cls()

        print(unfin_pos + " was a HIT!")
        print("Player 1 took " + str(100 - int(health_percentage)) + "% damage to their ships.") # # # Reverse health percentage for damage percentage.
        print("Switching to player 1...")
        sleep(5)

        cls()
        p1_turn()

    elif b_p[floc1][floc2] == 'H': # # # If given position was already shot at, return to beginning of turn.
        print("You've already shot at this position.")
        reset_vars() # # # May be unnecessary, did it as a precaution.
        sleep(1)
        cls()
        p2_turn()

    else: # # # If it's neither of the above, it's a miss.
        m_p2[floc1][floc2] = 'M' # # # Change position at H/M board to miss marker.
        b_p[floc1][floc2] = 'M' # # # Change position on enemies' ship board to miss marker

        cls()

        health_percentage = (p1_health / 17) * 100 # # # Take percentage of current health of the opponent.
        ceil(health_percentage) # # # Round health percentage up for estimate

        print(unfin_pos + " was a MISS!")
        print("Player 1 has taken " + str(100 - int(health_percentage)) + "% damage to their ships so far.") # # # Convert to damage taken
        print("Switching to player 1...")
        sleep(5)

        cls()
        p1_turn()


game_mechanics() # # # First line called when program is run, starts the game.