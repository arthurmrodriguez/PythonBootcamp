'''
Class Player: holds the information about current player's
status, regarding his name, amount of chips available for bet
and the current hand
'''

import hand
class Player():
  
  # Constructor
  def __init__(self, name='player1', current_hand=list(), chips = 0):
    
    self.name = name
    self.hand = hand.Hand(current_hand)
    self.chips = 0
