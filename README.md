# BlackJack Game

## Table of Contents


<ol>
  <li>
    <a href="#project-introduction-and-requirements">Project Introduction and Requirements</a>
  </li>
  <li>
    <a href="#running-and-testing">Running and Testing</a>
  </li>
  <li>
    <a href="#assumptions">Assumptions</a>
  </li>
  <li>
    <a href="#strength">Project Strength</a>
  </li>
  <li>
    <a href="#design-rationale">Rationale on design choices, algorithmic decisions made</a>
  </li>
  <li>
    <a href="#tradeoffs">Tradeoffs</a>
  </li>
  <li>
    <a href="#future-improvement-opportunities">Future Improvement Opportunities</a>
  </li>
</ol>

## Project Introduction and Requirements

### Introduction

Blackjack is a card game. We'll use a single standard 52-card deck. This deck has:

- "number cards" with a face value of 2-10, worth the number on the card "face cards" (King, Queen, Jack), each worth 10 points
- "aces" (Ace), worth 1 or 11 points. The value is chosen so that the sum of the cards is as close to 21 as possible without exceeding 21.

The above cards constitute a "Suit" in a deck. A deck consists of four suits. The suit names are unimportant, and can be ignored for the purposes of this game. The important thing is that each deck has four twos, four kings, four aces, and so on.

All 52 cards should be present in the deck at the start of the game. The cards dealt should be randomized during play - the cards dealt should not be predictable.

For our Blackjack game, there are two players: the human (you) and the dealer (controlled by the computer).


### Gameplay Overview

1. Deal initial cards (two cards to each player)
2. Display initial hands (hiding dealer's second card and score)
3. Prompt user (Hit or Stand?)
   * Hit: add card to hand (check if busted)
   * Stand: end turn
   * show updated hand and value
   * repeat until player has stood, won (score == 21), or busted (score > 21)
4. Dealer plays (if player has neither busted nor won)
   * print dealer's full hand, score
   * dealer keeps hitting until score >= 17
5. Decide and report the winner, including hands and scores where relevant

### Winning

- Each player's objective is to get as close to 21 points as possible without going over.
- The human wants to outscore the dealer, despite not knowing the dealer's score.
- The dealer plays by a simple rule: hit until the hand's score is greater than or equal to 17 ("stand on 17"). For our game there is no betting, no splitting, no doubling down. This is a simple game.


## Running and Testing

- The program was tested on Python 3.9.13. It should work with all Python 3+ versions
- To start the program, use the command as follows:

```
python start.py
```

- To run the test, use the following command:

```
python test.py
```


## Project Strength

- My implementation can fulfill the listed functional requirements.
- It follows Object-oriented programming (OOP) practices.
- Functions and game logic are well-commented.

## Design Rationale

**Rationale on design choices, algorithmic decisions made?**

- I followed Object-oriented programming (OOP) by defining **classes** such as `Player`, `Card`, and `Deck`.
  - OOP enables code reusability. For example, if we want to support another poker game, we can reuse the `Card` class.
  - Encapsulate details to reduce coupling. For example, the code for stringifying `Card` and `Player`'s hand is hidden from game logic in `start.py` by overriding the built-in `__str__` and `__int__` functions. Changing these in the future is easier by keeping different components of the game independent.

- When implementing `Dealer`, I used **inheritance** so that `Dealer` can reuse multiple behaviors of `Player`. Additionally, changing `Dealer`'s strategy in the future won't affect the parent class `Player`.


## Tradeoffs

**Tradeoffs you encountered while programming and how you resolved them**

- This project is pretty lightweight. So I did not try to break the existing four classes into even smaller pieces and place them into different `.py` files or folders. Because doing so may make the program difficult to read.

- However, I acknowledge that my implementation still has a high coupling level. For a larger project, for example, a multi-player game supporting several poker game versions, it's better to define more classes and follow SOLID principles like single responsibility, open close, etc.


## Future Improvement Opportunities

- Refactor the game logic code in `start.py` into a `Game` class. It takes parameters like game states and `Player` instances and will be responsible for controlling the game workflow. This change will allow
  - extendability to other kinds of poker games
  - easy for unit testing
  - avoid the code smells like long methods and duplicate code in `start.py`
- Create test cases on the game logic. The test cases I have written are insufficient and cannot cover the game logic.
