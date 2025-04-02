import pygame
import numpy as np
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

        self.font = pygame.font.Font("assets/fonts/KGPerfectPenmanship.ttf",60)
        #initialization of "Start Game Button"
        self.beginGameSurface = pygame.Surface((600,100))
        self.beginGameRect = self.beginGameSurface.get_rect(center=(self.SCREEN_WIDTH/2,(self.SCREEN_HEIGHT/2)-100))

        self.beginGameText = self.font.render("Begin Game", True, (10, 10, 10))
        self.beginGameTextRect = self.beginGameText.get_rect(center=(self.SCREEN_WIDTH/2,(self.SCREEN_HEIGHT/2)-100))
        #end of initialization of "Start Game Button"

        pygame.display.set_caption("Black-Ma-Jack") # edits the little title of a window
        while self.__running: #begin a loop depending on the private running var
            for event in pygame.event.get(): # checks event queue
                if event.type == pygame.QUIT: # if user presses the x on the window exit program
                    self.__running = False # exits while loop
            
            # Start of code for the "Start Game Button"
            self.screen.fill("black")
            if pygame.mouse.get_pos()[0] in range(self.beginGameRect.left,self.beginGameRect.right) and pygame.mouse.get_pos()[1] in range(self.beginGameRect.top,self.beginGameRect.bottom): #check to see if mouse is hovering the button
                self.beginGameSurface = pygame.transform.smoothscale(self.beginGameSurface, ((600*1.1,100*1.1))) #make the button bigger if youre hovering it to indicate it is selected
                self.beginGameRect = self.beginGameSurface.get_rect(center=(self.SCREEN_WIDTH/2,(self.SCREEN_HEIGHT/2)-100)) #move button into position
                self.beginGameSurface.fill((133, 198, 255)) #color the button
                self.beginGameText = self.font.render("Begin Game", True, (10, 10, 10)) #create surface for the text on the button
                self.beginGameTextRect = self.beginGameText.get_rect(center=(self.SCREEN_WIDTH/2,(self.SCREEN_HEIGHT/2)-100)) # move the text into position

                self.screen.blit(self.beginGameSurface, self.beginGameRect) # paste button onto screen
                self.screen.blit(self.beginGameText, self.beginGameTextRect) # paste text onto screen
                # start of Code for decorative rotating cards
                self.beginGameDecoSurf = pygame.image.load("assets/cards/3x/c/CLUB-1@3x.png").convert() #documentation states that using .convert() after loading a surface dramatically increases speed
                self.beginGameDecoSurf = pygame.transform.rotozoom(self.beginGameDecoSurf, 4*np.cos(pygame.time.get_ticks()/300),0.15)
                self.beginGameDecoRect0 = self.beginGameDecoSurf.get_rect(center=(self.beginGameRect.left,self.SCREEN_HEIGHT/2 - 100))
                self.beginGameDecoRect1 = self.beginGameDecoSurf.get_rect(center=(self.beginGameRect.right,self.SCREEN_HEIGHT/2 - 100))

                self.screen.blit(self.beginGameDecoSurf,self.beginGameDecoRect0)
                self.screen.blit(self.beginGameDecoSurf,self.beginGameDecoRect1)
                # end of Code for decorative rotating cards
                # start of code for click detection and "screen change"
                self.checkMouseUp = pygame.event.wait(15)
                if self.checkMouseUp.type == pygame.MOUSEBUTTONUP:
                    # INSERT CODE TO OPEN THE GAME ONCE THATS DEVELOPED
                    self.__running = False # delete this once you get the actual code for the game
                # end of code for click detection and "screen change"
            else:
                self.beginGameSurface = pygame.transform.smoothscale(self.beginGameSurface, ((600,100))) # make the button the original size when not hovering
                self.beginGameRect = self.beginGameSurface.get_rect(center=(self.SCREEN_WIDTH/2,(self.SCREEN_HEIGHT/2)-100)) #move button into position
                self.beginGameSurface.fill((133, 198, 255)) # color the button
                self.beginGameText = self.font.render("Begin Game", True, (10, 10, 10)) # create surface for the text on the button
                self.beginGameTextRect = self.beginGameText.get_rect(center=(self.SCREEN_WIDTH/2,(self.SCREEN_HEIGHT/2)-100)) # move the text into position

                self.screen.blit(self.beginGameSurface, self.beginGameRect) # paste button onto screen
                self.screen.blit(self.beginGameText, self.beginGameTextRect) # paste text onto screen
                # start of Code for decorative static cards
                self.beginGameDecoSurf = pygame.image.load("assets/cards/3x/c/CLUB-1@3x.png").convert() #documentation states that using .convert() after loading a surface dramatically increases speed
                self.beginGameDecoSurf = pygame.transform.rotozoom(self.beginGameDecoSurf, 0,0.15)
                self.beginGameDecoRect0 = self.beginGameDecoSurf.get_rect(center=(self.beginGameRect.left,self.SCREEN_HEIGHT/2 - 100))
                self.beginGameDecoRect1 = self.beginGameDecoSurf.get_rect(center=(self.beginGameRect.right,self.SCREEN_HEIGHT/2 - 100))

                self.screen.blit(self.beginGameDecoSurf,self.beginGameDecoRect0)
                self.screen.blit(self.beginGameDecoSurf,self.beginGameDecoRect1)
                # end of Code for decorative static cards
            pygame.display.flip()

            self.clock.tick(60)
        
        pygame.quit()


    def beginGame(self):
        pass

    def instructions(self):
        pass

    def quit(self):
        pass





