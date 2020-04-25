import pygame
from Mängulaud import *
from värvid import *
pygame.init()


class seaded:

    def __init__(self, taustvärv, tekstivärv, lõpp, ristvring):
        self.taustvärv = taustvärv
        self.tekstivärv = tekstivärv
        self.lõpp = lõpp
        self.pikkus = 400
        self.laius = 400
        self.tagasi = False
        self.ristvring = ristvring

    def kasvahetada(self):
        if self.hiir_nupul() == "vaheta":
            print(1233)
            print(self.ristvring)
            if self.ristvring == "Alustab: O":
                self.ristvring = "Alustab: X"
            elif self.ristvring == "Alustab: X":
                self.ristvring = "Alustab: O"
        return self.ristvring

    def hiir_nupul(self):
        mitmes = None
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_y <= 100:
            if mouse_y >= 10 and mouse_y <= 30 and mouse_x >= 10 and mouse_x <= 30 and pygame.mouse.get_pressed()[0] == 1:
                # Mäng
                mitmes = "tagasi"
            if mouse_y >= 50 and mouse_y <= 110 and mouse_x >= 70 and mouse_x <= 340 and pygame.mouse.get_pressed()[0] == 1:
                # Seaded
                mitmes = "vaheta"
        return mitmes

    def run(self):
        display = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Seaded")
        display.fill(self.taustvärv)
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        pygame.draw.rect(display, must, (10, 10, 20, 20))

        pygame.draw.rect(display, must, (70, 50, 260, 60))
        pygame.font.init()

        smallerfont = pygame.font.SysFont('Times New Roman', 20)
        textsurface = smallerfont.render(("←"), False, valge)
        textRect = textsurface.get_rect()
        textRect.center = (20, 20)
        display.blit(textsurface, textRect)

        alustab_tekst = myfont.render((self.ristvring), False, punane)
        textRect = alustab_tekst.get_rect()
        textRect.center = (self.pikkus // 2, 80)
        display.blit(alustab_tekst, textRect)

        while self.lõpp == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lõpp = True
                    pygame.quit()
                if self.hiir_nupul() != None:
                    if self.hiir_nupul() == "tagasi":
                        self.tagasi = True
                        self.lõpp = True
                    if self.hiir_nupul() == "vaheta":
                        pygame.draw.rect(display, must, (70, 50, 260, 60))
                        self.kasvahetada()
                        alustab_tekst = myfont.render((self.ristvring), False, punane)
                        textRect = alustab_tekst.get_rect()
                        textRect.center = (self.pikkus // 2, 80)
                        display.blit(alustab_tekst, textRect)





            pygame.display.update()
    pygame.quit()
