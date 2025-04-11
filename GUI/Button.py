import pygame
import numpy as np

class Button:
    def __init__(self,screen,XShift,YShift,buttonColor,SCREEN_WIDTH,SCREEN_HEIGHT):
        """creates a button object which can be turned into a variety of kinds of buttons (some of these arent actual buttons just kinda didnt wanna make 1 billion classes)

            DecoButton: Cool looking button with two cards next to the button, card can change depending on if user is hovering or not
            TextButton: Draws a rectangle of buttonColor color and draws text on top of it

        Args:
            screen (surface): pass in screen object
            XShift (int): integer to shift X position of button
            YShift (int): integer to shift Y position of button
            buttonColor (tuple): (Red,Green,Blue)
            buttonText (string): text to display on button
            SCREEN_WIDTH (int): Pass global screen width var
            SCREEN_HEIGHT (int): Pass global screen height var
        """        
        self.screen = screen
        self.buttonXShift = XShift
        self.buttonYShift = YShift
        self.buttonColor = buttonColor
        self.font = pygame.font.Font("assets/fonts/KGPerfectPenmanship.ttf",60)
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def DecoButton(self, buttonText, buttonSize, cardFilePath, hoverCardFilePath, mouseUpAction):
        """Generates a decorative button with two swaying cards on either side which runs mouseUpAction on mouseup (click)

        Args:
            buttonSize (tuple of ints): (button height,button width)
            cardFilePath (str): File path of card that appears when mouse isnt hovering button
            hoverCardFilePath (str): File path of the card that appears when mouse is hovering button
            mouseUpAction (function): Function you want to run after clicking button
        """
        
        self.buttonSurface = pygame.Surface(buttonSize)
        self.buttonRect = self.buttonSurface.get_rect(center=(self.SCREEN_WIDTH/2 + self.buttonXShift,(self.SCREEN_HEIGHT/2)+self.buttonYShift))        
        if self.buttonRect.collidepoint(pygame.mouse.get_pos()): #check to see if mouse is hovering the button
            self.buttonSurface = pygame.transform.smoothscale(self.buttonSurface, ((buttonSize[0]*1.1,buttonSize[1]*1.1))) #make the button bigger if youre hovering it to indicate it is selected
            self.buttonRect = self.buttonSurface.get_rect(center=(self.SCREEN_WIDTH/2 +self.buttonXShift,(self.SCREEN_HEIGHT/2)+self.buttonYShift)) #move button into position
            self.buttonSurface.fill(self.buttonColor) #color the button
            self.buttonTextSurface = self.font.render(buttonText, True, (10, 10, 10)) #create surface for the text on the button
            self.buttonTextRect = self.buttonTextSurface.get_rect(center=(self.SCREEN_WIDTH/2 + self.buttonXShift,(self.SCREEN_HEIGHT/2)+self.buttonYShift)) # move the text into position

            self.screen.blit(self.buttonSurface, self.buttonRect) # paste button onto screen
            self.screen.blit(self.buttonTextSurface, self.buttonTextRect) # paste text onto screen
            # start of Code for decorative rotating cards
            self.buttonDecoSurface = pygame.image.load(hoverCardFilePath).convert_alpha() #documentation states that using .convert() after loading a surface dramatically increases speed
            self.buttonDecoSurface = pygame.transform.rotozoom(self.buttonDecoSurface, 4*np.cos(pygame.time.get_ticks()/300),0.15)
            self.buttonDecoRect0 = self.buttonDecoSurface.get_rect(center=(self.buttonRect.left,self.SCREEN_HEIGHT/2 +self.buttonYShift))
            self.buttonDecoRect1 = self.buttonDecoSurface.get_rect(center=(self.buttonRect.right,self.SCREEN_HEIGHT/2 +self.buttonYShift))

            self.screen.blit(self.buttonDecoSurface,self.buttonDecoRect0)
            self.screen.blit(self.buttonDecoSurface,self.buttonDecoRect1)
            # end of Code for decorative rotating cards
            # start of code for click detection and "screen change"
            self.checkMouseUp = pygame.event.wait(15)
            if self.checkMouseUp.type == pygame.MOUSEBUTTONUP:
                mouseUpAction() 
            # end of code for click detection and "screen change"
        else:
            self.buttonSurface = pygame.transform.smoothscale(self.buttonSurface, ((buttonSize[0],buttonSize[1]))) # make the button the original size when not hovering
            self.buttonRect = self.buttonSurface.get_rect(center=(self.SCREEN_WIDTH/2 + self.buttonXShift,(self.SCREEN_HEIGHT/2)+self.buttonYShift)) #move button into position                self.buttonSurface.fill((133, 198, 255)) # color the button
            self.buttonTextSurface = self.font.render(buttonText, True, (10, 10, 10)) # create surface for the text on the button
            self.buttonTextRect = self.buttonTextSurface.get_rect(center=(self.SCREEN_WIDTH/2 + self.buttonXShift,(self.SCREEN_HEIGHT/2)+self.buttonYShift)) # move the text into position
            self.buttonSurface.fill(self.buttonColor) #color the button

            self.screen.blit(self.buttonSurface, self.buttonRect) # paste button onto screen
            self.screen.blit(self.buttonTextSurface, self.buttonTextRect) # paste text onto screen
            # start of Code for decorative static cards
            self.buttonDecoSurface = pygame.image.load(cardFilePath).convert_alpha() #documentation states that using .convert() after loading a surface dramatically increases speed
            self.buttonDecoSurface = pygame.transform.rotozoom(self.buttonDecoSurface, 0,0.15)
            self.buttonDecoRect0 = self.buttonDecoSurface.get_rect(center=(self.buttonRect.left,self.SCREEN_HEIGHT/2 +self.buttonYShift))
            self.buttonDecoRect1 = self.buttonDecoSurface.get_rect(center=(self.buttonRect.right,self.SCREEN_HEIGHT/2 +self.buttonYShift))

            self.screen.blit(self.buttonDecoSurface,self.buttonDecoRect0)
            self.screen.blit(self.buttonDecoSurface,self.buttonDecoRect1)

    def TextButton(self, buttonText, buttonSize, fontsize):
        self.buttonSurface = pygame.Surface(buttonSize)
        self.buttonRect = self.buttonSurface.get_rect(center=(self.SCREEN_WIDTH/2 + self.buttonXShift,(self.SCREEN_HEIGHT/2)+self.buttonYShift)) 
        self.font = pygame.font.Font("assets/fonts/KGPerfectPenmanship.ttf", fontsize)
        
        self.buttonRect = self.buttonSurface.get_rect(center=(self.SCREEN_WIDTH/2 + self.buttonXShift,(self.SCREEN_HEIGHT/2)+self.buttonYShift)) #move button into position 
        self.buttonSurface.fill(self.buttonColor) #color the button

        self.buttonTextSurface = self.font.render(buttonText, True, (10, 10, 10)) # create surface for the text on the button
        self.buttonTextRect = self.buttonTextSurface.get_rect(center=(self.SCREEN_WIDTH/2 + self.buttonXShift,(self.SCREEN_HEIGHT/2)+self.buttonYShift)) # move the text into position

        self.screen.blit(self.buttonSurface, self.buttonRect) # paste button onto screen
        self.screen.blit(self.buttonTextSurface, self.buttonTextRect) # paste text onto screen

    def CardButton(self, cardFilePath, scaleCoeff, angle = 0, flipped = False, mouseUpAction = lambda: None): 
        if flipped == False:
            self.cardSurface = pygame.image.load(cardFilePath).convert_alpha()
        else:
            self.cardSurface = pygame.image.load("assets/cards/3x/cardback@3x.png").convert_alpha()

        self.cardSurface = pygame.transform.rotozoom(self.cardSurface, angle, scaleCoeff)
        self.cardRect = self.cardSurface.get_rect(center=(self.SCREEN_WIDTH/2 +self.buttonXShift,self.SCREEN_HEIGHT/2 +self.buttonYShift))

        if self.cardRect.collidepoint(pygame.mouse.get_pos()): #check to see if mouse is hovering the button
            self.cardSurface = pygame.transform.rotozoom(self.cardSurface, 4*np.cos(pygame.time.get_ticks()/300), 1.15)
            self.cardRect = self.cardSurface.get_rect(center=(self.SCREEN_WIDTH/2 +self.buttonXShift,self.SCREEN_HEIGHT/2 +self.buttonYShift))
            self.screen.blit(self.cardSurface,self.cardRect)
            self.checkMouseUp = pygame.event.wait(15)
            if self.checkMouseUp.type == pygame.MOUSEBUTTONUP:
                # INSERT CODE TO OPEN THE GAME ONCE THATS DEVELOPED
                mouseUpAction() 
            # end of code for click detection and "screen change"
            
        else:
            self.cardSurface = pygame.transform.rotozoom(self.cardSurface, 0, 1)
            self.cardRect = self.cardSurface.get_rect(center=(self.SCREEN_WIDTH/2 +self.buttonXShift,self.SCREEN_HEIGHT/2 +self.buttonYShift))
            self.screen.blit(self.cardSurface,self.cardRect)
