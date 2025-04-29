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

    def test_calculateHand1(self): # standard hand with no aces
        result = self.deck.calculateHand([("7","H"),("J","S"),("4","D")])
        assert result == 21

    def test_calculateHand2(self): # hand with aces, should, ideally go to the highest possible score without busting i.e 13
        result = self.deck.calculateHand([("A","H"),("2","S"),("K","S")])
        assert result == 13

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
        
