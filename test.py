import unittest

from player import Player, Dealer
from poker import Card, Deck

class Test_deck(unittest.TestCase):
    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(len(deck), 52, "incorrect number of pocker cards")

class Test_player(unittest.TestCase):
    def test_score_with_ace_1(self):
        dealer = Dealer(Card('A', 'S'), Card('A', 'S'))
        self.assertEqual(dealer.getScore(), 12, "AA != 12")
        dealer.hit(Card('A', 'S'))
        self.assertEqual(dealer.getScore(), 10+1+1+1, "A A != 13")

    def test_score_with_ace_2(self):
        dealer = Dealer(Card('A', 'S'), Card('2', 'S'))
        dealer.hit(Card('2', 'S'))
        self.assertEqual(dealer.getScore(), 11+2+2, "A 2 2 != 15")

    def test_score(self):
        dealer = Dealer(Card('J', 'S'), Card('2', 'S'))
        dealer.hit(Card('5', 'S'))
        self.assertEqual(dealer.getScore(), 10+2+5, "J 2 5 != 17")

    def test_score_print(self):
        dealer = Dealer(Card('A', 'S'), Card('2', 'S'))
        self.assertEqual(dealer.commandLineShowHand(True),
                        "A ? = ?",
                        "Hide failed!")
        self.assertEqual(str(dealer.commandLineShowHand(False)),
                        "A 2 = 13",
                        "reveal failed!")

unittest.main()
