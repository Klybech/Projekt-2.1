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


while taller==1:
    if taller==1:
        fibersm.udregnsm()
    elif taller==2:
        fibermm.udregnmm()
    elif taller==3:
        udgravningland.gravland()
    elif taller==4:
        udgravningby.gravby()
    elif taller == 5:
        print("Programmet afsluttes!!!")
    else:
        print("tastefejl, prøv igen!")
