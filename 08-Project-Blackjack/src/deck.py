'''
Class Deck: stores the information of a
set of cards and manages the main operations
like shuffle, add or remove a card from the deck
'''

import card
import random
class Deck():

    # Constructor
    def __init__(self, suits, ranks):

        self.suits = suits
        self.ranks = ranks
        self.cards = list()

        for suit in suits:
            for rank in ranks:
                self.cards.append(card.Card(suit,rank))

    # Methods for shuffling the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)

    # Method for adding a new card only
    def add_card(self,card):
        if card not in self.cards:
            self.cards.append(card)
        else:
            print(f'Card {card} is already on deck')

    # Method to remove the indicated card
    def remove_card(self, index = 0):
        return self.cards.pop(index)

    # Dunder method str
    def __str__(self):
        cards = ''
        for card in self.cards:
            cards += str(card)+'\n'
        return cards
