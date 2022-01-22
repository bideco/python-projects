# Python Projects

Here are some of the python projects I've worked on over the past year. Some are just concepts, like the 'driving.py' idea, while others are complete to the extent that I had originally intended. Please feel free to take a look, I have a few of them in [working widgets](https://nicholas.barr.contact) if you don't feel like copying and running on your own device.

## [Battleship](https://github.com/bideco/python-projects/blob/master/battleship.py)

Battleship was one of the first ideas I had when I started working with Python. I wanted to see if it was possible to do something as complex as a two player game like this in a text-based console format. This program runs with the built-ins Math and Time as the only two imports, and while the code is definitely messy, it does work as intended.

## [Color-maker](https://github.com/bideco/python-projects/blob/master/color-maker.py)

Color-maker is my first attempt at making a GUI based program using [PySimpleGUI][PyGUI]. Its purpose is to collect a list of HEX codes and display them so that the colors are easily visible. It can also generate random HEX codes based off of an amount value if provided. It has three separate menus and allows the user to choose a single value or all values to copy to their clipboard using [Pyperclip](https://pypi.org/project/pyperclip/). I found it to be a great learning experience for building applications with GUI modules and a fun project all around.

## [Drawing](https://github.com/bideco/python-projects/blob/master/drawing.py)

This one was a great learning experience into how different forms of user input can be used to perform actions within applications. I wrote a program that contains a GUI, and a canvas. The GUI was made with [PySimpleGUI][PyGUI] once again, and the canvas was made with [Turtle](https://docs.python.org/3/library/turtle.html). I take mouse input as well as keyboard input to allow the user to draw in different colors, sizes, do color fills, and a lot of other simple actions. It is essentially a dumbed-down Microsoft Paint. I had a lot of fun writing this one.

## [Driving](https://github.com/bideco/python-projects/blob/master/driving.py)

This one was written before the drawing.py application and my intent was to see if the [Turtle](https://docs.python.org/3/library/turtle.html) module could do simple animations. While the frame-rate is obviously not great, it does *sort of* work.

## [Hangman](https://github.com/bideco/python-projects/blob/master/hangman.py)

I was very invested in converting common pen & paper games and board games into console programs. Hangman was a great learning tool for how to properly format, track, and use data within the application to make things happen. This hangman game can be played with one or two players, the single player version contains 215 difficult words to guess, in the two player game you are able to write your own word in and can have the other player guess it.

## [Minesweeper](https://github.com/bideco/python-projects/blob/master/minesweeper.py)

After getting comfortable with the basics of Python I felt like I wanted to try something more complex; I saw a challenge on [Edabit](https://edabit.com/challenge/vb9BDiGC9noYLdyCF) with a much more simplified version of minesweeper in the Expert section, I liked the idea of making a working minesweeper game so I worked away for a bit to make it happen. I found that the hardest part was to make the surrounding bombless but connected spaces to reveal themselves when the user clicked on a tile. For that, I figured out how to implement a [Flood-fill algorithm](https://en.wikipedia.org/wiki/Flood_fill), which turned out to be a very satisfying accomplishment. This program uses [PySimpleGUI][PyGUI] for the graphical interface and the buttons translate to a 2D list, which have the values for empty spaces, clicked spaces, and bomb spaces.

## [Tic Tac Toe](https://github.com/bideco/python-projects/blob/master/tic_tac_toe.py)

Tic Tac Toe is a game that I created in C++ before trying out Python. In the C++ version I used ASCII characters and arrays to keep track of moves. Translating it to Python would have been incredibly easy. However, I decided to make it a little more interesting by giving it a GUI. I used [Turtle](https://docs.python.org/3/library/turtle.html) for drawing the board, pieces, and tracking the location of mouse clicks to place said pieces. I also used a tiny bit of [Tkinter ](https://docs.python.org/3/library/tkinter.html)to make pop-up windows for the winning message.



[PyGUI]: https://pysimplegui.readthedocs.io/en/latest/
