 #Robert Begley, Zack Rogols, Max Moeller, Grayson Crowell,Ben Pyle,
# Ashton Boland, Kevin Lesiak, Adam Schneir, Alex Jones, Jordan Chandler
import pygame
pygame.init()
font = pygame.font.SysFont("curlz", 45)
def credit(surf, dt):
    for i in range(1):
        surf.fill((0,0,0))
        credit1 = font.render("Robert Begley: The Lord", 1, (255,255,255))
        credit2 = font.render("Alex Jones: The One Man Army", 1, (255,255,255))
        credit3 = font.render("Ashton Boland: The Endless, The Ageless", 1, (255,255,255))
        credit4 = font.render("Adam Schneir: The Jesus", 1, (255,255,255))
        credit5 = font.render("Zack Rogols: That One Guy", 1, (255,255,255))
        credit6 = font.render("Max Moeller: The Walrus", 1, (255,255,255))
        credit7 = font.render("Grayson Crowell of The Amazing Hair", 1, (255,255,255))
        credit8 = font.render("The Artist Formally Known As Ben Pyle", 1, (255,255,255))
        credit9 = font.render("Kevin Lesiak: The Pretty Boy", 1, (255,255,255))
        credit10 = font.render("Jordan Chanler: The Music Maker", 1, (255,255,255))
        surf.blit(credit1,(20,0))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit2,(20,70))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit3,(20,140))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit4,(20,210))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit5,(20,280))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit6,(20,350))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit7,(20,420))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit8,(20,490))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit9,(20,560))
        pygame.display.update()
        pygame.time.delay(1500)
        surf.blit(credit10,(20,630))
        pygame.display.update()
        pygame.time.delay(4000)
        break

