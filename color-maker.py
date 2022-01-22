from _tkinter import TclError
from math import floor

import PySimpleGUI as sg
import pyperclip
import random

sg.theme("DarkGreen5")
open_window = 0
window_closed = False


def hex_viewer():
    lower_than_10 = 0

    hex_window = sg.Window('Hex Collector').Layout(
        [[sg.Column([[sg.Text(text="Enter your hex codes!", justification="center")]], justification='c')],
         [sg.Column([[sg.InputText("#ffffff, #000000, #dddddd")]])],
         [sg.Column([[sg.Button("Load", bind_return_key=True), sg.Cancel("Close")]], justification='c')]])

    while True:
        event, values = hex_window.read()
        if event == "Load":
            input_value = list(values[0].split(","))
            for x in range(len(input_value)):
                input_value[x] = input_value[x].replace(' ', '')
            copy_value = list(values[0].split(", "))
            copy_value2 = values[0]
            break
        if event in ("Close", None):
            input_value = "close_window"
            break
    hex_window.close()

    # Second window code
    try:
        if input_value != "close_window":
            layout = []
            pre_layout = []
            input_value_length = len(input_value)
            remainder = input_value_length % 10
            ten_goes_in = input_value_length / 10
            how_many_tens = floor(ten_goes_in)

            if len(input_value) > 10:
                for x1 in range(how_many_tens):
                    pre_layout = []
                    for x in range(10):
                        pre_layout += [sg.Button(button_color=("black", f"{input_value[0]}"), tooltip=f"User generated: {input_value[0]}", size=(5, 3), key=f"{input_value[0]}")]
                        del (input_value[0])
                    layout += [pre_layout]
                pre_layout = []
                for i in range(remainder):
                    pre_layout += [sg.Button(button_color=("black", f"{input_value[0]}"), tooltip=f"User generated: {input_value[0]}", size=(5, 3), key=f"{input_value[0]}")]
                    del (input_value[0])
                layout += [pre_layout]
            else:
                for x in range(input_value_length):
                    pre_layout += [sg.Button(button_color=("black", f"{input_value[x]}"), tooltip=f"User generated: {input_value[x]}", size=(5, 3), key=f"{input_value[x]}")]
                layout += [pre_layout]
                lower_than_10 = 1

            if lower_than_10 == 0:
                hex_viewer_window = sg.Window('Random Color Picker', size=(630, 635)).Layout([[sg.Column([[sg.Button("Copy All"), sg.Button("Close", bind_return_key=True)]], justification='c')], [sg.Column(layout, size=(600, 635), scrollable=True, vertical_scroll_only=True)]])
            else:
                hex_viewer_window = sg.Window('Random Color Picker').Layout([[sg.Column(layout, scrollable=True, vertical_scroll_only=True),
                                                                              sg.Button("Copy All"), sg.Button("Close", bind_return_key=True)]])
            while True:
                event, values = hex_viewer_window.read()

                if event == "Copy All":
                    pyperclip.copy(copy_value2)
                    sg.popup_quick_message("All values copied!", auto_close=True, auto_close_duration=1, text_color="red", background_color="black")

                for x in range(len(copy_value)):

                    if event == copy_value[x]:
                        pyperclip.copy(copy_value[x])
                        sg.popup_quick_message("Copied!", auto_close=True, auto_close_duration=1, text_color="red", background_color="black")

                if event in ("Close", None):
                    break
            hex_viewer_window.close()
            main_window()

    except TclError:
        layout_col = [
            [sg.Text("Whoops!\nLooks like your input was improperly formatted.\n\nReformat it and try again.",
                     justification='center')],
            [sg.Button("Close")]
        ]
        layout = [[sg.Column(layout_col, element_justification='center')]]

        error = sg.Window("Input Error!", layout, element_justification='c')
        while True:
            event, values = error.read()
            if event in ("Close", sg.WIN_CLOSED):
                break
        error.close()
        main_window()


