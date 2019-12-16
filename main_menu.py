import pygame
import time
pygame.init()
lõpp = False
laius = 400
pikkus = 400

hall = [128,128,128]
punane = [255,51,51]
must = [0,0,0]
sinine = [51,122,255]
kollane = [255,255,51]
roheline =[91,255, 51]
valge = [255,255,255]

display = pygame.display.set_mode((laius, pikkus))
pygame.display.set_caption("Peamenüü")

display.fill(hall)

pygame.draw.rect(display, must, (100,100,200, 80))
pygame.draw.rect(display, must, (100,200,200, 80))
pygame.draw.rect(display, must, (100,300,200, 80))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)
textsurface = myfont.render(("MÄNGI"), False, punane)
textRect = textsurface.get_rect()
textRect.center = (pikkus // 2, 140)
display.blit(textsurface, textRect)

textsurface1 = myfont.render(("SEADED"), False, punane)
textRect1 = textsurface1.get_rect()
textRect1.center = (pikkus // 2, 240)
display.blit(textsurface1, textRect1)

textsurface2 = myfont.render(("VÄLJU"), False, punane)
textRect2 = textsurface2.get_rect()
textRect2.center = (pikkus // 2, 340)
display.blit(textsurface2, textRect2)


def hiir_nupul():
    return None

while lõpp == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lõpp = True

    pygame.display.update()

pygame.quit()