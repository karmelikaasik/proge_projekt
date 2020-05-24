import pygame
import time
from Mängulaud import *
from seaded import *
from värvid import *
pygame.init()
laius = 400
pikkus = 400

def runmain(märk, taustavärv, nupuvärv, kesmängib):
    display = pygame.display.set_mode((laius, pikkus))
    pygame.display.set_caption("Peamenüü")

    display.fill(taustavärv)

    # Drawing boxes
    pygame.draw.rect(display, button, (100,200,200, 80))
    pygame.draw.rect(display, button, (100,300,200, 80))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 40)

    mängu_rect = pygame.draw.rect(display, button, (100, 100, 200, 80))
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

    # Hoverimine
    def hiir_nupul():
        hover = None
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_x >=100 and mouse_x <= 300:
            if mouse_y >= 100 and mouse_y <= 180:
                #Mäng
                hover = "mängi"
            if mouse_y >= 200 and mouse_y <= 280:
                #Seaded
                hover = "seaded"
            if mouse_y >= 300 and mouse_y <= 380:
                #Välju
                hover = "välju"
        return hover

    # Klikkimine
    def klikk_nupul():
        mitmes = None
        if pygame.mouse.get_pressed()[0] == 1:
            mitmes = hiir_nupul()
        return mitmes

    # Seadete  ja mängulaua objektid
    lõpp = False
    b = seaded(taustavärv, nupuvärv, False, märk, kesmängib)
    menüü = True
    a = Mängulaud(400, 400, punane, valge, valge, valge, [False, False, False,
                                                          False, False, False,
                                                          False, False, False], False, False)

    while lõpp == False:
        for event in pygame.event.get():
            pygame.display.update()
            # Hoverides tumedamaks
            if mängu_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(display, tumedamvärv(button), (100, 100, 200, 80))
                textsurface = myfont.render((b.kesmängib), False, valge)
                textRect = textsurface.get_rect()
                textRect.center = (pikkus // 2, 140)
                display.blit(textsurface, textRect)
            else:
                pygame.draw.rect(display, button, (100, 100, 200, 80))
                textsurface = myfont.render(("MÄNGI"), False, valge)
                textRect = textsurface.get_rect()
                textRect.center = (pikkus // 2, 140)
                display.blit(textsurface, textRect)

            # Hoverides tumedamaks ning kui klikk, siis mine
            if menüü == True:
                if event.type == pygame.QUIT:
                    lõpp = True
                if hiir_nupul() == "välju":
                    if klikk_nupul() == "välju":
                        lõpp = True
                if klikk_nupul() == "seaded":
                    menüü = False
                    b.run()
                if klikk_nupul() == "mängi":
                    menüü = False
                    if b.ristvring == "Alustab: O":
                        a.mäng("ring", b.taustvärv, b.nupuvärv, b.kesmängib)
                    elif b.ristvring == "Alustab: X":
                        a.mäng("rist", b.taustvärv, b.nupuvärv, b.kesmängib)

        # Menüü = False, if necessary
        if b.tagasi == True:
            runmain(b.ristvring, b.taustvärv, b.nupuvärv, b.kesmängib)
            b.tagasi = False
            menüü = True
            pygame.display.update()
        if a.tagasi == True:
            runmain(b.ristvring, b.taustvärv, b.nupuvärv, b.kesmängib)
            a.tagasi = False
            menüü = True
            pygame.display.update()

    pygame.quit()

runmain("Alustab: X", hall, valge, "pvp")