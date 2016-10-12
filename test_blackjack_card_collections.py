import pytest
from blackjack_card_collections import *

################################################################################
# Unit tests for blackjack_card_collections.py
################################################################################

def test_docstring():
    deck = Deck ()
    assert 'list of 52 cards each a dict with name, suit keys' in deck.__doc__

def test_cards_in_Deck():
    deck = Deck()
    assert hasattr(deck, "Cards") == 1

def test_count_cards_in_Deck():
    deck = Deck()
    counter = 0
    while deck.Cards:
        deck.Cards.pop()
        counter = counter +1
    assert counter == 52

def test_count_suits_in_Deck():
    deck = Deck()
    spades, clubs, hearts, diamonds = [0, 0, 0, 0]
    for card in deck.Cards:
        if card['suit'] == 'Spades':
            spades = spades + 1
        elif card['suit'] == 'Clubs':
            clubs = clubs + 1
        elif card['suit'] == 'Hearts':
            hearts = hearts + 1
        elif card['suit'] == 'Diamonds':
            diamonds = diamonds + 1
    assert [spades, clubs, hearts, diamonds] == [13, 13, 13, 13]
