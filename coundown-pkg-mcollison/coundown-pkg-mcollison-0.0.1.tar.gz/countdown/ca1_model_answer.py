"""
This module is a program that simulates the channel 4 game show countdown
from a command-line interface. This simulation runs a single player version
with only one round.
"""
import model_ans_test
from itertools import combinations
from random import choice
from threading import Timer

WORDS_FILE = 'words.txt'
WELCOME_ASCII_FILE = "countdown.txt"
CONSONANTS_FILE = "consonants.txt"
VOWELS_FILE = "vowels.txt"
TIME_ALLOWED = 30
timeout = False

def select_characters(testing: bool = False, letters: int = 9) -> str:
    """
    User generates an 9 character random string of consonants and vowels

    Arguments:

    :param testing: a boolean to activate a testing behaviour
    :param letters: can be used to define number of letters in the game
    """
    consonants = ascii_ui(CONSONANTS_FILE) #load the consonant letters
    vowels = ascii_ui(VOWELS_FILE) #load the vowel letters
    selected_characters = "testdatas" if testing else ""
    while len(selected_characters) < letters:
        user_input = input("Please enter 'c' for a consonant or 'v' for a " +
                           "vowel...")
        if user_input == 'c':
            selected_characters = selected_characters + choice(consonants)
        elif user_input == 'v':
            selected_characters = selected_characters + choice(vowels)
        else:
            print("the character or characters entered can not be ",
                  "interpreted as 'c' or 'v'. ")
    return selected_characters

def read_dictionary(filename: str) -> list:
    """
    creates a list of words from a file containing all possible words

    Arguments:
    :param filename: a string containing the filename of the dictionary file
    """
    with open(filename) as dictionary_file:
        return dictionary_file.read().split()

def word_lookup(letters: str) -> list:
    """This functions finds all words that can be made from a set of letters

    The function returns only the longest words and finds all combinations of
    letters that can be used to make corresponding words, using a sorted
    combination algorithm.

    Arguments:
    :letters: the possible characters that can be used to generate the words
    """
    words = read_dictionary(WORDS_FILE) # import words from file
    # sort words alphabetically
    sorted_words = [''.join(sorted(x.lower())) for x in words]
    # sort letters alphabetically
    sorted_word = ''.join(sorted(letters))
    matches = [] # initialise return list
    # starting from longest word iterate down to zero
    for i in range(len(sorted_word), 0, -1):
        # generate all combinations of letters for given length
        for substring_letters_list in combinations(sorted_word, i):
            substring_letters = "".join(substring_letters_list)
            #if sorted combination of letters matches sorted words list - hit
            if substring_letters in sorted_words:
                # find the index of the hit from sorted list
                start_index = -1
                while True:
                    try:
                        index = sorted_words.index(substring_letters,start_index+1)
                        # use index to identify the original word and add to results
                        matches.append(words[index])
                        start_index = index
                    except ValueError:
                        break

        # if there are results for given length return before trying
        # shorter words
        if matches:
            return matches
    return matches #this is likely empty here

def ascii_ui(filename: str) -> str:
    """Read basic ascii text from files and returns the string"""
    with open(filename) as file:
        return file.read()

def input_check() -> None:
    """Function is triggered if timeout is reached in secondary thread"""
    global timeout
    timeout = True
    print('Sorry, times up. Please press enter to continue')

def timed_input(timeout_time: int) -> str:
    """Threaded handling function to time the user input"""
    time_thread = Timer(timeout_time, input_check)
    time_thread.start()
    prompt = "You have %d seconds to input your answer...\n" % timeout_time
    user_guess = input(prompt)
    time_thread.cancel()
    return user_guess

def game_play() -> None:
    """The main game logic is contained here"""
    print(ascii_ui(WELCOME_ASCII_FILE)) #print the welcome intro
    #game logic
    user_letters = select_characters() #get the selections from the user
    print("The letters for this game are: " + user_letters) #display random letters
    user_guess = timed_input(TIME_ALLOWED)
    dictionary_words = read_dictionary(WORDS_FILE) #load dictionary file for comparison
    if not timeout:
        user_guess_sorted = ''.join(sorted(user_guess)) #user input sorted for comparison
        #check user input contains letters and is a valid word
        for letter_combi in combinations("".join(sorted(user_letters)), len(user_guess)):
            if "".join(letter_combi) == user_guess_sorted and user_guess in dictionary_words:
                print("Well done you scored " + str(len(user_guess)) + " points.")
                break #only needs to be correct once
    if timeout or user_guess not in dictionary_words:
        print("You scored zero points.")
    #calculate best answers for final results display
    best_answers = word_lookup(user_letters)
    print("The best answers would have scored " + str(len(best_answers[0])))
    print("The best answers were:")
    # cast results as a set to remove redundancy
    best_answers_set = set(best_answers)
    for ans in best_answers_set:
        print(ans)
    print(ascii_ui("countdown-outro.txt"))


if __name__ == "__main__":
    #program setup
    try:
        model_ans_test.tests()
    except AssertionError as message:
        print(message)
    game_play()
