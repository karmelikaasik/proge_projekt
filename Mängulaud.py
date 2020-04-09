import pygame
pygame.init()


class Mängulaud():

    def __init__(self, laius, pikkus, taustvärv, gridvärv, ristvärv, ringvärv, joonevärv, grid, lõpp):
        self.laius = laius
        self.pikkus = pikkus
        self.taustvärv = taustvärv
        self.gridvärv = gridvärv
        self.ristvärv = ristvärv
        self.ringvärv = ringvärv
        self.joonevärv = joonevärv
        self.grid = grid
        self.lõpp = lõpp

    def mangulaud(self):
        display = pygame.display.set_mode((self.laius, self.pikkus))
        return display

    def jooned(self, display):
        a = display.fill(self.taustvärv)
        b = pygame.draw.line(display, self.gridvärv, (150,50), (150,350), 5)
        c = pygame.draw.line(display, self.gridvärv, (250, 50), (250, 350), 5)
        d = pygame.draw.line(display, self.gridvärv, (50, 150), (350, 150), 5)
        e = pygame.draw.line(display, self.gridvärv, (50, 250), (350, 250), 5)
        f = pygame.display.update()
        return a,b,c,d,e,f

    def rist(self, ruut, display):
        if ruut != 0:
            x_koordinaat = int(50 + (((ruut + 2) % 3) * 100))
            y_koordinaat = int(50 + (((ruut - ruut % 3) / 3) * 100))
            if ruut%3 == 0:
                y_koordinaat = 50 + ((ruut/3)-1)*100
            pygame.draw.line(display, self.ristvärv, (x_koordinaat, y_koordinaat), (x_koordinaat+100, y_koordinaat+100), 5)
            pygame.draw.line(display, self.ristvärv, (x_koordinaat, y_koordinaat+100), (x_koordinaat+100, y_koordinaat),5)

    def ring(self, ruut, display):
        if ruut != 0:
            x_koordinaat = int(50 + (((ruut + 2) % 3) * 100))
            y_koordinaat = int(50 + (((ruut - ruut % 3) / 3) * 100))
            if ruut%3 == 0:
                y_koordinaat = int(50 + ((ruut/3)-1)*100)
            keskpunkt = (x_koordinaat+50, y_koordinaat+50)
            raadius = 50
            pygame.draw.circle(display, self.ringvärv, keskpunkt, raadius, 3)

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

    def ringvoirist(self, ringvrist, ruut):
        if ringvrist == "ring":
            self.ring(ruut, self.mangulaud())
            return "rist"
        elif ringvrist == "rist":
            self.rist(ruut, self.mangulaud())
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

    def mängu_lõpp(self, ringvrist, display):
        must = [0,0,0]
        valge = [255,255,255]
        punane = [255,51,51]
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        if self.m2ngl2bi(self.grid, self.mangulaud())[1] == "võitja":
            if ringvrist == "rist":
                textsurface = myfont.render(("Võitja on "+ "ring"), False, must, valge)
            if ringvrist == "ring":
                textsurface = myfont.render(("Võitja on " + "rist"), False, must, valge)
        elif self.m2ngl2bi(self.grid, self.mangulaud())[1] == "viik":
            textsurface = myfont.render(("VIIK"), False, must, valge)
        else:
            textsurface = myfont.render(("bigerror"), False, punane, valge)
        textRect = textsurface.get_rect()
        textRect.center = (self.pikkus // 2, 50)
        display.blit(textsurface, textRect)

    def mäng(self):
        pygame.display.set_caption("Trips-traps-trull")
        self.jooned(self.mangulaud())
        ringvrist = "rist"
        mängulõpp = False
        pygame.display.update()
        while self.lõpp == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lõpp = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ruut = self.hiire_asukoht()
                    if self.grid[ruut-1] == False and mängulõpp == False:
                        pygame.display.flip()
                        self.ringvoirist(ringvrist, self.hiire_asukoht())
                        ringvrist = self.ringvoirist(ringvrist, self.hiire_asukoht())
                        self.grid[ruut-1] = ringvrist
                        if self.m2ngl2bi(self.grid, self.mangulaud())[0] == True:
                            mängulõpp = True
                            self.mängu_lõpp(ringvrist, self.mangulaud())



            pygame.display.update()


        pygame.quit()


hall = [128,128,128]
punane = [255,51,51]
must = [0,0,0]
sinine = [51,122,255]
kollane = [255,255,51]
roheline =[91,255, 51]
valge = [255,255,255]
