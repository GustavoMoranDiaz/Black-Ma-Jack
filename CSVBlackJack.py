import csv
import blackjackFuncs

class CSVBlackJack():
    def __init__(self, deckName):
        self.__deckName = deckName
        self.__result = "playerTurn"

    def popAndAdd(self,hand):
        """deletes 1 card from the top of the csv deck, then appends that card onto hand

        Args:
            hand (list of tuples): list of tuples representing the hand to be added to
        """        
        with open(self.__deckName,"r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            cards = list(reader)
            hand.append(tuple(cards.pop(0)))
            with open(self.__deckName, "w",newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerows(cards)

    def getResult(self):
        return(self.__result)

    def hit(self, Hand):
        self.popAndAdd(Hand)

    def stand(self, playerHand, dealerHand):
        ptotal = blackjackFuncs.calculateHand(playerHand) #calculate player hand total
        dtotal = blackjackFuncs.calculateHand(dealerHand) #calculate dealer hand total
        while dtotal < 17:
            self.hit(dealerHand)
            dtotal = blackjackFuncs.calculateHand(dealerHand)

        if dtotal > 21:
            self.__result = "dBust"
        elif ptotal == 21 and dtotal != 21:
            self.__result = "bjWin"
        elif dtotal > ptotal:
            self.__result = "scoreLoss"
        elif ptotal > dtotal:
            self.__result = "scoreWin"
        elif ptotal == 21 and dtotal == 21:
            self.__result = "bjPush"
        elif ptotal == dtotal:
            self.__result = "push"
    



