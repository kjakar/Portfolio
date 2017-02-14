#Kevin Lesiak

import pygame

legs = pygame.image.load("..\\assets\\images\\Leg Shark.png")
smitty = pygame.image.load("..\\assets\\images\\smitty werbenjagermanjensen shark.png")
zombie = pygame.image.load("..\\assets\\images\\Zombie Shark.png")
under = pygame.image.load("..\\assets\\images\\Under Bite.png")
pirateShark = pygame.image.load("..\\assets\\images\\Pirate Shark.png")

class gameOver(object):

    def __init__(self):
        """uses the images and changes the font and text size"""
        self.image = pygame.image.load("..\\assets\\images\\sharkend.png")
        self.font = pygame.font.SysFont("Stencil", 45)
        self.hover = None

    def render(self,surf):
        surf.blit(self.image, (0,0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Write
        """Each color is for the individual text"""
        color1=(255,255,255)
        color2=(255,255,255)
        color3=(255,255,255)
        color4 =(255,255,255)
        color5 =(255,255,255)
        color6 =(255,255,255)
        """uses the update function to change the color of the text"""
        if self.hover == "1":
            color1=(255,255,0)
        elif self.hover == "2":
            color2 = (255,255,0)
        elif self.hover == "3":
            color3 = (255,255,0)
        elif self.hover == "4":
            color4 =(255,255,0)
        elif self.hover == "5":
            color5 = (255,255,0)
        elif self.hover == "6":
            color6 = (255,255,0)
        line1 = self.font.render("1st place : ", 1, color1)
        line2 = self.font.render("2nd place : ", 1, color2)
        line3 = self.font.render("3rd place : ", 1, color3)
        line4 = self.font.render("4th place : ", 1, color4)
        line5 = self.font.render("Retry?",  1, color5)
        line6 = self.font.render("Main Menu", 1, color6)
        surf.blit(line1,(200, 150))
        surf.blit(line2,(200,250))
        surf.blit(line3,(200,350))
        surf.blit(line4, (200,450))
        surf.blit(line5, (640 - int(line5.get_width() / 2), 550))
        surf.blit(line6, (640 - int(line6.get_width() / 2), 650))


    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.hover = None
        """finds the collisions of the test"""
        """if mouse[1] >= 150 and mouse[1] <= 185:
            self.hover = "1"
        if mouse[1] >= 250 and mouse[1] <= 285:
            self.hover = "2"
        if mouse[1] >= 350 and mouse[1] <= 385:
            self.hover = "3"
        if mouse[1] >= 450 and mouse[1] <= 485:
            self.hover = "4"""
        if mouse[1] >= 550 and mouse[1] <= 585:
            self.hover = "5"
        if mouse[1] >= 650 and mouse[1] <= 685:
            self.hover = "6"

class playerSelect(object):

    def __init__(self):
        """uses the images and changes the font and text size"""
        self.image = pygame.image.load("..\\assets\\images\\mainmenu.jpg")
        self.font = pygame.font.SysFont("Stencil", 45)
        self.hover = None

    def render(self,surf):
        surf.blit(self.image, (0,0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Write
        """Each color is for the individual text"""
        color1=(255,255,255)
        color2=(255,255,255)
        color3=(255,255,255)
        color4 =(255,255,255)
        color5 =(255,255,255)
        """uses the update function to change the color of the text"""
        if self.hover == "1":
            color1=(255,255,0)
        elif self.hover == "2":
            color2 = (255,255,0)
        elif self.hover == "3":
            color3 = (255,255,0)
        elif self.hover == "4":
            color4 =(255,255,0)
        elif self.hover == "5":
            color5 = (255,255,0)
        single = self.font.render("Smitty WerbenJagermanJensen Shark", 1, color1)
        multi = self.font.render("Legs Shark", 1, color2)
        options = self.font.render("Zombie Shark", 1, color3)
        credit = self.font.render("Under Bite Shark",  1, color4)
        pirate = self.font.render("Pirate Shark", 1, color5)
        title = self.font.render("Choose Your Shark!", 1, (164, 0, 0))
        surf.blit(single,(300, 150))
        surf.blit(multi,(300,250))
        surf.blit(options,(300,350))
        surf.blit(credit, (300,450))
        surf.blit(pirate, (300,550))
        surf.blit(title, (640 - int(title.get_width() / 2), 50))
        #shark sprites
        smitty.set_colorkey((188,71,154))
        surf.blit(smitty, (100, 150))

        legs.set_colorkey((188,71,154))
        surf.blit(legs, (100, 250))

        zombie.set_colorkey((188,71,154))
        surf.blit(zombie, (100, 350))

        under.set_colorkey((188,71,154))
        surf.blit(under, (100, 450))

        pirateShark.set_colorkey((188,71,154))
        surf.blit(pirateShark, (100, 550))

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.hover = None
        """finds the collisions of the test"""
        if mouse[1] >= 150 and mouse[1] <= 185:
            self.hover = "1"
        if mouse[1] >= 250 and mouse[1] <= 285:
            self.hover = "2"
        if mouse[1] >= 350 and mouse[1] <= 385:
            self.hover = "3"
        if mouse[1] >= 450 and mouse[1] <= 485:
            self.hover = "4"
        if mouse[1] >= 550 and mouse[1] <= 585:
            self.hover = "5"

class MainMenu:
    def __init__(self):
        """uses the images and changes the font and text size"""
        self.image = pygame.image.load("..\\assets\\images\\mainmenu.png")
        self.font = pygame.font.SysFont("Stencil", 45)
        self.hover = None


    def render(self,surf):
        surf.blit(self.image, (0,0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Write
        """Each color is for the individual text"""
        color1=(255,255,255)
        color2=(255,255,255)
        color3=(255,255,255)
        color4 =(255,255,255)
        """uses the update function to change the color of the text"""
        if self.hover == "Single":
            color1=(255,255,0)
        elif self.hover == "Multi":
            color2 = (255,255,0)
        elif self.hover == "Options":
            color3 = (255,255,0)
        elif self.hover == "Credits":
            color4 =(255,255,0)
        single = self.font.render("Single", 1, color1)
        multi = self.font.render("Multiplayer", 1,color2)
        options = self.font.render("Options", 1,color3)
        credit = self.font.render("Credits",  1,color4)
        surf.blit(single,(200, 350))
        surf.blit(multi,(200,450))
        surf.blit(options,(200,550))
        surf.blit(credit, (200,650))

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.hover = None
        """finds the collisions of the test"""

        if mouse[0] >= 200 and mouse[0] <= 350:
            if mouse[1] >= 350 and mouse[1] <= 383:
                self.hover = "Single"
        if mouse[0] >= 200 and mouse[0] <= 500:
            if mouse[1] >= 452 and mouse[1] <= 485:
                self.hover = "Multi"
        if mouse[0] >= 200 and mouse[0] <= 387:
            if mouse[1] >= 554 and mouse[1] <= 584:
                self.hover = "Options"
        if mouse[0] >= 200 and mouse[0] <= 387:
            if mouse[1] >= 650 and mouse[1] <= 685:
                self.hover = 'Credits'
