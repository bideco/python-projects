import random
import time

wordlist = [
    "abruptly",
    "absurd",
    "abyss",
    "affix",
    "askew",
    "avenue",
    "awkward",
    "axiom",
    "azure",
    "bagpipes",
    "bandwagon",
    "banjo",
    "bayou",
    "beekeeper",
    "bikini",
    "blitz",
    "blizzard",
    "boggle",
    "bookworm",
    "boxcar",
    "boxful",
    "buckaroo",
    "buffalo",
    "buffoon",
    "buxom",
    "buzzard",
    "buzzing",
    "buzzwords",
    "caliph",
    "cobweb",
    "cockiness",
    "croquet",
    "crypt",
    "curacao",
    "cycle",
    "daiquiri",
    "dirndl",
    "disavow",
    "dizzying",
    "duplex",
    "dwarves",
    "embezzle",
    "equip",
    "espionage",
    "euouae",
    "exodus",
    "faking",
    "fishhook",
    "fixable",
    "fjord",
    "flapjack",
    "flopping",
    "fluffiness",
    "flyby",
    "foxglove",
    "frazzled",
    "frizzled",
    "fuchsia",
    "funny",
    "gabby",
    "galaxy",
    "galvanize",
    "gazebo",
    "giaour",
    "gizmo",
    "glowworm",
    "glyph",
    "gnarly",
    "gnostic",
    "gossip",
    "grogginess",
    "haiku",
    "haphazard",
    "hyphen",
    "iatrogenic",
    "icebox",
    "injury",
    "ivory",
    "ivy",
    "jackpot",
    "jaundice",
    "jawbreaker",
    "jaywalk",
    "jazz",
    "jazziest",
    "jazzy",
    "jelly",
    "jigsaw",
    "jinx",
    "jiujitsu",
    "jockey",
    "jogging",
    "joking",
    "jovial",
    "joyful",
    "juicy",
    "jukebox",
    "jumbo",
    "kayak",
    "kazoo",
    "keyhole",
    "khaki",
    "kilobyte",
    "kiosk",
    "kitsch",
    "kiwifruit",
    "klutz",
    "knapsack",
    "larynx",
    "lengths",
    "lucky",
    "luxury",
    "lymph",
    "marquis",
    "matrix",
    "megahertz",
    "microwave",
    "mnemonic",
    "mystify",
    "naphtha",
    "nightclub",
    "nowadays",
    "numbskull",
    "nymph",
    "onyx",
    "ovary",
    "oxidize",
    "oxygen",
    "pajama",
    "peekaboo",
    "phlegm",
    "pixel",
    "pizazz",
    "pneumonia",
    "polka",
    "pshaw",
    "psyche",
    "puppy",
    "puzzling",
    "quartz",
    "queue",
    "quips",
    "quixotic",
    "quiz",
    "quizzes",
    "quorum",
    "razzmatazz",
    "rhubarb",
    "rhythm",
    "rickshaw",
    "schnapps",
    "scratch",
    "shiv",
    "snazzy",
    "sphinx",
    "spritz",
    "squawk",
    "staff",
    "strength",
    "strengths",
    "stretch",
    "stronghold",
    "stymied",
    "subway",
    "swivel",
    "syndrome",
    "thriftless",
    "thumbscrew",
    "topaz",
    "transcript",
    "transgress",
    "transplant",
    "triphthong",
    "twelfth",
    "twelfths",
    "unknown",
    "unworthy",
    "unzip",
    "uptown",
    "vaporize",
    "vixen",
    "vodka",
    "voodoo",
    "vortex",
    "voyeurism",
    "walkway",
    "waltz",
    "wave",
    "wavy",
    "waxy",
    "wellspring",
    "wheezy",
    "whiskey",
    "whizzing",
    "whomever",
    "wimpy",
    "witchcraft",
    "wizard",
    "woozy",
    "wristwatch",
    "wyvern",
    "xylophone",
    "yachtsman",
    "yippee",
    "yoked",
    "youthful",
    "yummy",
    "zephyr",
    "zigzag",
    "zigzagging",
    "zilch",
    "zipper",
    "zodiac",
    "zombie"
]
word = ''
censored_word = ''
guess = ''
hangs = 0
times_found = 0
head = ' '
right_arm = '  '
torso = ''
left_arm = ' '
right_leg = ' '
left_leg = ' '
used_letters = []
cur_round = 0
running = True


def reset():
    global word, censored_word, guess, hangs, times_found, head, right_leg, left_leg, left_arm, torso, right_arm, used_letters, cur_round
    cur_round = 0
    word = ''
    censored_word = ''
    guess = ''
    hangs = 0
    times_found = 0
    head = ' '
    right_arm = '  '
    torso = ''
    left_arm = ' '
    right_leg = ' '
    left_leg = ' '
    used_letters = []


