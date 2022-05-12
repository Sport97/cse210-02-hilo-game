from game.card import Card
card = Card()

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
        self.draw_card = ""
        self.player_card = ""
        self.is_playing = True
        self.score = 300

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
        card.draw_first_card()
        print("First Card:", card.first_card_value)

        self.player_card = input("Second card higher or lower? (h/l): ")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        card.draw_second_card()
        
        if self.player_card.lower() == "h":
            if card.second_card_value > card.first_card_value:
                card.update_points()
                self.score += card.increase_score
                print("Correct")
            else:
                card.update_points()
                self.score += card.decrease_score
                print("Incorrect")
        else:
            if card.second_card_value < card.first_card_value:
                card.update_points()
                self.score += card.increase_score
                print("Correct")
            else:
                card.update_points()
                self.score += card.decrease_score
                print("Incorrect")
        
        print(f"Second Card:", card.second_card_value)

        if self.score <= 0:
            print(self.score)
            print("Game Over")
            self.is_playing = False
        else:
            print(self.score)

    def do_outputs(self):
        """Displays the card and the score.
        Also asks the player if they want to go again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        self.draw_card = input("Draw card? (y/n): ")
        if self.draw_card.lower() == "y":
            self.is_playing = True
            self.player_card = None
        elif self.draw_card.lower() == "n":
            self.is_playing = False
        else:
            print("Choose y for yes, or n for no")