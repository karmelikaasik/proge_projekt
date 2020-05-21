from Mängulaud import *
from seaded import *
from värvid import *
import random

def peaaegu_rida(ruudustik, oma_märk):
    puudujääv = None
    if ruudustik[4] == oma_märk:
        for i in range(len(ruudustik)):
            if i == 4:
                pass
            else:
                if ruudustik[i] == oma_märk and ruudustik[8 - i] == False:
                    puudujääv = 8 - i
    elif ruudustik[4] == False:
        for i in range(len(ruudustik)):
            if i == 4:
                pass
            else:
                if ruudustik[i] == oma_märk and ruudustik[8 - i] == oma_märk:
                    puudujääv = 4
    else:
        if ruudustik[0] == oma_märk:
            if ruudustik[1] == oma_märk and ruudustik[2] == False:
                puudujääv == 2
            elif ruudustik[2] == oma_märk and ruudustik[1] == False:
                puudujääv == 1
            elif ruudustik[3] == oma_märk and ruudustik[6] == False:
                puudujääv == 6
            elif ruudustik[6] == oma_märk and ruudustik[3] == False:
                puudujääv == 3




def bot_easy(ruudustik, oma_märk):
    tühjad = []
    for i in ruudustik:
        if i == False:
            tühjad.append(i)
    return random.choice(tühjad)


def bot_medium(ruudustik, oma_märk):
    if peaaegu_rida(ruudustik, oma_märk) != None:
        return peaaegu_rida(ruudustik, oma_märk)
    else:
        return bot_easy(ruudustik, oma_märk)


def main(ruudustik, oma_märk, EvoiM):
    print("Ruudustik:")
    print(ruudustik)
    if EvoiM == "pvb (M)":
        return bot_medium(ruudustik, oma_märk)
    elif EvoiM == "pvb (E)":
        return bot_easy(ruudustik, oma_märk)