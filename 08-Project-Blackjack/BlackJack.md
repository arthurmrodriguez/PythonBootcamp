# Milestone Project 2 - Blackjack Game

This project requires us to create a simple in-line Blackjack game with **one human player** and an **automated dealer**. As this is a simplified version of the game, we will focus on the following game states, actions and objects.

## Gameplay

The **player** starts with two cards facing up and the **dealer** starts with one card facing up and one facing down. The **player** has a predefined (or user defined) amount of **chips** in order to **bet** after seeing his hand. Then, the game starts as described below:

  1. The **player** chooses an amount to **bet** (from his chips), and then he can either **hit** (ask for a card) or **stay** (not receive cards anymore).

  1.1. If the player **busts** (goes over 21) he loses and will also lose his bet.

  2. After player's turn, there can be different ways for the game to end. If player **stayed under 21**, the **dealer** will always hit until one of the following things happen:

  2.1. **Dealer** hits until the value of hand is **greater** than the players: **player loses** and loses bet.

  2.2. **Dealer** hits over 21: **player wins** and wins the double of the amount placed as a bet.

The game can go on while **player has chips to bet** or while Ctrl+C is not pressed (exit game). There're also some special rules to be considered for both **player and dealer**

1. *Jack*, *Queen* or *King* cards have a value of 10.
2. *Aces* can count as either 1 or 11, depending on the hand.

The development of the game can be seen in the **src** folder, where every single script will be properly commented. We chose to use **separated scripts** over *jupyter notebooks* to make it look like a real Python project. Also, we choose **simplicity** over *complexity* when it comes to develop this game.
