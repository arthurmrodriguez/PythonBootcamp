'''
Class Hand: stores the information of a player's
hand for our Blackjack game
'''

class Hand():
  
  # Global variable
  limit = 21
  
  # Constructor
  def __init__(self, cards):
    
    self.cards = cards
    self.value = 0
    self.check_hand_value()

  # Check hand value  
  def check_hand_value(self):
    
    self.value = 0
    for card in self.cards:
      if card.rank == 'A' :
        if self.value+card.value > Hand.limit:
          card.value = 1
          
      self.value += card.value
    
  # Add card to hand
  def add_card(self, card):
    self.cards.append(card)
    self.check_hand_value()
    
  # Remove cards from hand
  def remove_cards(self):
    self.cards.clear()
    
  # Dunder method set
  def __str__(self):
    
    cards = f'Hand value: {self.value}\n'
    for card in self.cards:
      cards += str(card)+'\n'
    return cards