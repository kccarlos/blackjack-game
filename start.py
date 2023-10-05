from player import Player, Dealer
from poker import Card, Deck

if __name__ == "__main__":
    # 0. Initialize game data
    gameOn = True
    playerNotStand = True
    deck = Deck()
    deck.shuffle()

    # 1. Deal initial cards (two cards to each player)
    dealer = Dealer(deck.deal(), deck.deal())
    player = Player(deck.deal(), deck.deal())

    while playerNotStand:
        # 2. Display initial hands (hiding dealer's second card and score)
        print('Dealer has: ' + dealer.commandLineShowHand(True))
        print('Player has: ' + player.commandLineShowHand(False))
        if player.getScore() > 21:
            print('Player busts with %i' % player.getScore())
            print('Dealer wins!')
            gameOn = False
            break
        elif player.getScore() == 21:
            print('Player wins!')
            print('Blackjack!')
            gameOn = False
            break
        # 3. Prompt user (Hit or Stand?)\
        if player.hitOrNot():
            player.hit(deck.deal())
        else:
            playerNotStand = False
            print('Player stands with: ' + player.commandLineShowHand(False))
            break

    # Reveal dealer's card
    if gameOn:
        print('Dealer has: ' + dealer.commandLineShowHand(False))
        if dealer.getScore() == 21:
            print('Dealer wins!')
            print('Blackjack!')
            gameOn = False

    # 4. Dealer plays (if player has neither busted nor won)
    if gameOn:
        while dealer.hitOrNot():
            print('Dealer hits')
            dealer.hit(deck.deal())
            print('Dealer has: ' + dealer.commandLineShowHand(False))
            if dealer.getScore() > 21:
                print('Dealer busts with %i' % dealer.getScore())
                print('Player wins!')
                gameOn = False
                break
            elif dealer.getScore() == 21:
                print('Dealer wins!')
                print('Blackjack!')
                gameOn = False
                break

    # 5. Decide and report the winner, including hands and scores where relevant
    if gameOn:
        if player.getScore() > dealer.getScore():
            print('Player win!')
        elif player.getScore() == dealer.getScore():
            print('Tie!')
        else:
            print('Dealer win!')

        print("%s to Dealer's %s" %(player.commandLineShowHand(False),
                                    dealer.commandLineShowHand(False)))

    exit(0)
