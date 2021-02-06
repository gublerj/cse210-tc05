from game.console import Console
from game.player import Player
from game.puzzle import Puzzle

class Director:
    """

    import classes and control flow

    """
    def __init__(self):
        self.puzzle = Puzzle()
        self.player = Player()
        self.console = Console()
        self.word = self.puzzle.generate_word()
        self.guesses = self.puzzle.create_blank_array()
        self.is_correct_guess = False
        self.lives = 5
        self.guess = ''

    def start_game(self):
        """
        this starts the game and keeps it running

        It starts with self.do_outputs before entering loop to initialize the puzzle
        """
        self.do_outputs()
        while self.player.loose() == False or self.player.win == False:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """
        This will get inputs from the player to keep the game running
        """
        self.guess = self.console.get_guess("Guess a Letter: ")
        self.is_correct_guess = self.puzzle.check_guess(self.guess)

    def do_updates(self):
        """
        This takes the input and updates all arrays
        """
        self.lives = self.player.count_lives(self.is_correct_guess)
        self.guesses = self.puzzle.update_array(self.guess)
    
    def do_outputs(self):
        """
        This will output the parachut and the array.
        """
        self.console.display_word(self.guesses)
        self.console.display_jumper(self.lives)



