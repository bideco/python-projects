from collections import deque
from random import randint
import PySimpleGUI as py

# Inspired by Edabit Minesweeper I challenge. https://edabit.com/challenge/YDgtdP69Mn9pC73xN

py.theme("darkamber")
play = True

while play:
    layout = [
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="0,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="1,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="2,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="3,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="4,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="5,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="6,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="7,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="8,9")],
              [py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,0"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,1"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,2"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,3"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,4"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,5"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,6"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,7"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,8"), py.Button("", button_color=("white", "white"),  size=(2, 1), key="9,9")],
              ]

    # Below lists detail all eight possible movements
    row = [-1, -1, -1, 0, 0, 1]
    col = [-1, 0, 1, -1, 1, 0]
    replacement = '_'
    used_coords = []
    LOST = False

    board = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]

    board_comp = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]

    bomb_list = []
    amount_of_bombs = randint(10, 12)
    for x in range(amount_of_bombs):
        new_bomb_location_x = randint(0, 9)
        new_bomb_location_y = randint(0, 9)
        while board[new_bomb_location_x][new_bomb_location_y] == "O":
            new_bomb_location_x = randint(0, 9)
            new_bomb_location_y = randint(0, 9)

        board[new_bomb_location_x][new_bomb_location_y] = "O"
        coordinate = str(new_bomb_location_x) + "," + str(new_bomb_location_y)
        bomb_list.append(coordinate)

    for x in bomb_list:
        x.split(",")
        coordinate_x = x[0]
        coordinate_y = x[2]
        for row_1 in range(len(board)):
            for item in range(len(board[row_1])):
                if board[row_1][item] == '-':
                    board[row_1][item] = str(sum(1 for u in range(row_1 - 1, row_1 + 2) for v in range(item - 1, item + 2) if 0 <= v < len(board[row_1]) and 0 <= u < len(board) and board[u][v] == 'O'))
                    if sum(1 for u in range(row_1 - 1, row_1 + 2) for v in range(item - 1, item + 2) if 0 <= v < len(board[row_1]) and 0 <= u < len(board) and board[u][v] == 'O') == 0:
                        board[row_1][item] = "-"


    def isSafe(board, x, y, target):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == target


    def floodfill(board, x, y, replacement):
        global row, col, layout
        # create a queue and enqueue starting pixel
        q = deque()
        q.append((x, y))

        # get the target color
        target = board[x][y]

        # break when the queue becomes empty
        while q:

            # dequeue front node and process it
            x, y = q.popleft()

            # replace the current pixel color with that of replacement
            board[x][y] = replacement
            used_coords.append(f"{x},{y}")
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(button_color=("black", "green"), disabled=True)
            # process all eight adjacent pixels of the current pixel and
            # enqueue each valid pixel
            for k in range(len(row)):
                # if the adjacent pixel at position `(x + row[k], y + col[k])` is
                # is valid and has the same color as the current pixel
                if isSafe(board, x + row[k], y + col[k], target):
                    # enqueue adjacent pixel
                    q.append((x + row[k], y + col[k]))


    def reveal(x, y):
        if board[x][y] == "1":
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(text="1", button_color=("white", "#D4AC0D"), disabled=True)
            return True
        if board[x][y] == "2":
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(text="2", button_color=("white", "#D68910"), disabled=True)
            return True
        if board[x][y] == "3":
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(text="3", button_color=("white", "#B9770E"), disabled=True)
            return True
        if board[x][y] == "4":
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(text="4", button_color=("white", "#9C640C"), disabled=True)
            return True
        if board[x][y] == "5":
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(text="5", button_color=("white", "#A04000"), disabled=True)
            return True
        if board[x][y] == "6":
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(text="6", button_color=("white", "#873600"), disabled=True)
            return True
        if board[x][y] == "7":
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(text="7", button_color=("white", "#6E2C00"), disabled=True)
            return True
        if board[x][y] == "O":
            change_button = window.find_element(f"{x},{y}")
            change_button.Update(text="O", button_color=("white", "#A93226"), disabled=True)
            return True
        else:
            return False


    def finished():
        not_finished = 0

        for f in range(10):
            for h in range(10):
                if f"{f},{h}" not in used_coords and board[f][h] != "O":
                    not_finished = not_finished+1

        if not_finished > 0:
            return False
        else:
            return True


    def mechs(x,y):
        global LOST

        if board[x][y] == "O":
            LOST = True

        if reveal(x, y):
            used_coords.append(f"{x},{y}")
        else:
            floodfill(board, x, y, replacement)

        for i in range(10):
            for j in range(10):
                if board[i][j] == "_" or board[i][j] == "1" or board[i][j] == "2" or board[i][j] == "3" or board[i][j] == "4" or board[i][j] == "5" or board[i][j] == "6" or board[i][j] == "7":
                    board_comp[i][j] = "#"

        if LOST and not finished():
            for e in range(10):
                for g in range(10):
                    str = f"{e},{g}"
                    if str not in used_coords and board[e][g] == "O":
                        mechs(e, g)
                    change_button = window.find_element(f"{e},{g}")
                    change_button.Update(disabled=True)


    if __name__ == '__main__':
        window = py.Window("Minesweeper", layout, size=(360, 340), use_default_focus=False)
        while True:
            event, values = window.read()
            if event == py.WIN_CLOSED or event == 'Cancel':
                play = False
                break
            if event:
                try:
                    coordinates = event.split(",")
                    x = int(coordinates[0])
                    y = int(coordinates[1])
                    mechs(x, y)
                    if LOST:
                        lost_win = py.popup_yes_no("YOU LOST\nReplay?", grab_anywhere=True, no_titlebar=True, location=(600, 600))
                        if lost_win == "Yes":
                            break
                        else:
                            window.close()
                            play = False
                            break
                    if finished() and not LOST:
                        win_win = py.popup_yes_no("YOU WON!\nReplay?", grab_anywhere=True, no_titlebar=True, location=(600, 600))
                        if win_win == "Yes":
                            break
                        else:
                            window.close()
                            play = False
                            break
                    window.refresh()
                except:
                    None
