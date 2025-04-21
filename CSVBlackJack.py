import csv
import random

class CSVBlackJack():
    def __init__(self, deckName):
        self.__deckName = deckName
        self.__result = "playerTurn"

    # Credit Jack J.
    def generateDeck(self):
        s = ['H', 'S', 'D', 'C']
        with open(self.__deckName, 'w', newline='') as csvfile:
            fieldnames = ['card value', 'suit']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
            for i in s:
                for j in range(1, 14):
                    if j == 1:
                        writer.writerow({'card value': "A", 'suit': i})
                    elif j == 11:
                        writer.writerow({'card value': "J", 'suit': i})
                    elif j == 12:
                        writer.writerow({'card value': "Q", 'suit': i})
                    elif j == 13:
                        writer.writerow({'card value': "K", 'suit': i})
                    else:
                        writer.writerow({'card value': j, 'suit': i})

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

    # Credit Andrew C.
    def shuffle(self):
        with open(self.__deckName, "r", newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader) #convert into a list, easier to work with in python

            random.shuffle(rows) #shuffle all rows

            with open(self.__deckName, "w", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerows(rows)

    # Calculates hand value totals; includes ace's 1/11 mechanic
    # Credit Andrew C.
    def calculateHand(self,hand):
        total = 0
        numAces = 0
        for card in hand:
            cardRank = card[0]
            if cardRank.isdigit() == True:
                cardValue = int(cardRank)
                total += cardValue
            elif cardRank == 'J' or cardRank == 'Q' or cardRank == 'K':
                cardValue = 10
                total += cardValue
            elif cardRank == 'A':
                cardValue = 11
                total += cardValue
                numAces += 1
    
        #This block changes an ace value from 11 to 1 if it prevents a bust
        while total > 21 and numAces != 0:
            total -= 10
            numAces -= 1
        
        return total
    
    def buildHands(self, playerHand, dealerHand):
        with open(self.__deckName,"r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            cards = list(reader)

            playerHand = []
            dealerHand = []
            count = 0
            while count < 2:
                self.hit(playerHand)
                self.hit(dealerHand)
                count += 1
        with open(self.__deckName, "w",newline="") as outfile: #deletes the 4 cards from the csv file
            writer = csv.writer(outfile)
            writer.writerows(cards)

        return playerHand, dealerHand

    def stand(self, playerHand, dealerHand):
        ptotal = self.calculateHand(playerHand) #calculate player hand total
        dtotal = self.calculateHand(dealerHand) #calculate dealer hand total
        while dtotal < 17:
            self.hit(dealerHand)
            dtotal = self.calculateHand(dealerHand)

        #credit to Andrew C.
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
    



