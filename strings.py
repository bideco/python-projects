import time

sentence = ''
sentence_reversed = ''
sentence_backwards = ''

def choose_string():
    global sentence
    sentence_or = input("sentence: ")
    if sentence_or[-1] == " ":
        for x in range(len(sentence_or) - 1):
            sentence = sentence + sentence_or[x]
    else:
        sentence = sentence_or


def menu():
    global sentence

    menu_option = input('''Would you like to...
        0. Choose a new string to use.
        1. Find the length of this string?
        2. Display this string backwards?
        3. Count the number of words in this string?
        4. Concatenate one string contents to another?
        5. Compare two strings and determine equality?
        6. Find a substring and display its starting postition within the string?
        7. Reverse the string?
        8. Convert the string to lowercase?
        9. Convert the string to uppercase?
        ''')

    if menu_option == "0":
        choose_string()
        menu()
    elif menu_option == "1":
        print(f"This string is {len(sentence)} characters long.")
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    elif menu_option == "2":
        backwards()
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    elif menu_option == "3":
        words = 1
        sentence_words = sentence
        for x in sentence_words:
            if x == " ":
                words = words + 1
        print(f"This string has {words} words.")
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    elif menu_option == "4":
        sentence_orig = sentence
        second_sentence = input("Enter another string: ")
        concatenated = sentence_orig + " " + second_sentence
        print(f"{sentence_orig} concatenated with {second_sentence} is {concatenated}")
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    elif menu_option == "5":
        second_sentence = input("Enter another string: ")
        if sentence == second_sentence:
            print("These strings are equal.")
        else:
            print("These strings are different.")
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    elif menu_option == "6":
        second_sentence = input("Enter another string: ")
        location = sentence.find(second_sentence)
        if location == -1:
            print("I couldn't find that string within the first.")
        else:
            print(f"I found your string starting at character #{location}")
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    elif menu_option == "7":
        reverse()
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    elif menu_option == "8":
        print(f"Your string, '{sentence}' in lowercase is '{sentence.lower()}'")
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    elif menu_option == "9":
        print(f"Your string, '{sentence}' in uppercase is '{sentence.upper()}'")
        print("Taking you back to the menu...")
        time.sleep(3)
        print("\n\n\n\n\n\n\n")
        menu()
    else:
        print("That wasn't an acceptable option.")
        time.sleep(3)
        menu()


def reverse():
    global sentence, sentence_reversed
    for x in reversed(range(len(sentence))):
        sentence_reversed = sentence_reversed + sentence[x]
    print(sentence_reversed)


def backwards():
    global sentence, sentence_backwards
    sentence_list = sentence.split(" ")
    for x in reversed(range(len(sentence_list))):
        sentence_backwards = sentence_backwards + str(sentence_list[x]) + " "
    print(sentence_backwards)


choose_string()
menu()
