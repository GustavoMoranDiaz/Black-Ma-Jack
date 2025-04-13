import pygame
import numpy as np
import GUI.Button as button
import os
import random
import blackjackFuncs
import data_gen
import csv
import CSVBlackJack

class GUI:
    """ALWAYS RUN CONSTRUCTOR FIRST,

    Class contains:

    MainMenu()

    BeginGame()

    Instructions()

    Quit()
    """    
    def __init__(self):
        """initializes core pygame variables
        """        
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720

        pygame.init() # initializes all pygame modules, required for everything else

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        
        if pygame.font:
            self.font = pygame.font.Font("assets/fonts/KGPerfectPenmanship.ttf",60)
        
        self.cardIndex = {
            ("A", "H"): "assets/cards/3x/h/HEART-1@3x.png",
            ("2", "H"): "assets/cards/3x/h/HEART-2@3x.png",
            ("3", "H"): "assets/cards/3x/h/HEART-3@3x.png",
            ("4", "H"): "assets/cards/3x/h/HEART-4@3x.png",
            ("5", "H"): "assets/cards/3x/h/HEART-5@3x.png",
            ("6", "H"): "assets/cards/3x/h/HEART-6@3x.png",
            ("7", "H"): "assets/cards/3x/h/HEART-7@3x.png",
            ("8", "H"): "assets/cards/3x/h/HEART-8@3x.png",
            ("9", "H"): "assets/cards/3x/h/HEART-9@3x.png",
            ("10", "H"): "assets/cards/3x/h/HEART-10@3x.png",
            ("J", "H"): "assets/cards/3x/h/HEART-11-JACK@3x.png",
            ("Q", "H"): "assets/cards/3x/h/HEART-12-QUEEN@3x.png",
            ("K", "H"): "assets/cards/3x/h/HEART-13-KING@3x.png",
            ("A", "D"): "assets/cards/3x/d/DIAMOND-1@3x.png",
            ("2", "D"): "assets/cards/3x/d/DIAMOND-2@3x.png",
            ("3", "D"): "assets/cards/3x/d/DIAMOND-3@3x.png",
            ("4", "D"): "assets/cards/3x/d/DIAMOND-4@3x.png",
            ("5", "D"): "assets/cards/3x/d/DIAMOND-5@3x.png",
            ("6", "D"): "assets/cards/3x/d/DIAMOND-6@3x.png",
            ("7", "D"): "assets/cards/3x/d/DIAMOND-7@3x.png",
            ("8", "D"): "assets/cards/3x/d/DIAMOND-8@3x.png",
            ("9", "D"): "assets/cards/3x/d/DIAMOND-9@3x.png",
            ("10", "D"): "assets/cards/3x/d/DIAMOND-10@3x.png",
            ("J", "D"): "assets/cards/3x/d/DIAMOND-11-JACK@3x.png",
            ("Q", "D"): "assets/cards/3x/d/DIAMOND-12-QUEEN@3x.png",
            ("K", "D"): "assets/cards/3x/d/DIAMOND-13-KING@3x.png",
            ("A", "C"): "assets/cards/3x/c/CLUB-1@3x.png",
            ("2", "C"): "assets/cards/3x/c/CLUB-2@3x.png",
            ("3", "C"): "assets/cards/3x/c/CLUB-3@3x.png",
            ("4", "C"): "assets/cards/3x/c/CLUB-4@3x.png",
            ("5", "C"): "assets/cards/3x/c/CLUB-5@3x.png",
            ("6", "C"): "assets/cards/3x/c/CLUB-6@3x.png",
            ("7", "C"): "assets/cards/3x/c/CLUB-7@3x.png",
            ("8", "C"): "assets/cards/3x/c/CLUB-8@3x.png",
            ("9", "C"): "assets/cards/3x/c/CLUB-9@3x.png",
            ("10", "C"): "assets/cards/3x/c/CLUB-10@3x.png",
            ("J", "C"): "assets/cards/3x/c/CLUB-11-JACK@3x.png",
            ("Q", "C"): "assets/cards/3x/c/CLUB-12-QUEEN@3x.png",
            ("K", "C"): "assets/cards/3x/c/CLUB-13-KING@3x.png",
            ("A", "S"): "assets/cards/3x/s/SPADE-1@3x.png",
            ("2", "S"): "assets/cards/3x/s/SPADE-2@3x.png",
            ("3", "S"): "assets/cards/3x/s/SPADE-3@3x.png",
            ("4", "S"): "assets/cards/3x/s/SPADE-4@3x.png",
            ("5", "S"): "assets/cards/3x/s/SPADE-5@3x.png",
            ("6", "S"): "assets/cards/3x/s/SPADE-6@3x.png",
            ("7", "S"): "assets/cards/3x/s/SPADE-7@3x.png",
            ("8", "S"): "assets/cards/3x/s/SPADE-8@3x.png",
            ("9", "S"): "assets/cards/3x/s/SPADE-9@3x.png",
            ("10", "S"): "assets/cards/3x/s/SPADE-10@3x.png",
            ("J", "S"): "assets/cards/3x/s/SPADE-11-JACK@3x.png",
            ("Q", "S"): "assets/cards/3x/s/SPADE-12-QUEEN@3x.png",
            ("K", "S"): "assets/cards/3x/s/SPADE-13-KING@3x.png",
            }

        self.__running = True


    def breakOut(self): # function used to break out of loops
        self.stay = False

    def mainMenu(self): 
        """Running this function will open the main menu, this should always be run on startup
        """

        pygame.display.set_caption("Black-Ma-Jack") # edits the little title of a window
        while self.__running: #begin a loop depending on the private running var
            self.events = pygame.event.get()
            for event in self.events: # checks event queue
                if event.type == pygame.QUIT: # if user presses the x on the window exit program
                    self.__running = False # exits while loop

            self.screen.fill((24, 64, 18))

            title = button.Button(self.screen, 0,-280,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            title.TextButton("Black-Ma-Jack",(600,100),(220,225,220),60)

            beginGame = button.Button(self.screen, 0,-150,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            beginGame.DecoButton("Begin Game",(600,100),(110, 224, 230), self.cardIndex[("A","C")],self.cardIndex[("A","H")],self.events, self.beginGame)

            instructions = button.Button(self.screen, 0,50,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            instructions.DecoButton("Instructions",(600,100),(230, 226, 110), self.cardIndex[("A","C")],self.cardIndex[("A","H")],self.events, self.instructions)

            quit = button.Button(self.screen, 0,250,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            quit.DecoButton("Quit",(600,100),(230, 110, 110), self.cardIndex[("A","C")],self.cardIndex[("A","H")],self.events, self.quit)

            pygame.display.flip() # prints everything to the screen, nice

            self.clock.tick(60)
        pygame.quit()

    def beginGame(self):
        deckName = "cardN.csv"
        pygame.display.set_caption("Black-Ma-Jack") # edits the little title of a window
        self.stay = True
        data_gen.generateDeck()
        blackjackFuncs.shuffle(deckName)
        csvBJ = CSVBlackJack.CSVBlackJack(deckName)
        # very important note, cards =! hand, hand is the tuples that represent the game state, cards are used to draw the cards on screen
        self.playerHand, self.dealerHand, = blackjackFuncs.buildHands(deckName) #creates both hands
        self.dealerCards = [] 
        self.playerCards = []

        while self.__running == True:
            self.events = pygame.event.get()
            for event in self.events: # checks event queue
                if event.type == pygame.QUIT: # if user presses the x on the window exit program
                    self.__running = False # exits while loop
            if self.stay == False:
                break

            if blackjackFuncs.calculateHand(self.playerHand) > 21: #detect if player has busted, if so, dont draw anything else, just the loss message
                self.screen.fill((24, 64, 18))
                self.bust = button.Button(self.screen,0,0,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
                self.bust.TextButton("PLAYER BUST, YOU LOSE",(700,300),(250,10,10),40)
            else:

                self.screen.fill((24, 64, 18))
                
                self.hit = button.Button(self.screen,400,280,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
                self.hit.DecoButton("Hit",(300,100),(255,255,255),self.cardIndex[("A","C")],self.cardIndex[("A","S")],self.events, lambda: csvBJ.hit(self.playerHand))

                self.stand = button.Button(self.screen,400,80,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
                self.stand.DecoButton("Stand",(300,100),(255,255,255),self.cardIndex[("A","C")],self.cardIndex[("A","S")],self.events, blackjackFuncs.stand)

                self.playerScore = button.Button(self.screen,0,50,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
                self.playerScore.TextButton(f"Your Score is currently: {blackjackFuncs.calculateHand(self.playerHand)}", (400,100),(255,255,255),20)

                self.dealerScore = button.Button(self.screen,0,-50,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
                self.dealerScore.TextButton(f"Dealer's Score is currently: {blackjackFuncs.calculateHand(self.dealerHand)}", (400,100),(255,255,255),20)

                
                self.playerCards = []

                for i in range(len(self.playerHand)):
                    self.playerCards.append(button.Button(self.screen,60-(i*(120)),250,self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
                    self.playerCards[i].CardButton(self.cardIndex[self.playerHand[i]])
                
                self.dealerCards = [] 

                for i in range(len(self.dealerHand)):
                    self.dealerCards.append(button.Button(self.screen,60-i*(120),-250,self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
                    self.dealerCards[i].CardButton(self.cardIndex[self.dealerHand[i]])

            pygame.display.flip() # prints everything to the screen, nice

            self.clock.tick(60)
    
    def instructions(self):
        pygame.display.set_caption("Black-Ma-Jack") # edits the little title of a window
        self.stay = True
        while self.__running == True:
            for event in pygame.event.get(): # checks event queue
                if event.type == pygame.QUIT: # if user presses the x on the window exit program
                    self.__running = False # exits while loop
            if self.stay == False:
                break
                
            self.screen.fill((24, 64, 18))
            
            self.howToPlay = button.Button(self.screen, 0, -300, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
            self.howToPlay.TextButton("How to Play Black-Ma-Jack",(400, 60),(255, 255, 255), 20)

            self.returnToMenu = button.Button(self.screen,250,280,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            self.returnToMenu.DecoButton("Return to Menu",(600,100),(255,255,255), self.cardIndex[("A","C")],self.cardIndex[("A","S")], self.breakOut)

            
            pygame.display.flip() # prints everything to the screen, nice

            self.clock.tick(60)

    def quit(self):
        self.__running = False





