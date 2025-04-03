import pygame
import numpy as np
import GUI.Button as button
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

        self.__running = True


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
            beginGame.DecoButton("assets/cards/3x/c/CLUB-1@3x.png","assets/cards/3x/h/HEART-1@3x.png", self.beginGame)

            instructions = button.Button(self.screen, 0,50,(600,100),(230, 226, 110),"Instructions",self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            instructions.DecoButton("assets/cards/3x/c/CLUB-1@3x.png","assets/cards/3x/h/HEART-1@3x.png", self.instructions)

            quit = button.Button(self.screen, 0,250,(600,100),(230, 110, 110),"Quit",self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
            quit.DecoButton("assets/cards/3x/c/CLUB-1@3x.png","assets/cards/3x/h/HEART-1@3x.png",self.quit)

            pygame.display.flip()

            self.clock.tick(60)
        
        pygame.quit()


    def beginGame(self):
        print("begin")
        pass

    def instructions(self):
        print("instruc")
        pass

    def quit(self):
        print("quit")
        pass





