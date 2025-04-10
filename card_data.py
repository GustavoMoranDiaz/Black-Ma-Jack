import csv
from GUI import GUI
import random
class card:
    def __init__(self, newV, newS):
        self.__cardV = newV
        self.__cardS = newS
    def getS(self):
        return self.__cardS
    def getV(self):
        return self.__cardV
s = ['H', 'S', 'D', 'C']
l = []
with open('cardN.csv', 'r', newline='') as csvfile:
    """fieldnames = ['card value', 'suit']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #for row in csvfile:
        
    for i in s:
        for j in range(1, 14):
            writer.writerow({'card value': j, 'suit': i})
            """
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        l.append(card(row[0], row[1]))
indexH =  { # this just makes it easier to call the filepaths of the cards
    "1" : "assets/cards/3x/h/HEART-1@3x.png",
    "2" : "assets/cards/3x/h/HEART-2@3x.png",
    "3" : "assets/cards/3x/h/HEART-3@3x.png",
    "4" : "assets/cards/3x/h/HEART-4@3x.png",
    "5" : "assets/cards/3x/h/HEART-5@3x.png",
    "6" : "assets/cards/3x/h/HEART-6@3x.png",
    "7" : "assets/cards/3x/h/HEART-7@3x.png", 
    "8" : "assets/cards/3x/h/HEART-8@3x.png", 
    "9" : "assets/cards/3x/h/HEART-9@3x.png", 
    "10" : "assets/cards/3x/h/HEART-10@3x.png", 
    "11" : "assets/cards/3x/h/HEART-11-JACK@3x.png",
    "12" : "assets/cards/3x/h/HEART-12-QUEEN@3x.png", 
    "13" : "assets/cards/3x/h/HEART-13-KING@3x.png"}
indexD = {"1" : "assets/cards/3x/d/DIAMOND-1@3x.png",
    "2" : "assets/cards/3x/d/DIAMOND-2@3x.png",
    "3" : "assets/cards/3x/d/DIAMOND-3@3x.png",
    "4" : "assets/cards/3x/d/DIAMOND-4@3x.png",
    "5" : "assets/cards/3x/d/DIAMOND-5@3x.png",
    "6" : "assets/cards/3x/d/DIAMOND-6@3x.png",
    "7" : "assets/cards/3x/d/DIAMOND-7@3x.png", 
    "8" : "assets/cards/3x/d/DIAMOND-8@3x.png", 
    "9" : "assets/cards/3x/d/DIAMOND-9@3x.png", 
    "10" : "assets/cards/3x/d/DIAMOND-10@3x.png", 
    "11" : "assets/cards/3x/d/DIAMOND-11-JACK@3x.png",
    "12" : "assets/cards/3x/d/DIAMOND-12-QUEEN@3x.png", 
    "13" : "assets/cards/3x/d/DIAMOND-13-KING@3x.png"}
indexS = {"1" : "assets/cards/3x/s/SPADE-1@3x.png",
    "2" : "assets/cards/3x/s/SPADE-2@3x.png",
    "3" : "assets/cards/3x/s/SPADE-3@3x.png",
    "4" : "assets/cards/3x/s/SPADE-4@3x.png",
    "5" : "assets/cards/3x/s/SPADE-5@3x.png",
    "6" : "assets/cards/3x/s/SPADE-6@3x.png",
    "7" : "assets/cards/3x/s/SPADE-7@3x.png", 
    "8" : "assets/cards/3x/s/SPADE-8@3x.png", 
    "9" : "assets/cards/3x/s/SPADE-9@3x.png", 
    "10" : "assets/cards/3x/s/SPADE-10@3x.png", 
    "11" : "assets/cards/3x/s/SPADE-11-JACK@3x.png",
    "12" : "assets/cards/3x/s/SPADE-12-QUEEN@3x.png", 
    "13" : "assets/cards/3x/s/SPADE-13-KING@3x.png"}
indexC = {"1" : "assets/cards/3x/c/CLUB-1@3x.png",
    "2" : "assets/cards/3x/c/CLUB-2@3x.png",
    "3" : "assets/cards/3x/c/CLUB-3@3x.png",
    "4" : "assets/cards/3x/c/CLUB-4@3x.png",
    "5" : "assets/cards/3x/c/CLUB-5@3x.png",
    "6" : "assets/cards/3x/c/CLUB-6@3x.png",
    "7" : "assets/cards/3x/c/CLUB-7@3x.png", 
    "8" : "assets/cards/3x/c/CLUB-8@3x.png", 
    "9" : "assets/cards/3x/c/CLUB-9@3x.png", 
    "10" : "assets/cards/3x/c/CLUB-10@3x.png", 
    "11" : "assets/cards/3x/c/CLUB-11-JACK@3x.png",
    "12" : "assets/cards/3x/c/CLUB-12-QUEEN@3x.png", 
    "13" : "assets/cards/3x/c/CLUB-13-KING@3x.png"}    
rng = len(l)
randomN = random.randint(0, rng)
print(randomN+1)
if l[randomN].getS() == 'H':
    val = l[randomN].getV()
    print(indexH[str(val)])
if l[randomN].getS() == 'C':
    val = l[randomN].getV()
    print(indexC[str(val)])
if l[randomN].getS() == 'S':
    val = l[randomN].getV()
    print(indexS[str(val)])
if l[randomN].getS() == 'D':
    val = l[randomN].getV()
    print(indexD[str(val)])
        
