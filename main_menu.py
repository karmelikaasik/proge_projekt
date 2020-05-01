import pygame
import time
from Mängulaud import *
from seaded import *
from värvid import *
pygame.init()
laius = 400
pikkus = 400

def runmain(märk, taustavärv, nupuvärv):
    display = pygame.display.set_mode((laius, pikkus))
    pygame.display.set_caption("Peamenüü")

    display.fill(taustavärv)

    pygame.draw.rect(display, must, (100,200,200, 80))
    pygame.draw.rect(display, must, (100,300,200, 80))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 40)

    mängu_rect = pygame.draw.rect(display, must, (100, 100, 200, 80))
    textsurface = myfont.render(("MÄNGI"), False, valge)
    textRect = textsurface.get_rect()
    textRect.center = (pikkus // 2, 140)
    display.blit(textsurface, textRect)

    textsurface1 = myfont.render(("SEADED"), False, valge)
    textRect1 = textsurface1.get_rect()
    textRect1.center = (pikkus // 2, 240)
    display.blit(textsurface1, textRect1)

    textsurface2 = myfont.render(("VÄLJU"), False, valge)
    textRect2 = textsurface2.get_rect()
    textRect2.center = (pikkus // 2, 340)
    display.blit(textsurface2, textRect2)


    def hiir_nupul():
        mitmes = None
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_x >=100 and mouse_x <= 300:
            if mouse_y >= 100 and mouse_y <= 180 and pygame.mouse.get_pressed()[0]==1:
                #Mäng
                mitmes = "mängi"
            if mouse_y >= 200 and mouse_y <= 280 and pygame.mouse.get_pressed()[0]==1:
                #Seaded
                mitmes = "seaded"
            if mouse_y >= 300 and mouse_y <= 380 and pygame.mouse.get_pressed()[0]==1:
                #Välju
                mitmes = "välju"
        return mitmes


    lõpp = False
    b = seaded(taustavärv, nupuvärv, False, märk, "pvp")
    menüü = True
    a = Mängulaud(400, 400, punane, valge, valge, valge, [False, False, False,
                                                          False, False, False,
                                                          False, False, False], False, False)

    while lõpp == False:
        for event in pygame.event.get():
            pygame.display.update()
            if mängu_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(display, must, (100, 100, 200, 80))
                textsurface = myfont.render(("PVP"), False, valge)
                textRect = textsurface.get_rect()
                textRect.center = (pikkus // 2, 140)
                display.blit(textsurface, textRect)
            else:
                pygame.draw.rect(display, must, (100, 100, 200, 80))
                textsurface = myfont.render(("MÄNGI"), False, valge)
                textRect = textsurface.get_rect()
                textRect.center = (pikkus // 2, 140)
                display.blit(textsurface, textRect)
            if menüü == True:
                if event.type == pygame.QUIT:
                    lõpp = True
                if hiir_nupul() == "välju":
                    lõpp = True
                if hiir_nupul() == "seaded":
                    menüü = False
                    b.run()
                if hiir_nupul() == "mängi":
                    menüü = False
                    if b.ristvring == "Alustab: O":
                        a.mäng("ring", b.taustvärv, b.nupuvärv)
                    elif b.ristvring == "Alustab: X":
                        a.mäng("rist", b.taustvärv, b.nupuvärv)

        if b.tagasi == True:
            runmain(b.ristvring, b.taustvärv, b.nupuvärv)
            b.tagasi = False
            menüü = True
            pygame.display.update()
        if a.tagasi == True:
            runmain(b.ristvring, b.taustvärv, b.nupuvärv)
            a.tagasi = False
            menüü = True
            pygame.display.update()

    pygame.quit()

runmain("Alustab: X", hall, valge)
