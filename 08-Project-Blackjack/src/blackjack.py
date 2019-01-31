# -*- coding: utf-8 -*-
'''
Main script for the Blackjack game
Functions for player input are implemented here
in favor of simplicity

Initial bankroll for Player1: random value between 50 and 100
'''

import deck, hand, time
import player as Player
from random import randint

# Function to get betting amount
def bet_chips(player):
  
  while True:
    
    try:
      chips = int(input('Wanna bet some chips? Press 0 for no bet: '))
    except ValueError:
      print('Invalid amount! Please try again!')
      continue
    
    if chips < 0:
      print('Invalid amount! Please try again!')
    elif chips > 0 and chips > player.chips:
      print('Not enough funds! Please try again!')
    elif chips == 0:
      print(f'Ok, no problem!')
      break
    else:
      print(f'Thanks for your bet {player.name}!')
      break
    
  return chips
      
      
# Function for hitting or staying
def hit_or_stay():
  
  while True:
  
    try:
      print('-------------------------------------------------')
      answer = int(input("Wanna hit or stay?: Press 1 for Hit, 2 for Stay: "))
      print('-------------------------------------------------')
    except:
      continue
    
    if answer in [1,2]:
      break
    else:
      continue
  
  return answer


# Print both hands
def print_hands(player,dealer):
  print('-------------------------')
  print(dealer.name + ' -> ' + str(dealer.hand))
  print('-------------------------')
  print(player.name + ' -> ' + str(player.hand))
  
  
# Check general game state
def check_game_state(player,dealer):
  
  if player.hand.value > 21:
    return 'bust'
  
  else:
    if dealer.hand.value > player.hand.value and dealer.hand.value <= 21: 
      return 'lose'
    elif dealer.hand.value > 21:
      return 'win'
    else:
      return 'play'


# Main function for playing Blackjack
def play():
  
  # Create deck
  suits = ['clubs','spades','hearts', 'diamonds']
  ranks = [str(item) for item in range (2,11)]
  ranks += ['A','J','Q','K']
  my_deck = deck.Deck(suits,ranks)
  
  # Welcome message
  print('\n\n-------------------------Welcome to Blackjack v1.0!-------------------------\n')
  
  # Create human player
  name = input("What's your name?: ")
  initial_chips = randint(50,101)
  player = Player.Player(name=name,chips=initial_chips)
  print(f'Great {name}! You will start with a chip bankroll of {str(initial_chips)}!\n')
      
  # Create computer dealer
  dealer = Player.Player(name='Dealer', chips=0)
  
  # Game loop starts here (while there are enough chips...)
  while player.chips > 0:
    
    print('\n\n-----------------------------------Match------------------------------------\n')
    # Shuffle deck and get player and dealer's card (hide 2nd card)
    print('Shuffling deck...')
    my_deck.shuffle()
    time.sleep(1)
    print(f'Player chips: {str(player.chips)}')
    player_cards = [my_deck.remove_card(),my_deck.remove_card()]
    dealer_cards = [my_deck.remove_card(),my_deck.remove_card()]
    dealer_cards[1].visible = False
 
    # Get player and dealer their hands
    player.hand = hand.Hand(player_cards)
    dealer.hand = hand.Hand(dealer_cards)
    
    # Print hands
    print_hands(player,dealer)
  
    # Ask for bet and deduce from player's bankroll
    chip_bet = bet_chips(player)
    player.chips -= chip_bet
    
    print('\n\n-----------------------------------Get Ready!------------------------------------')
    time.sleep(1)
    print('\n\n----------------------------------Player Turn------------------------------------\n')
    print(f'Player chips: {str(player.chips)}')
    time.sleep(1)
    print_hands(player,dealer)
    
    # Auxiliar state
    game_state = 'play'
    
    # After bet, choose hit or stay. If hit, additional card is given to player
    while hit_or_stay() == 1:
      
      # Hit is called so an additional card is asked
      print('Player asks for a card...\n')
      time.sleep(1)      
      player.hand.add_card(my_deck.remove_card())
      
      # Print current state of game and check if player busted
      print('\n\n----------------------------------Player Turn------------------------------------\n')
      print_hands(player,dealer)
      game_state = check_game_state(player,dealer)
      
      if game_state == 'bust':
        break
      
    
    # Player chose to stay or busted
    # If player is not bust, dealer starts hitting  
    if game_state != 'bust':
      
      print('Player stays...now it\'s dealer\'s turn!')
      time.sleep(1)
      print('\n\n----------------------------------Dealer Turn------------------------------------\n')
      print('Dealer flips his hidden card...')
      time.sleep(1)

      # Dealer shows his second card and starts hitting (if not wins)
      dealer.hand.cards[1].visible = True
      dealer.hand.check_hand_value()
      time.sleep(1)
      
      # Check before start hitting
      print_hands(player,dealer)
      game_state = check_game_state(player,dealer)

      # Dealer hits until win or bust
      while game_state == 'play':
      
        input('Dealer draws a card...Press Enter to continue...')
        time.sleep(1)
        dealer.hand.add_card(my_deck.remove_card())
        
        # Check game state after dealer draws
        print('\n\n----------------------------------Dealer Turn------------------------------------\n')
        print_hands(player,dealer)
        game_state = check_game_state(player,dealer)
        
        
      # Endgame: after dealer hitting, we check if player won or lost
      if game_state == 'win':
        print(f"You win this match!. You are granted with {str(chip_bet*2)} chips!")
        player.chips += (2*chip_bet)
        
      elif game_state == 'lose':
        print(f"Sorry, you lost this match! You lost your bet of {str(chip_bet)} chips")
        
      
    else:
      print(f"Sorry, you're busted! You lost your bet of {str(chip_bet)} chips")
      dealer.hand.cards[1].visible = True
      
      
    # Restart deck with used cards
    print('\n\n-----------------------------------Match End------------------------------------\n')
    print('Returning cards to deck...')
    time.sleep(1)
    used_cards = player.hand.cards + dealer.hand.cards
    for card in used_cards:
      my_deck.add_card(card)
      
    # Continue message  
    if player.chips > 0:
      input(f'You still have {str(player.chips)} chips to play. Press Enter to continue or Ctrl+C to exit game')
    else:
      print('You have no chips left to play. Backjack Game is over!')
      

if __name__ == '__main__':
  play()