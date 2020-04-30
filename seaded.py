import pygame
from värvid import *

pygame.init()


class seaded:

    def __init__(self, taustvärv, nupuvärv, lõpp, ristvring, kesmängib):
        self.taustvärv = taustvärv
        self.nupuvärv = nupuvärv
        self.lõpp = lõpp
        self.tekstivärv = valge
        self.pikkus = 400
        self.laius = 400
        self.tagasi = False
        self.ristvring = ristvring
        self.kesmängib = kesmängib

    def setRistvring(self, argument):
        self.ristvring = argument

    def setKesmängib(self, argument):
        self.kesmängib = argument

    def ristvõiring(self):
        if self.hiir_nupul() == "vaheta_nupp":
            if self.ristvring == "Alustab: O":
                self.setRistvring("Alustab: X")
            elif self.ristvring == "Alustab: X":
                self.setRistvring("Alustab: O")
        return self.ristvring

    def hiir_nupul(self):
        mitmes = None
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_y >= 10 and mouse_y <= 30 and mouse_x >= 10 and mouse_x <= 30 and pygame.mouse.get_pressed()[0] == 1:
            mitmes = "tagasi"
        if mouse_y >= 40 and mouse_y <= 100 and mouse_x >= 60 and mouse_x <= 350 and pygame.mouse.get_pressed()[0] == 1:
            mitmes = "vaheta_nupp"
        if mouse_y >= 125 and mouse_y <= 185 and mouse_x >= 60 and mouse_x <= 350 and pygame.mouse.get_pressed()[0] == 1:
            mitmes = "vaheta_taust"
        if mouse_y >= 210 and mouse_y <= 270 and mouse_x >= 60 and mouse_x <= 350 and pygame.mouse.get_pressed()[0] == 1:
            mitmes = "vaheta_nupuvärv"
        if mouse_y >= 295 and mouse_y <= 355 and mouse_x >= 60 and mouse_x <= 350 and pygame.mouse.get_pressed()[0] == 1:
            mitmes = "vaheta_mänguviis"

        return mitmes

    def kesmängivad(self):
        if self.kesmängib == "pvp":
            self.setKesmängib("pvb")
        elif self.kesmängib == "pvb":
            self.setKesmängib("pvp")
        return self.kesmängib

    def muudataustavärvi(self, värv):
        värvid = ["hall", "punane", "must", "sinine", "kollane", "roheline", "valge"]
        if värvid.index(värv) != 6:
            self.converttagurpidi(värvid[värvid.index(värv)+1],self.tekstivärv)
            return värvid[värvid.index(värv)+1]
        else:
            self.converttagurpidi(värvid[0], self.tekstivärv)
            return värvid[0]

    def muudanupuvärvi(self,värv):
        värvid = ["hall", "punane", "must", "sinine", "kollane", "roheline", "valge"]
        if värvid.index(värv) != 6:
            self.converttagurpidi(self.taustvärv,värvid[värvid.index(värv) + 1])
            return värvid[värvid.index(värv) + 1]
        else:
            self.converttagurpidi(self.taustvärv, värvid[0])
            return värvid[0]

    def converttovärv(self):
        if self.taustvärv == [128,128,128]:
            tvärv = "hall"
        elif self.taustvärv == [255,51,51]:
            tvärv = "punane"
        elif self.taustvärv == [51,122,255]:
            tvärv = "sinine"
        elif self.taustvärv == [255,255,51]:
            tvärv = "kollane"
        elif self.taustvärv == [0,0,0]:
            tvärv = "must"
        elif self.taustvärv == [91,255, 51]:
            tvärv = "roheline"
        elif self.taustvärv == [255, 255, 255]:
            tvärv = "valge"

        if self.nupuvärv == [128,128,128]:
            nvärv = "hall"
        elif self.nupuvärv == [255,51,51]:
            nvärv = "punane"
        elif self.nupuvärv == [51,122,255]:
            nvärv = "sinine"
        elif self.nupuvärv == [255,255,51]:
            nvärv = "kollane"
        elif self.nupuvärv == [0,0,0]:
            nvärv = "must"
        elif self.nupuvärv == [91,255, 51]:
            nvärv = "roheline"
        elif self.nupuvärv == [255, 255, 255]:
            nvärv = "valge"

        return tvärv, nvärv

    def converttagurpidi(self,tvärv, nvärv):
        if tvärv == "must":
            self.taustvärv = must
        if tvärv == "valge":
            self.taustvärv = valge
        if tvärv == "sinine":
            self.taustvärv = sinine
        if tvärv == "roheline":
            self.taustvärv = roheline
        if tvärv == "punane":
            self.taustvärv = punane
        if tvärv == "hall":
            self.taustvärv = hall
        if tvärv == "kollane":
            self.taustvärv = kollane

        if nvärv == "must":
            self.nupuvärv = must
        if nvärv == "valge":
            self.nupuvärv = valge
        if nvärv == "sinine":
            self.nupuvärv = sinine
        if nvärv == "roheline":
            self.nupuvärv = roheline
        if nvärv == "punane":
            self.nupuvärv = punane
        if nvärv == "hall":
            self.nupuvärv = hall
        if nvärv == "kollane":
            self.nupuvärv = kollane


    def run(self):
        display = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Seaded")
        display.fill(self.taustvärv)
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        pygame.draw.rect(display, must, (10, 10, 20, 20))

        pygame.draw.rect(display, must, (60, 40, 280, 60))
        pygame.font.init()

        smallerfont = pygame.font.SysFont('Times New Roman', 20)
        textsurface = smallerfont.render(("←"), False, valge)
        textRect = textsurface.get_rect()
        textRect.center = (20, 20)
        display.blit(textsurface, textRect)

        alustab_tekst = myfont.render((self.ristvring), False, self.tekstivärv)
        textRect = alustab_tekst.get_rect()
        textRect.center = (self.pikkus // 2, 70)
        display.blit(alustab_tekst, textRect)

        pygame.draw.rect(display, must, (60, 125, 280, 60))
        tekst = myfont.render("Taust: "+ self.converttovärv()[0], False, self.tekstivärv)
        textRect = tekst.get_rect()
        textRect.center = (self.pikkus // 2, 155)
        display.blit(tekst, textRect)

        pygame.draw.rect(display, must, (60, 210, 280, 60))
        tekst = myfont.render("Nupp: " + self.converttovärv()[1], False, self.tekstivärv)
        textRect = tekst.get_rect()
        textRect.center = (self.pikkus // 2, 237)
        display.blit(tekst, textRect)

        pygame.draw.rect(display, must, (60, 295, 280, 60))
        tekst = myfont.render("Mäng: " + self.kesmängib, False, self.tekstivärv)
        textRect = tekst.get_rect()
        textRect.center = (self.pikkus // 2, 320)
        display.blit(tekst, textRect)


        while self.lõpp == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lõpp = True
                    pygame.quit()
                if self.hiir_nupul() != None:
                    if self.hiir_nupul() == "tagasi":
                        self.tagasi = True
                        self.lõpp = True
                    if self.hiir_nupul() == "vaheta_nupp":
                        pygame.draw.rect(display, must, (60, 40, 280, 60))
                        self.ristvõiring()
                        alustab_tekst = myfont.render((self.ristvring), False, self.tekstivärv)
                        textRect = alustab_tekst.get_rect()
                        textRect.center = (self.pikkus // 2, 70)
                        display.blit(alustab_tekst, textRect)
                    if self.hiir_nupul() == "vaheta_taust":
                        pygame.draw.rect(display, must, (60, 125, 280, 60))
                        tekst = myfont.render("Taust: "+ self.muudataustavärvi(self.converttovärv()[0]), False, self.tekstivärv)
                        textRect = tekst.get_rect()
                        textRect.center = (self.pikkus // 2, 155)
                        display.blit(tekst, textRect)
                    if self.hiir_nupul() == "vaheta_nupuvärv":
                        pygame.draw.rect(display, must, (60, 210, 280, 60))
                        tekst = myfont.render("Nupp: " + self.muudanupuvärvi(self.converttovärv()[1]), False, self.tekstivärv)
                        textRect = tekst.get_rect()
                        textRect.center = (self.pikkus // 2, 237)
                        display.blit(tekst, textRect)
                    if self.hiir_nupul() == "vaheta_mänguviis":
                        pygame.draw.rect(display, must, (60, 295, 280, 60))
                        tekst = myfont.render("Mäng: " + self.kesmängivad(), False, self.tekstivärv)
                        textRect = tekst.get_rect()
                        textRect.center = (self.pikkus // 2, 320)
                        display.blit(tekst, textRect)

            pygame.display.update()
    pygame.quit()
