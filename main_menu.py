import pygame
import time
from Mängulaud import *
from seaded import *
pygame.init()
laius = 400
pikkus = 400

hall = [128,128,128]
punane = [255,51,51]
must = [0,0,0]
sinine = [51,122,255]
kollane = [255,255,51]
roheline =[91,255, 51]
valge = [255,255,255]

class main_menu():

    def __init__(self, laius, pikkus, taustvärv, gridvärv, ristvärv, ringvärv, joonevärv, grid):
        self.laius = laius
        self.pikkus = pikkus
        self.taustvärv = taustvärv
        self.gridvärv = gridvärv
        self.ristvärv = ristvärv
        self.ringvärv = ringvärv
        self.joonevärv = joonevärv
        self.grid = grid


    def hiir_nupul(self):
        mitmes = None
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_x >=100 and mouse_x <= 300:
            if mouse_y >= 100 and mouse_y <= 180 and pygame.mouse.get_pressed()[0]==1:
                #Mäng
                mitmes = "esimene"
            if mouse_y >= 200 and mouse_y <= 280 and pygame.mouse.get_pressed()[0]==1:
                #Seaded
                mitmes = "teine"
            if mouse_y >= 300 and mouse_y <= 380 and pygame.mouse.get_pressed()[0]==1:
                #Välju
                mitmes = "kolmas"
        return mitmes

    def menüü(self):
        display = pygame.display.set_mode((self.laius, self.pikkus))
        pygame.display.set_caption("Peamenüü")

        display.fill(hall)

        pygame.draw.rect(display, must, (100, 100, 200, 80))
        pygame.draw.rect(display, must, (100, 200, 200, 80))
        pygame.draw.rect(display, must, (100, 300, 200, 80))
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
        lõpp = False
        while lõpp == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    lõpp = True
                if self.hiir_nupul() == "kolmas":
                    lõpp = True
                if self.hiir_nupul() == "teine":
                    b = seaded(valge,must, False)
                    b.run()
                if self.hiir_nupul() == "esimene":
                    a = Mängulaud(self.laius, self.pikkus, self.taustvärv, self.gridvärv, self.ristvärv, self.ringvärv, self.joonevärv, [False, False, False,
                                                                                                                                        False, False, False,
                                                                                                                                        False, False, False], False)
                    a.mäng()

            pygame.display.update()

        pygame.quit()

main = main_menu(400,400,hall,punane,must,must,valge,[False, False, False,
                                                      False, False, False,
                                                      False, False, False])
main.menüü()