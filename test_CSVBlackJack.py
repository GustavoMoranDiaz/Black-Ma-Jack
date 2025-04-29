import CSVBlackJack as cbj
import pytest
import csv

class TestCSVBlackJack:
    
    def setup_method(self): #setup just has to create the object of the CSVBlackJack Class
        print("setting up a new test deck...")
        self.deck = cbj.CSVBlackJack("testDeck.csv")

    def teardown_method(self):
        print("deleting test deck...")
        del self.deck

    #--test of generateDeck Method--
    def test_generateDeck(self):
        self.deck.generateDeck()
        with open("testDeck.csv") as csvfile:
            reader = csv.reader(csvfile)
            cards = list(reader)
        assert len(cards) == 52

    #--test of calculateHand Method--

    #test1 = 7 of hearts, jack of spades, 4 of diamonds should equal a score of 21
    #test2 = ace of hearts, 2 of spades, king of spades should equal a score of 13 to avoid busting

    @pytest.mark.parametrize("hand,expected",[([("7","H"),("J","S"),("4","D")],21),([("A","H"),("2","S"),("K","S")],13)])
    def test_calculateHand(self, hand, expected): # standard hand with no aces
        result = self.deck.calculateHand(hand)
        assert result == expected

    #--test of buildHands--

    def test_buildHands(self):
        with open("testDeck.csv") as csvfile: # save top 4 cards from the deck
            reader = csv.reader(csvfile)
            top4cards = list(reader)
            top4cards = top4cards[:4]

        hand1 = []
        hand2 = []
        hand1, hand2 = self.deck.buildHands(hand1,hand2) #create the hands

        assert list(hand1[0]) and list(hand1[1]) and list(hand2[0]) and list(hand2[1]) in top4cards # make sure that the hands are only composed of cards from the top 4 cards of the deck

    #--test of stand--
    
    #test1: playerhand = ace of hearts, king of diamonds | dealerhand = king of spades, 9 of clubs should result in a blackjack win for player i.e bjwin
    #test2: playerhand = ace of hearts, king of diamonds, 8 of diamonds | dealerhand = king of spades, 9 of clubs, equal score should result in a push

    @pytest.mark.parametrize("playerhand,dealerhand,expected", [([("A","H"),("K","D")],[("K","S"),("9","C")],"bjWin"),([("A","H"),("K","D"),("8","D")],[("K","S"),("9","C")],"push")])
    def test_stand(self,playerhand,dealerhand,expected):
        self.deck.stand(playerhand,dealerhand)
        result = self.deck.getResult()
        assert result == expected
