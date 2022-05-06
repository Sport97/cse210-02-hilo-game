from game.card import Card

class Director:
    """
    Responsibility:
        control the sequence of play
        
        Attributes:
            is_playing: boolean
            score: int
            final_score: int
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.final_score = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Ask the user if they want higher or lower card.

        Args:
            self (Director): An instance of Director.
        """
        # Adil Rafi (remove pass once finished)

        pass

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        # Oleksii Zaloznyi (remove pass once finished)

        pass

    def do_outputs(self):
        """Displays the card and the score.
        Also asks the player if they want to go again. 

        Args:
            self (Director): An instance of Director.
        """
        # Stephen Port

        pass