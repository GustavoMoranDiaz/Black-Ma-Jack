import pygame

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

        self.__running = True


    def mainMenu(self): 
        """Running this function will open the main menu, this should always be run on startup
        """
        pygame.display.set_caption("Black-Ma-Jack") # edits the little title of a window

        while self.__running: #begin a loop depending on the private running var
            for event in pygame.event.get(): # checks event queue
                if event.type == pygame.QUIT: # if user presses the x on the window exit program
                    self.__running = False # exits while loop
                
            self.screen.fill("black")

            pygame.display.flip()

            self.clock.tick(60)
        
        pygame.quit()


    def beginGame(self):
        pass

    def instructions(self):
        pass

    def quit(self):
        pass





