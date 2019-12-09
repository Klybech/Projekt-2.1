def gravby():


    Landsby = 300 #kr pr m
    Storby = 750 #kr pr m
    Underboring = 1000 #kr pr m

    taller=4

    print("")
    print("Du har valgt udgravning by")
    print("Udfyld felterne her under med værdier")
    print("")
    grav = int(input("Indtast antal meter landsby: "))
    strby = int(indput("Indtast antal meter storby"))
    ubor = int(input("Indtast antal meter underboring: "))

    landsby = grav*Landsby
    storby = strby*Storby
    underboring = ubor*Underboring

    print("")
    print("Prisen for nedgravning", nedgrav,"kr")
    print("Prisen for storby", storby,"kr")
    print("Prisen for underboring", underboring,"kr")
    print("")