def hex_generator():
    global window_closed
    hex_generator_start_window = sg.Window('Amount Collector').Layout(
        [[sg.Column([[sg.Text("How many random colors would you like to generate?", justification='center')]],
                    justification='c')],
         [sg.Column([[sg.InputText()]])],
         [sg.Column([[sg.Button("Enter", bind_return_key=True), sg.Cancel("Close")]], justification='c')]])

    while True:
        event, values = hex_generator_start_window.read()
        if event == "Enter":
            try:
                user_hex_num = int(values[0])
            except ValueError:
                hex_generator_start_window.close()
                sg.popup_error("Whoops, that was not a valid integer.")
                window_closed = True
                user_hex_num = 0
                break
            window_closed = False
            break
        if event in ("Close", None):
            window_closed = True
            user_hex_num = 0
            break

    if window_closed or user_hex_num > 1500:
        hex_generator_start_window.close()
        main_window()
    else:
        hex_generator_start_window.close()

        layout = []
        hex_list = ''
        random.seed()

        remainder = user_hex_num % 5
        five_goes_in = user_hex_num / 5
        how_many_fives = floor(five_goes_in)

        if user_hex_num > 5:
            for x1 in range(how_many_fives):
                pre_layout = []
                for i in range(5):
                    hex_code = '#'
                    while len(hex_code) <= 6:
                        letter_number = random.randint(0, 1)
                        letters = 'abcdef'

                        if letter_number == 0:
                            # get random letter
                            random_letter = random.choice(letters)
                            hex_code += random_letter
                        else:
                            # get random number
                            random_strint = str(random.randint(0, 9))
                            hex_code += random_strint

                    pre_layout += [sg.Button(button_color=("black", f"{hex_code}"),
                                             tooltip=f"Randomly generated: {hex_code}", size=(5, 3), key=f"{hex_code}")]
                    hex_list += hex_code + ", "
                layout += [pre_layout]
            pre_layout = []

            for i in range(remainder):
                hex_code = '#'
                while len(hex_code) <= 6:
                    letter_number = random.randint(0, 1)
                    letters = 'abcdef'

                    if letter_number == 0:
                        # get random letter
                        random_letter = random.choice(letters)
                        hex_code += random_letter
                    else:
                        # get random number
                        random_strint = str(random.randint(0, 9))
                        hex_code += random_strint
                pre_layout += [sg.Button(button_color=("black", f"{hex_code}"),
                                         tooltip=f"Randomly generated: {hex_code}", size=(5, 3), key=f"{hex_code}")]
            layout += [pre_layout]
        else:
            pre_layout = []
            for i2 in range(user_hex_num):
                hex_code = '#'
                while len(hex_code) <= 6:
                    letter_number = random.randint(0, 1)
                    letters = 'abcdef'

                    if letter_number == 0:
                        # get random letter
                        random_letter = random.choice(letters)
                        hex_code += random_letter
                    else:
                        # get random number
                        random_strint = str(random.randint(0, 9))
                        hex_code += random_strint

                pre_layout += [sg.Button(button_color=("black", f"{hex_code}"),
                                         tooltip=f"Randomly generated: {hex_code}", size=(5, 3), key=f"{hex_code}")]
            layout += [pre_layout]
        if user_hex_num > 14:
            hex_generator_window = sg.Window('Random Color Picker', size=(335, 320)).Layout(
                [[sg.Column([[sg.Text(text=f"Here's {user_hex_num} color(s)!\nClick to copy, hover to view hex.",
                                      justification="c")]], justification='c')],
                 [sg.Column([[sg.Button("Copy All", bind_return_key=True), sg.Button(button_text="Close")]],
                            justification='c')],
                 [sg.Column(layout, size=(290, 320), justification='c', scrollable=True, vertical_scroll_only=True)]])
        else:
            hex_generator_window = sg.Window('Random Color Picker', size=(335, 200)).Layout(
                [[sg.Column([[sg.Text(text=f"Here's {user_hex_num} color(s)!\nClick to copy, hover to view hex.",
                                      justification="c")]], justification='c')],
                 [sg.Column([[sg.Button("Copy All", bind_return_key=True), sg.Button(button_text="Close")]],
                            justification='c')],
                 [sg.Column(layout, size=(290, 200), justification='c', scrollable=True, vertical_scroll_only=True)]])
        hex_array = hex_list.split(", ")

        while True:
            event, values = hex_generator_window.read()

            for x in range(len(hex_array)):

                if event == hex_array[x]:
                    pyperclip.copy(hex_array[x])
                    sg.popup_quick_message("Copied!", auto_close=True, auto_close_duration=1, text_color="red",
                                           background_color="black")
            if event == "Copy All":
                refined_hex_list = hex_list[:-2] + hex_list[-2 + 1:]
                pyperclip.copy(refined_hex_list)
                sg.popup_quick_message("Copied!", auto_close=True, auto_close_duration=1, text_color="red",
                                       background_color="black")
                break
            if event in ("Close", None):
                break
        hex_generator_window.close()
        main_window()


def main_window():
    m_window = sg.Window('Color-maker').Layout(
        [[sg.Column([[sg.Text(text="Welcome to the Color-maker!",
                              justification="c")]], justification='c')],
         [sg.Column([[sg.Button("Hex Viewer", bind_return_key=True), sg.Button("Hex Generator"), sg.Cancel("Close")]],
                    justification='c')]])

    while True:
        global open_window
        open_window = 0
        event, values = m_window.read()

        if event == "Hex Viewer":
            open_window = 1
            break
        if event == "Hex Generator":
            open_window = 2
            break
        if event in ("Close", None):
            open_window = 3
            break

    if open_window == 1:
        m_window.close()
        hex_viewer()
    if open_window == 2:
        m_window.close()
        hex_generator()


while open_window != 3:
    main_window()
