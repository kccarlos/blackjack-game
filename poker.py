import random

class Card (object):

    LETTERS = [str(i) for i in range(2, 11)] + ['A', 'J', 'Q', 'K']
    SPECIAL_VAL = {'A': 11, "J": 10, "Q": 10, "K": 10}
    SUITS = ['S', 'D', 'H', 'C']

    def __init__ (self, letter, suit):
        """Card object constructor.

        Keyword arguments:
        letter -- string. One of LETTERS
        suit -- string. One of SUITS
        """
        self.letter = letter
        self.suit = suit

    def __str__ (self):
        """Return the card letter/number as Card object's string formatting"""
        return self.letter

    def __int__(self):
        """Return the point of card as Card object's integer formatting"""
        if self.letter in self.SPECIAL_VAL:
            return self.SPECIAL_VAL[self.letter]
        else:
            return int(self.letter)


class Deck(object):

    def __init__(self):
        """Deck object constructor.

         Create a Deck made of 52 Cards objects
         """
        self.deck = []
        for suit in Card.SUITS:
            for letter in Card.LETTERS:
                card = Card(letter, suit)
                self.deck.append(card)

    def shuffle(self):
        """Shuffle the card"""
        random.shuffle(self.deck)

    def __len__(self):
        """Return remaining card number in the deck"""
        return len(self.deck)

    def deal(self):
        """Return the first card of the deck

        Return -- Card object / None if no card available
        """
        return self.deck.pop(0) if len(self) > 0 else None
