from pathlib import Path
import random
from collections import Counter


#Point values:
# 6 letters - 2000
# 5 letters - 1200
# 4 letters - 400
# 3 letters - 100
# Two letters and below do not count.

#Uses Path from the pathlib library to find our current file path and the word list without having to deal with a bunch of absolute/relative pathing BS ourselves.
CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parent.parent
WORDLIST_PATH = PROJECT_ROOT / "Collins Scrabble Words (2019).txt"

class AnagramsGame:
    #needs to track a wordlist, score, time limit, words found, and current letters

    def __init__(self, dictionary_path=WORDLIST_PATH):

        with open(dictionary_path, "r") as wordfile:
            self.wordlist = set(word.strip().upper() for word in wordfile)
        
        self.score = 0
        self.time_limit = 60
        self.words_found = set()
        self.rack = []

        self.valid_letters = (
            ['A']*9 + ['B']*2 + ['C']*2 + ['D']*4 + ['E']*12 + ['F']*2 + 
            ['G']*3 + ['H']*2 + ['I']*9 + ['J']*1 + ['K']*1 + ['L']*4 + 
            ['M']*2 + ['N']*6 + ['O']*8 + ['P']*2 + ['Q']*1 + ['R']*6 + 
            ['S']*4 + ['T']*6 + ['U']*4 + ['V']*2 + ['W']*2 + ['X']*1 + 
            ['Y']*2 + ['Z']*1
        )

    #function to start a new round, calls the function to generate random letters, reset the score and words found, call function to start the timer and return the current letters and starting time
    def new_round(self):
        self.rack = random.sample(self.valid_letters, 6)
        self.score = 0
        self.words_found = set()

        return self.get_state()

    
    #most likely, asynchronous function to handle the timer decoupled from everything else, for 60 seconds

    #function to submit a "word", three letters minimum, checks the word against words found first and then the dictionary of words, returns true or false and the number of points scored, saves word into words found
    
    
    ##Note: We start the name with an underscore to signal that this is gonna just be an internally-used function, kinda like using private in other languages.
    def _calculate_score(self, word):
        length = len(word)
        match length:
            case 6:
                return 2000
            case 5:
                return 1200
            case 4:
                return 400
            case 3:
                return 100
            case _:
                return 0
    

    def submit_word(self, word):
        word = word.upper()
        
        #First, check if the word is in our found words.
        if word in self.words_found:
            return False, 0

        #Then we gotta check if the word is even in the dictionary.
        if word in self.wordlist:
            return False, 0

        #If it passes both of those checks, now we check if the word is in our rack, and if so, we reward the appropriate amount of points!
        rack_letter_counts = Counter(self.rack)
        word_letter_counts = Counter(word)

        #Subtracting these from each other essentially checks if every letter in our word can be found in the rack. The subtraction on its own, if it's valid and every letter is in the rack, will just be a []. We use a not to negate that nothing, making this a successful condition if every letter is in the rack.
        if not (word_letter_counts - rack_letter_counts):
            points = self._calculate_score(word)
            self.score += points
            self.words_found.add(word)

            return True, points
        
        return False, 0

    #function to get the state of the game, returns the time remaining and the score
    def get_state(self):
        return {
            "rack": self.rack,
            "score": self.score,
            "words_found": self.words_found
        }

    #function to end the game, called when the timer ends, does SOMETHING with the total score and words found

    def play(self):
        print("Welcome to Anagrams!")
        # Game logic goes here