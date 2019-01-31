'''
Class Card: stores the information of a Card
used for our Blackjack game
'''

# Defines a specific card
# suit: clubs, diamonds, hearts, spades
# rank: A, 2-10, J, Q, K (simplified)
# value: from 2 to 11 . A = 11 (simplified)
# visible: True-False
class Card():

    # Constructor
    def __init__(self, suit, rank, visible = True):

        self.suit = suit
        self.rank = rank
        self.visible = visible

        if rank in ['10', 'J', 'Q', 'K']:
            self.value = 10
        elif rank == 'A':
            self.value = 11
        elif rank in [str(item) for item in range(2,11)]:
            self.value = int(rank)

    # Dunder method: str
    def __str__(self):
        
        if self.visible:
            return f'{self.rank} of {self.suit}'
        else:
            return 'X'
