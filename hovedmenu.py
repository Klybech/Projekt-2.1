https://github.com/Klybech/Projekt-2.1.git

import fibersm
import fibermm
import udgravningland
import udgravningby



def prmenu():
    print("1) Single Mode, MAX 50km ") #
    print("2) Multi Mode, MAX 2km ") #
    print("3) Kabel nedgravning 'Uden for byen'") #
    print("4) Kabel nedgravning 'I byen'")#
    print("5) Afslut program") # afslutter programmet
    print("")

prmenu()
taller=int(input())

while True:
    if taller==1:
        fibersm.udregnsm()
        prmenu()
        taller=int(input())
    if taller==2:
        fibermm.udregnmm()
        prmenu()
        taller=int(input())
    if taller==3:
        udgravningland.gravland()
        prmenu()
        taller=int(input())
    if taller==4:
        udgravningby.gravby()
        prmenu()
        taller=int(input())
    if taller == 5:
        print("Programmet afsluttes!!!")
        break
    else:
        print("tastefejl, prøv igen!")
        prmenu()
