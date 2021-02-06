 """
 check guesses
 keep track of parachute
check if player won/lost

 """

class Player:
        
    def __init__(self):
        self.lives = 5

        pass

    def count_wrong(self,correct):
        """
        count how many wrong guesses
        returns a number
        """
        if correct:
            return self.lives
        else:
            return self.lives - 1
        pass

    def win():
        """
        check if they won
    
        """
        pass


    def loose():
        """
        check if they lost
        """
        pass