import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.game = CardGame()
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Spades", 10)
        self.cards = [self.card1, self.card2]

    def test_check_for_aces(self):
        self.assertEquals(False, self.game.check_for_ace(self.card2))

    def test_checks_for_highest_card(self):
        self.assertEquals(self.card2, self.game.highest_card(self.card1,self.card2))

    def test_check_total_cards(self):
        self.assertEquals("You have a total of 11", self.game.cards_total(self.cards))

