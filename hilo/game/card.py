import random

class Card:
    """
    Responsibility:
        keep track of the first card random value and
        second card random value
    Attributes:
        first_card_value: int
        second_card_value: int
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.first_card_value = 0
        self.second_card_value = 0
    
    def draw_first_card(self):
        """Draws first card value.
        
        Args:
            self (Director): an instance of Director.
        """
        # Adil Rafi (remove pass once finished)

        self.first_card_value = random.randint(1, 13)


    def draw_second_card(self):
        """Draws second card value, different from first card value.
        
        Args:
            self (Director): an instance of Director.
        """
        # Oleksii Zaloznyi (remove pass once finished)

        pass