import pygame
pygame.init()
from värvid import *
from bot import *
import time

class Mängulaud():

    def __init__(self, laius, pikkus, gridvärv, ristvärv, ringvärv, joonevärv, grid, tagasi, lõpp):
        self.laius = laius
        self.pikkus = pikkus
        self.ristvärv = ristvärv
        self.ringvärv = ringvärv
        self.gridvärv = gridvärv
        self.joonevärv = joonevärv
        self.grid = grid
        self.tagasi = tagasi
        self.lõpp = lõpp

    def setGrid(self, grid):
        self.grid = grid

    def rist(self, ruut, display, nupuvärv):
        if ruut != 0:
            x_koordinaat = int(50 + (((ruut + 2) % 3) * 100))
            y_koordinaat = int(50 + (((ruut - ruut % 3) / 3) * 100))
            if ruut%3 == 0:
                y_koordinaat = 50 + ((ruut/3)-1)*100
            pygame.draw.line(display, nupuvärv, (x_koordinaat, y_koordinaat), (x_koordinaat+100, y_koordinaat+100), 5)
            pygame.draw.line(display, nupuvärv, (x_koordinaat, y_koordinaat+100), (x_koordinaat+100, y_koordinaat),5)

    def ring(self, ruut, display, nupuvärv):
        if ruut != 0:
            x_koordinaat = int(50 + (((ruut + 2) % 3) * 100))
            y_koordinaat = int(50 + (((ruut - ruut % 3) / 3) * 100))
            if ruut%3 == 0:
                y_koordinaat = int(50 + ((ruut/3)-1)*100)
            keskpunkt = (x_koordinaat+50, y_koordinaat+50)
            raadius = 50
            pygame.draw.circle(display, nupuvärv, keskpunkt, raadius, 3)

    def hiire_asukoht(self):
        if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 350 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 350:
            mousex = pygame.mouse.get_pos()[0] - 50
            mousey = pygame.mouse.get_pos()[1] - 50
            xarv = (mousex - mousex%100)/100 + 1
            yarv = (mousey - mousey%100)/100
            ruut = int(yarv*3 + xarv)
            return ruut
        else:
            return 0

    def ringvoirist(self, ringvrist, ruut, display, nupuvärv):
        if ringvrist == "ring":
            self.ring(ruut, display, nupuvärv)
            return "rist"
        elif ringvrist == "rist":
            self.rist(ruut, display, nupuvärv)
            return "ring"

    def m2ngl2bi(self, grid, display):
        mängläbi = False
        võitja = False
        viik = False
        põhjus = None
        if mängläbi == False:
            viik = True
            for i in range(len(grid)):
                if grid[i] != False:
                    if i%3==0 and grid[i] == grid[i+1] and grid[i] == grid[i+2]:
                        võitja = True
                        if i == 3:
                            i = 1
                        if i == 6:
                            i = 2
                        pygame.draw.line(display, self.joonevärv, (50,100+(100*i)), (350, 100+(100*i)),5)
                    if i<3 and grid[i] == grid[i+3] and grid[i] == grid[i+6]:
                        võitja = True
                        pygame.draw.line(display, self.joonevärv, (100 + (100 * i),50), (100 + (100 * i),350), 5)
                    if i == 4:
                        if grid[i] == grid[i-2] and grid[i] == grid[i+2]:
                            võitja = True
                            pygame.draw.line(display, self.joonevärv, (350,50), (50,350), 7)
                        if grid[i] == grid[i-4] and grid[i] == grid[i+4]:
                            võitja = True
                            pygame.draw.line(display, self.joonevärv, (50, 50), (350, 350), 7)
                elif grid[i] == False:
                    viik = False
            if võitja == True:
                mängläbi = True
                põhjus = "võitja"
            elif viik == True:
                mängläbi = True
                põhjus = "viik"

        return mängläbi, põhjus

    def klikk_nupul(self):
        mitmes = None
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_x >= 100 and mouse_x <= 300:
            if mouse_y >= 100 and mouse_y <= 150 and pygame.mouse.get_pressed()[0] == 1:
                mitmes = "uusmäng"
            if mouse_y >= 160 and mouse_y <= 210 and pygame.mouse.get_pressed()[0] == 1:
                mitmes = "menüü"
            if mouse_y >= 220 and mouse_y <= 270 and pygame.mouse.get_pressed()[0] == 1:
                mitmes = "välju"
        return mitmes

    def kas_uuesti_vms(self, display):
        pygame.draw.rect(display, button, (100, 100, 200, 50))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(("UUS MÄNG"), False, valge)
        textRect = textsurface.get_rect()
        textRect.center = (self.pikkus // 2, 120)
        display.blit(textsurface, textRect)
        textsurface = myfont.render("MENÜÜ", False, valge)
        textRect = pygame.draw.rect(display, button, (100, 160, 200, 50))
        textRect.center = (self.pikkus // 2, 180)
        display.blit(textsurface, textRect)
        textsurface = myfont.render("VÄLJU", False, valge)
        textRect = pygame.draw.rect(display, button, (100, 220, 200, 50))
        textRect.center = (self.pikkus // 2, 240)
        display.blit(textsurface, textRect)

    def mängu_lõpp(self, ringvrist, display):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        if self.m2ngl2bi(self.grid, display)[1] == "võitja":
            if ringvrist == "rist":
                textsurface = myfont.render(("Võitja on "+ "ring"), False, valge, must)
            if ringvrist == "ring":
                textsurface = myfont.render(("Võitja on " + "rist"), False, valge, must)
        elif self.m2ngl2bi(self.grid, display)[1] == "viik":
            textsurface = myfont.render(("VIIK"), False, valge, must)
        else:
            textsurface = myfont.render(("bigerror"), False, punane, valge)
        textRect = textsurface.get_rect()
        textRect.center = (self.pikkus // 2, 50)
        display.blit(textsurface, textRect)

    def mäng(self, märk, taustavärv, nupuvärv, kesmängib):
        if märk == "rist":
            eimärk = "ring"
        else:
            eimärk = "rist"
        #print(self.tagasi)
        pygame.display.set_caption("Trips-traps-trull")
        display = pygame.display.set_mode((self.laius, self.pikkus))
        display.fill(taustavärv)
        pygame.draw.line(display, self.gridvärv, (150,50), (150,350), 5)
        pygame.draw.line(display, self.gridvärv, (250, 50), (250, 350), 5)
        pygame.draw.line(display, self.gridvärv, (50, 150), (350, 150), 5)
        pygame.draw.line(display, self.gridvärv, (50, 250), (350, 250), 5)
        ringvrist = märk
        mängulõpp = False
        pygame.display.update()
        while self.lõpp == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lõpp = True
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ruut = self.hiire_asukoht()

                    if self.klikk_nupul() == "uusmäng" and mängulõpp == True:
                        self.setGrid([False, False, False,
                                      False, False, False,
                                      False, False, False])
                        self.mäng(märk, taustavärv, nupuvärv, kesmängib)
                        mängulõpp = False
                        self.tagasi = False
                        self.lõpp = False

                    elif self.klikk_nupul() == "välju" and mängulõpp == True:
                        self.tagasi = False
                        self.lõpp = True
                        mängulõpp = False
                        pygame.quit()

                    elif self.klikk_nupul() == "menüü" and mängulõpp == True:
                        self.tagasi = True
                        self.lõpp = True
                        mängulõpp = False

                    elif self.grid[ruut-1] == False and mängulõpp == False:
                        pygame.display.update()
                        self.ringvoirist(ringvrist, ruut, display, nupuvärv)
                        ringvrist = self.ringvoirist(ringvrist, ruut, display, nupuvärv)

                        self.grid[ruut-1] = ringvrist
                        if self.m2ngl2bi(self.grid, display)[0] == True:
                            self.mängu_lõpp(ringvrist, display)
                            self.kas_uuesti_vms(display)
                            mängulõpp = True
                        elif kesmängib != "pvp":
                            ruut = main(self.grid, eimärk, kesmängib)
                            print(ruut)
                            pygame.display.update()
                            self.ringvoirist(ringvrist, ruut, display, nupuvärv)
                            ringvrist = self.ringvoirist(ringvrist, ruut, display, nupuvärv)

                            self.grid[ruut] = ringvrist
                            if self.m2ngl2bi(self.grid, display)[0] == True:
                                self.mängu_lõpp(ringvrist, display)
                                self.kas_uuesti_vms(display)
                                mängulõpp = True



            pygame.display.update()

