"""
generate word, send back to director

check if guess is right
"""
import random

class Puzzle:
    def __init__(self):
        self.blank = []
        self.word = []

    def create_blank_array(self):
        """
        checks how many letters there are in the word (self.word)
        puts that many _ in self.blank
        """

        for x in self.word:
            self.blank.append('_')

        return self.blank

    def generate_word(self):
        """
        randomly

        returns a word in the form of a list of letters (an array)
        """

        word_list = []
        
        with open("cse210-tc05\jumper\game\words.txt") as file:
            for line in file:
                if len(line) > 4:
                    word_list.append(line)
        
        self.word = random.choice(word_list)
        self.word = list(self.word)
        self.word.pop()

        return self.word

    def check_guess(self, user_guess):
        """
        if correct, 

        return boolean
        """
        count = 0
        for x in range(0, len(self.word)):
            if user_guess == self.word[x]:
                return True
        return False

    def update_array(self, user_guess):
        """
        checks to see if user_guess is in the word, then replaces
        a '_' with the letter if it is
        """
        
        for i in range(0, len(self.word)):
            if user_guess == self.word[i]:
                #user_guess = self.blank[i]
                self.blank[i] = user_guess
                print(self.blank[i])

        return self.blank
