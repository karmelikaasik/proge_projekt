from Mängulaud import *
from seaded import *
from värvid import *
import random

def peaaegu_rida(ruudustik, oma_märk):
    puudujääv = None
    print(ruudustik)
    if ruudustik[4] == oma_märk:
        print("ruudustik[4] on oma märk")
        for i in range(len(ruudustik)):
            if i == 4:
                pass
            else:
                if ruudustik[i] == oma_märk and ruudustik[8 - i] == False:
                    puudujääv = 8 - i + 1
                    print("peaaegu rida, esimene. Puudujääv on " + str(puudujääv))
    if ruudustik[4] == False and puudujääv == None:
        for i in range(len(ruudustik)):
            if i == 4:
                pass
            else:
                if ruudustik[i] == oma_märk and ruudustik[8 - i] == oma_märk:
                    puudujääv = 5
                    print("i on " + str(i))
                    print("peaaegu rida, teine. Puudujääv on " + str(puudujääv))
    print("Algne puudujääv on " + str(puudujääv))
    if puudujääv == None:
        # Jah, seda prolly saab paremini teha. Ärme sellest räägi
        if ruudustik[0] == oma_märk:
            print("tere 0")
            print(ruudustik)
            if ruudustik[1] == oma_märk and ruudustik[2] == False:
                puudujääv = 3
            if ruudustik[2] == oma_märk and ruudustik[1] == False:
                puudujääv = 2
            if ruudustik[3] == oma_märk and ruudustik[6] == False:
                puudujääv = 7
            if ruudustik[6] == oma_märk and ruudustik[3] == False:
                puudujääv = 4

        if ruudustik[2] == oma_märk:
            print("tere 2")
            print(ruudustik)
            if ruudustik[1] == oma_märk and ruudustik[0] == False:
                puudujääv = 1
            if ruudustik[0] == oma_märk and ruudustik[1] == False:
                puudujääv = 2
            if ruudustik[5] == oma_märk and ruudustik[8] == False:
                puudujääv = 9
            if ruudustik[8] == oma_märk and ruudustik[5] == False:
                puudujääv = 6

        if ruudustik[6] == oma_märk:
            print("tere 6")
            print(ruudustik)
            if ruudustik[0] == oma_märk and ruudustik[3] == False:
                puudujääv = 4
            if ruudustik[3] == oma_märk and ruudustik[0] == False:
                puudujääv = 1
            if ruudustik[7] == oma_märk and ruudustik[8] == False:
                puudujääv = 9
            if ruudustik[8] == oma_märk and ruudustik[7] == False:
                puudujääv = 8

        if ruudustik[8] == oma_märk:
            print("tere 8")
            print(ruudustik)
            print("")
            print(ruudustik[2])
            print(ruudustik[3])
            print(ruudustik[4])
            if ruudustik[2] == oma_märk and ruudustik[5] == False:
                puudujääv = 6
            if ruudustik[5] == oma_märk and ruudustik[2] == False:
                puudujääv = 3
            if ruudustik[6] == oma_märk and ruudustik[7] == False:
                puudujääv = 8
            if ruudustik[7] == oma_märk and ruudustik[6] == False:
                puudujääv = 7

        print("peaaegu rida, kolmas. Puudujääv on " + str(puudujääv))
    print("Viimne puudujääv on " + str(puudujääv))
    return puudujääv




def bot_easy(ruudustik):
    tühjad = []
    for i in range(len(ruudustik)):
        if ruudustik[i] == False:
            tühjad.append(i)
    ruut = random.choice(tühjad) + 1
    return ruut


def bot_medium(ruudustik, oma_märk):
    if peaaegu_rida(ruudustik, oma_märk) != None:
        return peaaegu_rida(ruudustik, oma_märk)
    else:
        return bot_easy(ruudustik)


def main(ruudustik, oma_märk, EvoiM):
    if EvoiM == "pvb (M)":
        return bot_medium(ruudustik, oma_märk)
    elif EvoiM == "pvb (E)":
        return bot_easy(ruudustik)