import pygame
pygame.init()

class seaded:

    def __init__(self, taustvärv, tekstivärv, lõpp):
        self.taustvärv = taustvärv
        self.tekstivärv = tekstivärv
        self.lõpp = lõpp

    def display(self):
        display = pygame.display.set_mode((400, 400))
        return display

    def run(self):
        pygame.display.set_caption("Trips-traps-trull")
        self.display().fill(self.taustvärv)
        pygame.display.update()
        while self.lõpp == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lõpp = True

        pygame.display.update()

    pygame.quit()