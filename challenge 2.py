# 1 Card War
# Author: Bo Meers
# Date: 24/2/15

gameOver = 0
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["c", "d", "h", "s"]
cards = []
hand1 = ""
hand2 = ""
import random
import time

print("""
                           Welcome to One Card War.

                    the objective of the game is to flip
                  a card that is higher than your opponent.""")
    
player1 = input("\n\nPlayer 1, what is your name? ")
player2 = input("Player 2, what is your name? ")


while gameOver != 1:
    
    for suit in SUITS:
        for rank in RANKS:
            card = rank + suit
            cards.append(card)

    input("""
                 Alright, here's your cards... now flip them!
                         Press <Enter> to flip. """)
    
    hand1 = random.choice(cards)
    cards.remove(hand1)
    hand2 = random.choice(cards)
    cards.remove(hand2)

    print("\n" + player1 + " had a " + hand1)
    print(player2 + " had a " + hand2)

    choice = input("\nPlay again: (Y/N) ")
    if choice in ("N", "n"):
        gameOver = 1
