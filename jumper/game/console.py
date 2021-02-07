
class Console:
    def __init__(self):
        self.guess = ""

    def display_word(self, blank):
        """
        Prints _ or correct letter for the guessed word from the array
        """   
        for x in blank:
            print(x)

    
    def display_jumper(self, lives):
        """
        prints parachute to console based on how many wrong guesses they made
        if they lose tell them
        """
        stages = [
                    """
                     _____
                    /_____\\
                    \     /               
                     \   /
                       0
                      /|\\
                      / \\

                    ^^^^^^^
                    """
                    ,

                     """

                    /_____\\
                    \     /               
                     \   /
                       0
                      /|\\
                      / \\

                    ^^^^^^^
                    """
                    ,

                     """

                    \     /               
                     \   /
                       0
                      /|\\
                      / \\

                    ^^^^^^^
                    """
                    ,

                     """
                               
                     \   /
                       0
                      /|\\
                      / \\

                    ^^^^^^^
                    """
                    ,

                     """
                       0
                      /|\\
                      / \\

                    ^^^^^^^
                    """
                    ,

                    """
                       x
                      /|\\
                      / \\

                    ^^^^^^^
                    """
        ]

        if lives == 5:
            print(stages[0])
        elif lives == 4:
            print(stages[1])
        elif lives == 3:
            print(stages[2])
        elif lives == 2:
            print(stages[3])
        elif lives == 1:
            print(stages[4])
        else:
            print(stages[5])



    def get_guess(self):
        """
        prompts user for guess
        """
        self.guess = input("Guess a letter [a-z]: ")

        return self.guess 
