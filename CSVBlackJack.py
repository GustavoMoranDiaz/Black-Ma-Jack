import csv
import blackjackFuncs

class CSVBlackJack():
    def __init__(self, deckName):
        self.__deckName = deckName
        self.__playerTurn = True

    def popAndAdd(self,hand):
        """deletes 1 card from the top of the csv deck, then appends that card onto hand

        Args:
            hand (list of tuples): list of tuples representing the hand to be added to
        """        
        with open(self.__deckName,"r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            cards = list(reader)
            hand.append(cards.pop(0))
            with open(self.__deckName, "w",newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerows(cards)

    def hit(self, playerHand):
        self.popAndAdd(playerHand)
        ptotal = blackjackFuncs.calculateHand(playerHand)
        if ptotal > 21:
            pass

