import random

class Card:
    """
    Responsibility:
        keep track of the first card random value and
        second card random value, then calculate the points for the player.
    Attributes:
        first_card_value: int
        second_card_value: int
        increase_score: int
        decrease_score: int
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.first_card_value = 0
        self.second_card_value = 0
        self.new_card_value = 0
        self.increase_score = 100
        self.decrease_score = -75
        self.new_score = 0
    
    def draw_first_card(self):
        """Draws first card value.
        
        Args:
            self (Director): an instance of Director.
        """
        self.first_card_value = random.randint(1, 13)

    def draw_second_card(self):
        """Draws second card value, different from first card value.
        
        Args:
            self (Director): an instance of Director.
        """
        self.new_card_value = random.randint(1, 13)

        if self.new_card_value == self.first_card_value:
            self.second_card_value = random.randint(1, 13)
        else:
            self.second_card_value = self.new_card_value
    
    def update_points(self):
        """Update player points based on guess.
        
        Args:
            self (Director): an instance of Director.
        """
        self.increase_score = 100
        self.decrease_score = -75