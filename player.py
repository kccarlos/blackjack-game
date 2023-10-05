class Player(object):

    def __init__(self, card1, card2):
        """Player object constructor.

        Initialize with 2 initial cards

        Keyword arguments:
        card1 -- Card object
        card2 -- Card object
         """
        self.hand = []
        self.hand.append(card1)
        self.hand.append(card2)

    def hitOrNot(self):
        """Return the decision of hitting or holding
        by asking user input

        return True (to hit) / False (to hold)
         """
        userInput = input('Would you like to (H)it or (S)tand? ')
        while userInput not in ['H', 'S']:
            print('Invalid input, please re-enter')
            userInput = input('Would you like to (H)it or (S)tand? ')
        print()
        return True if userInput == 'H' else False

    def hit(self, card):
        """Add card to hand of this player

        Keyword arguments:
        card -- card to be added to hand
        """
        return self.hand.append(card)

    def getScore(self):
        """Return the score of current hand
        If player has Ace, return a score version closest to 21
        """
        score = sum([int(card) for card in self.hand])
        numOfA = sum([str(card) == 'A' for card in self.hand])
        if numOfA == 0:
            return score
        while score > 21:
            if numOfA == 0:
                break
            score -= 10
            numOfA -= 1
        return score

    def commandLineShowHand(self, hidden):
        """Return a printable version of hand with current score

        Keyword arguments:
        hidden -- boolean. True to only reveal one card
        """
        if not hidden:
            cardStrings = ' '.join([str(card) for card in self.hand])
            scoreString = str(self.getScore())
        else:
            numHand = len(self.hand)
            scoreString = '?'
            if numHand == 0:
                cardStrings = str(self.hand[0])
            else:
                cardStrings = str(self.hand[0]) + ' ?' * (numHand - 1)
        output = '%s = %s' % (cardStrings, scoreString)
        return output


class Dealer(Player):
    def __init__(self, card1, card2):
        """Dealer object constructor"""
        super().__init__(card1, card2)

    def hitOrNot(self):
        """Return the decision of hitting or holding
        Rule: hit until the hand's score >= 17

        return True (to hit) / False (to hold)
         """
        return True if self.getScore() < 17 else False
