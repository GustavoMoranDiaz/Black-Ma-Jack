import pygame
import numpy as np
import GUI.Button as button
import os
import random

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
        
        self.cardIndex = { # this just makes it easier to call the filepaths of the cards
            "HA" : "assets/cards/3x/h/HEART-1@3x.png",
            "H2" : "assets/cards/3x/h/HEART-2@3x.png",
            "H3" : "assets/cards/3x/h/HEART-3@3x.png",
            "H4" : "assets/cards/3x/h/HEART-4@3x.png",
            "H5" : "assets/cards/3x/h/HEART-5@3x.png",
            "H6" : "assets/cards/3x/h/HEART-6@3x.png",
            "H7" : "assets/cards/3x/h/HEART-7@3x.png", 
            "H8" : "assets/cards/3x/h/HEART-8@3x.png", 
            "H9" : "assets/cards/3x/h/HEART-9@3x.png", 
            "H10" : "assets/cards/3x/h/HEART-10@3x.png", 
            "HJ" : "assets/cards/3x/h/HEART-11-JACK@3x.png",
            "HQ" : "assets/cards/3x/h/HEART-12-QUEEN@3x.png", 
            "HK" : "assets/cards/3x/h/HEART-13-KING@3x.png",
            "DA" : "assets/cards/3x/d/DIAMOND-1@3x.png",
            "D2" : "assets/cards/3x/d/DIAMOND-2@3x.png",
            "D3" : "assets/cards/3x/d/DIAMOND-3@3x.png",
            "D4" : "assets/cards/3x/d/DIAMOND-4@3x.png",
            "D5" : "assets/cards/3x/d/DIAMOND-5@3x.png",
            "D6" : "assets/cards/3x/d/DIAMOND-6@3x.png",
            "D7" : "assets/cards/3x/d/DIAMOND-7@3x.png", 
            "D8" : "assets/cards/3x/d/DIAMOND-8@3x.png", 
            "D9" : "assets/cards/3x/d/DIAMOND-9@3x.png", 
            "D10" : "assets/cards/3x/d/DIAMOND-10@3x.png", 
            "DJ" : "assets/cards/3x/d/DIAMOND-11-JACK@3x.png",
            "DQ" : "assets/cards/3x/d/DIAMOND-12-QUEEN@3x.png", 
            "DK" : "assets/cards/3x/d/DIAMOND-13-KING@3x.png",
            "CA" : "assets/cards/3x/c/CLUB-1@3x.png",
            "C2" : "assets/cards/3x/c/CLUB-2@3x.png",
            "C3" : "assets/cards/3x/c/CLUB-3@3x.png",
            "C4" : "assets/cards/3x/c/CLUB-4@3x.png",
            "C5" : "assets/cards/3x/c/CLUB-5@3x.png",
            "C6" : "assets/cards/3x/c/CLUB-6@3x.png",
            "C7" : "assets/cards/3x/c/CLUB-7@3x.png", 
            "C8" : "assets/cards/3x/c/CLUB-8@3x.png", 
            "C9" : "assets/cards/3x/c/CLUB-9@3x.png", 
            "C10" : "assets/cards/3x/c/CLUB-10@3x.png", 
            "CJ" : "assets/cards/3x/c/CLUB-11-JACK@3x.png",
            "CQ" : "assets/cards/3x/c/CLUB-12-QUEEN@3x.png", 
            "CK" : "assets/cards/3x/c/CLUB-13-KING@3x.png",
            "SA" : "assets/cards/3x/s/SPADE-1@3x.png",
            "S2" : "assets/cards/3x/s/SPADE-2@3x.png",
            "S3" : "assets/cards/3x/s/SPADE-3@3x.png",
            "S4" : "assets/cards/3x/s/SPADE-4@3x.png",
            "S5" : "assets/cards/3x/s/SPADE-5@3x.png",
            "S6" : "assets/cards/3x/s/SPADE-6@3x.png",
            "S7" : "assets/cards/3x/s/SPADE-7@3x.png", 
            "S8" : "assets/cards/3x/s/SPADE-8@3x.png", 
            "S9" : "assets/cards/3x/s/SPADE-9@3x.png", 
            "S10" : "assets/cards/3x/s/SPADE-10@3x.png", 
            "SJ" : "assets/cards/3x/s/SPADE-11-JACK@3x.png",
            "SQ" : "assets/cards/3x/s/SPADE-12-QUEEN@3x.png", 
            "SK" : "assets/cards/3x/s/SPADE-13-KING@3x.png",
            }

        self.__running = True


    def breakOut(self): # function used to break out of loops
        self.stay = False

    def mainMenu(self): 
        """Running this function will open the main menu, this should always be run on startup
        """
        pygame.display.set_caption("Black-Ma-Jack") # edits the little title of a window
        while self.__running: #begin a loop depending on the private running var
            for event in pygame.event.get(): # checks event queue
                if event.type == pygame.QUIT: # if user presses the x on the window exit program
                    self.__running = False # exits while loop

            self.screen.fill((24, 64, 18))

            beginGame = button.Button(self.screen, 0,-150,(600,100),(110, 224, 230),"Begin Game",self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            beginGame.DecoButton(self.cardIndex["CA"],self.cardIndex["HA"], self.beginGame)

            instructions = button.Button(self.screen, 0,50,(600,100),(230, 226, 110),"Instructions",self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            instructions.DecoButton(self.cardIndex["SA"],self.cardIndex["DA"], self.instructions)

            quit = button.Button(self.screen, 0,250,(600,100),(230, 110, 110),"Quit",self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            quit.DecoButton(self.cardIndex["CA"],self.cardIndex["HA"],self.quit)

            pygame.display.flip() # prints everything to the screen, nice

            self.clock.tick(60)
        pygame.quit()

    def beginGame(self):
        print("begin")
        pass
    
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
            
            self.howToPlay = button.Button(self.screen, 0, -300, (400, 60), (255, 255, 255), "How to Play Black-Ma-Jack", self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
            self.howToPlay.TextButton(20)

            self.returnToMenu = button.Button(self.screen,250,280,(600,100),(255,255,255),"Return to Menu",self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            self.returnToMenu.DecoButton("assets/cards/3x/c/CLUB-1@3x.png","assets/cards/3x/h/HEART-1@3x.png", self.breakOut)

            
            pygame.display.flip() # prints everything to the screen, nice

            self.clock.tick(60)

        

    def quit(self):
        self.__running = False





