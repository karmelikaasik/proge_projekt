import pygame
import time
pygame.init()
laius = 400
pikkus = 400
lõpp = False
display = pygame.display.set_mode((laius, pikkus))
pygame.display.set_caption("Trips-traps-trull")
hall = [128,128,128]
punane = [255,51,51]
must = [0,0,0]
sinine = [51,122,255]
kollane = [255,255,51]
roheline =[91,255, 51]
valge = [255,255,255]
gridforreference = [ [ 1,2,3],
                     [ 4,5,6],
                     [ 7,8,9 ] ]

grid = [ False,False,False,
         False,False,False,
         False,False,False ]

display.fill(hall)

def jooned():
    pygame.draw.line(display, punane, (150,50), (150,350), 5)
    pygame.draw.line(display, punane, (250, 50), (250, 350), 5)
    pygame.draw.line(display, punane, (50, 150), (350, 150), 5)
    pygame.draw.line(display, punane, (50, 250), (350, 250), 5)

def rist(ruut):
    if ruut != 0:
        x_koordinaat = int(50 + (((ruut + 2) % 3) * 100))
        y_koordinaat = int(50 + (((ruut - ruut % 3) / 3) * 100))
        if ruut%3 == 0:
            y_koordinaat = 50 + ((ruut/3)-1)*100
        pygame.draw.line(display, must, (x_koordinaat, y_koordinaat), (x_koordinaat+100, y_koordinaat+100), 5)
        pygame.draw.line(display, must, (x_koordinaat, y_koordinaat+100), (x_koordinaat+100, y_koordinaat),5)

def ring(ruut):
    if ruut != 0:
        x_koordinaat = int(50 + (((ruut + 2) % 3) * 100))
        y_koordinaat = int(50 + (((ruut - ruut % 3) / 3) * 100))
        if ruut%3 == 0:
            y_koordinaat = int(50 + ((ruut/3)-1)*100)
        keskpunkt = (x_koordinaat+50, y_koordinaat+50)
        raadius = 50
        pygame.draw.circle(display, must, keskpunkt, raadius, 3)

def hiire_asukoht():
    if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 350 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 350:
        mousex = pygame.mouse.get_pos()[0] - 50
        mousey = pygame.mouse.get_pos()[1] - 50
        xarv = (mousex - mousex%100)/100 + 1
        yarv = (mousey - mousey%100)/100
        ruut = int(yarv*3 + xarv)
        return ruut
    else:
        return 0

def ringvoirist(ringvrist, ruut):
    if ringvrist == "ring":
        ring(ruut)
        return "rist"
    elif ringvrist == "rist":
        rist(ruut)
        return "ring"

def m2ngl2bi(grid):
    mängläbi = False
    võitja = False
    viik = False
    põhjus = None
    if mängläbi == False:
        print("Mängläbi == False")
        viik = True
        for i in range(len(grid)):
            if grid[i] != False:
                if i%3==0 and grid[i] == grid[i+1] and grid[i] == grid[i+2]:
                    võitja = True
                    if i == 3:
                        i = 1
                    if i == 6:
                        i = 2
                    pygame.draw.line(display, kollane, (50,100+(100*i)), (350, 100+(100*i)),5)
                if i<3 and grid[i] == grid[i+3] and grid[i] == grid[i+6]:
                    võitja = True
                    pygame.draw.line(display, kollane, (100 + (100 * i),50), (100 + (100 * i),350), 5)
                if i == 4:
                    if grid[i] == grid[i-2] and grid[i] == grid[i+2]:
                        võitja = True
                        pygame.draw.line(display, kollane, (350,50), (50,350), 7)
                    if grid[i] == grid[i-4] and grid[i] == grid[i+4]:
                        võitja = True
                        pygame.draw.line(display, kollane, (50, 50), (350, 350), 7)
            elif grid[i] == False:
                viik = False
        if võitja == True:
            print("Võitja")
            mängläbi = True
            põhjus = "võitja"
        elif viik == True:
            print("viik")
            mängläbi = True
            põhjus = "viik"


    return mängläbi, põhjus

def mängu_lõpp():
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    if m2ngl2bi(grid)[1] == "võitja":
        if ringvrist == "rist":
            textsurface = myfont.render(("Võitja on "+ "ring"), False, must, valge)
        if ringvrist == "ring":
            textsurface = myfont.render(("Võitja on " + "rist"), False, must, valge)
    elif m2ngl2bi(grid)[1] == "viik":
        textsurface = myfont.render(("VIIK"), False, must, valge)
    else:
        textsurface = myfont.render(("bigerror"), False, punane, valge)
    textRect = textsurface.get_rect()
    textRect.center = (pikkus // 2, 50)
    display.blit(textsurface, textRect)

jooned()
ringvrist = "rist"
mängulõpp = False
while lõpp == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lõpp = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            ruut = hiire_asukoht()
            if grid[ruut-1] == False and mängulõpp == False:
                ringvoirist(ringvrist, hiire_asukoht())
                ringvrist = ringvoirist(ringvrist, hiire_asukoht())
                grid[ruut-1] = ringvrist
                if m2ngl2bi(grid)[0] == True:
                    mängulõpp = True
                    mängu_lõpp()



    pygame.display.update()


pygame.quit()