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
        self.first_card = Card.draw_first_card()
        self.second_card = Card.draw_second_card()
        self.draw_card = None
        self.player_card = None
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
        print(f"First Card: {self.first_card}")

        while self.player_card.lower() != "h" or self.player_card.lower() != "l":
            self.player_card = input("Draw higher card or lower card? (h/l): ")
        else:
            print("Choose h for higher, or l for lower.")

        # Adil Rafi (remove pass once finished)

    def do_updates(self):
        """Updates the player's score.
        The player earns 100 points if they guessed correctly.
        The player loses 75 points if they guessed incorrectly.

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
        print(f"Next Card: {self.second_card}")

        if self.final_score == 0:
            print(self.final_score)
            self.is_playing = False
        else:
            print(self.score)
            self.draw_card = input("Draw card? (y/n): ")
            if self.draw_card.lower() == "y":
                self.is_playing = True
                self.player_card = None
            elif self.draw_card.lower() == "n":
                self.is_playing = False
            else:
                print("Choose y for yes, or n for no")

        # Stephen Port