def won():
    print('''\
██╗   ██╗ █████╗ ██╗   ██╗    ██╗       ██╗ █████╗ ███╗  ██╗██╗
╚██╗ ██╔╝██╔══██╗██║   ██║    ██║  ██╗  ██║██╔══██╗████╗ ██║██║
 ╚████╔╝ ██║  ██║██║   ██║    ╚██╗████╗██╔╝██║  ██║██╔██╗██║██║
  ╚██╔╝  ██║  ██║██║   ██║     ████╔═████║ ██║  ██║██║╚████║╚═╝
   ██║   ╚█████╔╝╚██████╔╝     ╚██╔╝ ╚██╔╝ ╚█████╔╝██║ ╚███║██╗
   ╚═╝    ╚════╝  ╚═════╝       ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚══╝╚═╝
    ''')
    print(f"The word was {word}, it took you {cur_round} guesses to get it right.")
    letters = ''
    for x in used_letters:
        letters = letters+x+", "
    print(f"The letters you used: {letters}")
    reset()
    time.sleep(4)
    main()


def lose():
    print('''\
██╗   ██╗ █████╗ ██╗   ██╗      ██╗      █████╗  ██████╗████████╗      ██╗  ██╗
╚██╗ ██╔╝██╔══██╗██║   ██║      ██║     ██╔══██╗██╔════╝╚══██╔══╝      ╚═╝ ██╔╝
 ╚████╔╝ ██║  ██║██║   ██║      ██║     ██║  ██║╚█████╗    ██║            ██╔╝
  ╚██╔╝  ██║  ██║██║   ██║      ██║     ██║  ██║ ╚═══██╗   ██║            ╚██╗
   ██║   ╚█████╔╝╚██████╔╝      ███████╗╚█████╔╝██████╔╝   ██║         ██╗ ╚██╗
   ╚═╝    ╚════╝  ╚═════╝       ╚══════╝ ╚════╝ ╚═════╝    ╚═╝         ╚═╝  ╚═╝
    ''')
    print(f"The word was {word}\nThese were your guesses:")
    letters = ''
    for x in used_letters:
        letters = letters+x+", "
    print(letters,"\nBetter luck next time!")
    reset()
    time.sleep(4)
    main()


def man():
    global head, right_leg, right_arm, left_leg, left_arm, torso

    print(f'''
   +---+
   |   |
   {head}   |
  {right_arm}{torso}{left_arm}  |
  {right_leg} {left_leg}  |
       |
 [========]''')


def hang():
    global hangs, head, right_leg, right_arm, left_leg, left_arm, torso
    if hangs == 0:
        head = 'o'
    elif hangs == 1:
        right_arm = '/ '
    elif hangs == 2:
        right_arm = '/'
        torso = '|'
    elif hangs == 3:
        left_arm = '\\'
    elif hangs == 4:
        right_leg = '/'
    elif hangs == 5:
        left_leg = '\\'
    hangs = hangs+1


def guess_letter():
    global guess, used_letters
    guess = input("\nGuess a letter\n> ")
    if guess in used_letters:
        print(f"Sorry, you've already used {guess}, pick another letter.")
        guess_letter()


def main():
    global word, censored_word, wordlist, hangs, times_found, cur_round
    for x in range(35):
        print("\n")

    single_multi = input("Is this a single or multi player match?\n> ")

    if single_multi == "1" or single_multi == "single" or single_multi == "one" or single_multi == "singleplayer":
        randint = random.randint(0, 213)
        word = wordlist[randint]

    elif single_multi == "2" or single_multi == "multi" or single_multi == "two" or single_multi == "multiplayer":
        print("Alright! Guesser look away, Chooser is going to type their word in...")
        word = input("Choose your word: ").lower()
        print(f"You've chosen the word '{word}', the screen will be cleared in three seconds for the Guesser to take their turn.")
        time.sleep(3)
        for x in range(100):
            print("\n")
    else:
        print("Invalid input, please try again.")
        main()

    for x in range(len(word)):
        if word[x] == " ":
            censored_word = censored_word + " "
        else:
            censored_word = censored_word + "-"
    censored_word_pre = list(censored_word)



    while running:
        cur_round = cur_round+1
        for x in censored_word:
            if x == '-' and hangs > 5:
                lose()
            elif hangs < 5 and "-" not in censored_word:
                won()
        times_found = 0
        man()
        letters = ''
        for x in used_letters:
            letters = letters+x+", "
        print(f"The word is {len(word)} letters long: {censored_word}")
        print(f"You've used these letters: {letters}")
        guess_letter()
        used_letters.append(guess)
        for x in range(len(word)):
            if guess == word[x]:
                censored_word_pre[x] = guess
                times_found = times_found+1
        censored_word = ''
        for x in range(len(word)):
            censored_word = censored_word + censored_word_pre[x]
        if times_found > 0:
            print(f"The letter {guess} was found {times_found} times.")
        else:
            print(f"The letter {guess} was not found.")
            hang()
        time.sleep(3)
        for x in range(23):
            print()


print("Welcome!")
print("Ready to play some hangman?\n")
main()
