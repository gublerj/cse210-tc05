

class Player:
    """
    keep track of parachute
    check if player won/lost

    """
    def __init__(self):
        """Initializes the class
        """
        self.lives = 5

    def count_lives(self,correct):
        """
        count how many wrong guesses
        returns a number
        """
        if correct:
            return self.lives
        else:
            self.lives -= 1
            return self.lives

    def win(self, actual_word, guessed_word):
        """
        check if they won
    
        """
        if actual_word == guessed_word:
            return True
        else:
            return False


    def loose(self):
        """
        check if they lost
        """
        if self.lives < 1:
            return True
        else:
            return False