import pytest
from blackjack_persons import *

################################################################################
# Unit tests for blackjack_persons.py
################################################################################

def test_docstring():
    hand = Hand()
    assert 'A single hand of cards' in Hand.__doc__

def test_hand_score():
    hand = Hand()
    assert hand.score == 0

def test_hand_still_in_round():
    hand = Hand()
    assert hand.still_in_round == True

def test_hand_bet():
    hand = Hand()
    assert hand.bet == 10

def test_hand_cards():
    hand = Hand()
    assert hand.cards == {}
