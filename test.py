import unittest

from main import play_blackjack, score_hand


class TestBlackjackFunctions(unittest.TestCase):
    def test_demo(self): # test case from the assingment file
        deck = [c.strip() for c in "CA, D5, H9, HQ, S8".split(",")]
        players = ["sam"]
        dealer = "dealer"
        (winner, result) = play_blackjack(deck, players, dealer)
        # example
        self.assertEqual(winner, "sam")
        self.assertEqual(result["sam"], ["CA", "H9"])
        self.assertEqual(score_hand(result["sam"]), 20)
        self.assertEqual(result["dealer"], ["D5", "HQ", "S8"])
        self.assertEqual(score_hand(result["dealer"]), 23)


    def test_start_22(self):
        deck = [c.strip() for c in "CA, DA, HA, SA, S8".split(",")]
        players = ["sam"]
        dealer = "dealer"
        (winner, result) = play_blackjack(deck, players, dealer)
        
        self.assertEqual(winner, "dealer")
        self.assertEqual(result["sam"], ["CA", "HA"])
        self.assertEqual(score_hand(result["sam"]), 22)
        self.assertEqual(result["dealer"], ["DA", "SA"])
        self.assertEqual(score_hand(result["dealer"]), 22)
        

    def test_start_21(self):
        deck = [c.strip() for c in "CA, DK, HK, SA, S8".split(",")]
        players = ["sam"]
        dealer = "dealer"
        (winner, result) = play_blackjack(deck, players, dealer)
        
        self.assertEqual(winner, "sam")
        self.assertEqual(result["sam"], ["CA", "HK"])
        self.assertEqual(score_hand(result["sam"]), 21)
        self.assertEqual(result["dealer"], ["DK", "SA"])
        self.assertEqual(score_hand(result["dealer"]), 21)


    def test_run_out_of_cards(self):
        deck = [c.strip() for c in "CA".split(",")]
        players = ["sam"]
        dealer = "dealer"
        (winner, result) = play_blackjack(deck, players, dealer)
        
        self.assertEqual(winner, "sam") # sam still technically wins because he has more points
        self.assertEqual(result["sam"], ["CA"])
        self.assertEqual(score_hand(result["sam"]), 11)
        self.assertEqual(result["dealer"], [])
        self.assertEqual(score_hand(result["dealer"]), 0)


    def test_jokers_in_deck(self):
        # add a bunch of random junk into the deck
        deck = [c.strip() for c in "CA, FF, KZ, SS, QF, LL, D8".split(",")]
        players = ["sam"]
        dealer = "dealer"
        (winner, result) = play_blackjack(deck, players, dealer)

        self.assertEqual(winner, "sam") # sam still technically wins because he has more points
        self.assertEqual(result["sam"], ['CA', 'KZ', 'QF', 'LL', 'D8']) # sam draws a bunch of non-cards, but still gets to 18 and wins
        self.assertEqual(score_hand(result["sam"]), 19)
        self.assertEqual(result["dealer"], ['FF', 'SS'])
        self.assertEqual(score_hand(result["dealer"]), 0)


if __name__ == "__main__":
    unittest.main()