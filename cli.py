import sys


def mutat_menu():
    """
    A menut irja ki.
    """
    print("-" * 30)
    print("MENU")
    print("1) Jegy foglalasa: 1")
    print("2) Foglalas lemondasa: 2")
    print("3) Foglalasok listazasa: 3")
    print("X) Kilepes a programbol: X")
    print("-" * 30)
    valasz = input(" Nyomd meg a valasztott billentyut!")
    if valasz == "1":
        foglal_jegyet()
    elif valasz == "2":
        lemond_foglalast()
    elif valasz == "3":
        listaz_foglalast()
    elif valasz == "X":
        kilep()
    else:
        print("Ervenytelen valasztas. Valassz ervenyes lehetoseget")


def foglal_jegyet():
    print("Jegyfoglalas:")
    # TODO logika!!!


def lemond_foglalast():
    print("Foglalas lemondasa:")
    # TODO logika!!!


def listaz_foglalast():
    print("Foglalasok listazasa:")
    # TODO logika!!!


def kilep():
    valasz = input("Biztosan ki akarsz lépni? Akkor nyomd meg az \"I\" billentyut!")
    if valasz == "I":
        print("Kilepek.")
        sys.exit()
    else:
        print("Nem lepek ki.")
