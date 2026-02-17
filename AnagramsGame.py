
#Point values:
# 6 letters - 2000
# 5 letters - 1200
# 4 letters - 400
# 3 letters - 100
# Two letters and below do not count.

class AnagramsGame:
    #needs to track a wordlist, score, time limit, words found, and current letters

    def __init__(self):
        pass

    #function to generate a set of letters, will need to make sure it's random but we guarantee a mix of vowels and consonants for shit to actually work
    
    #most likely, asynchronous function to handle the timer decoupled from everything else, for 60 seconds

    #function to start a new round, calls the function to generate random letters, reset the score and words found, call function to start the timer and return the current letters and starting time

    #function to submit a "word", three letters minimum, checks the word against words found first and then the dictionary of words, returns true or false and the number of points scored, saves word into words found

    #function to get the state of the game, returns the time remaining and the score

    #function to end the game, called when the timer ends, does SOMETHING with the total score and words found

    def play(self):
        print("Welcome to Anagrams!")
        # Game logic goes here

print("Hello World!")