################################################################################
# Hand Class
################################################################################
class Hand():
    """
    A single hand of cards
    """
    def __init__(self):
        self.score = 0
        self.still_in_round = True
        self.bet = 10
        self.cards = {}

################################################################################
# Person (Parent), Player and Dealer (Children) Classes
################################################################################
class Person():
    """
    Parent class for anyone playing BlackJack
    """
    def __init__(self, name):
        self.name = name
        self.hands = [Hand()]

    # add random card to hand
    def hit(self):
        pass

    # make decision to stand
    def stand(self):
        pass

class Player(Person):
    """
    Child class for Player that inherits from Person class
    Extends upon decisions that Person can make
    """
    def __init__(self, name):
        Person.__init__(self, name)
        self.purse = 100
        self.still_in_game = True

    # make decision to split hand in two; can only do with matching cards
    def split(self):
        pass

    # make decision to double bet and receive only one more card
    def double(self):
        pass

    # make decision to surrendur and get half BET back
    def surrender(self):
        pass

    # call out blackjack; out of hand
    def blackjack(self, hand):
        pass

class Dealer(Person):
    """
    Child class for Dealer that inherits from Person class
    Cannot make any decisions other than those from Person
    """
    def __init__(self, name):
        Person.__init__(self, name)
