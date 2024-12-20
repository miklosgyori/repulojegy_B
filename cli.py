import sys
from utils import letrehoz_foglalas, torol_foglalas

from foglalasirendszer import FoglalasiRendszer


def mutat_menu(foglalasi_rendszer: FoglalasiRendszer):
    """
    A menut irja ki.
    """
    print("\n")
    print("-" * 30)
    print("MENU")
    print("1) Jegy foglalasa (jaratok listazasaval): 1")
    print("2) Foglalas lemondasa: 2")
    print("3) Foglalasok listazasa: 3")
    print("X) Kilepes a programbol: X")
    print("-" * 30)
    valasz = input("Nyomd meg a valasztott billentyut, majd az ENTER-t!")
    if valasz == "1":
        foglal_jegyet(foglalasi_rendszer)
    elif valasz == "2":
        lemond_foglalast(foglalasi_rendszer)
    elif valasz == "3":
        listaz_foglalast(foglalasi_rendszer)
    elif valasz == "X":
        kilep()
    else:
        print("Ervenytelen valasztas. Valassz ervenyes lehetoseget")


def foglal_jegyet(foglalasi_rendszer: FoglalasiRendszer):
    print("\n*** Jegyfoglalas: ***")
    print("Listazom a jaratokat, legitarsasagok szerint:")
    for legitarsasag in foglalasi_rendszer.legitarsasagok:
        print(legitarsasag)
    jaratszam = int(input("Add meg a jarat szamat, amelyre foglalni akarsz, majd nyomj ENTER-t!"))
    utasnev = input("Add meg az utas nevet, majd nyomj ENTER-t!")
    letrehoz_foglalas(utasnev, jaratszam, foglalasi_rendszer)


def lemond_foglalast(foglalasi_rendszer: FoglalasiRendszer):
    print("\n*** Foglalas lemondasa: ***")
    print("Az ervenyes foglalasok:")
    for foglalas in foglalasi_rendszer.foglalasok:
        print(foglalas)
    torlendo = int(input("\nAdd meg a torlendo foglalas szamat, majd nyomj ENTER-t!"))
    torol_foglalas(torlendo, foglalasi_rendszer)

def listaz_foglalast(foglalasi_rendszer: FoglalasiRendszer):
    print("\n*** Foglalasok listazasa: ***\n")
    for foglalas in foglalasi_rendszer.foglalasok:
        print(foglalas)


def kilep():
    print("\n*** Kilepes: ***")
    valasz = input("Biztosan ki akarsz lépni? Akkor nyomd meg az \"I\" billentyut!")
    if valasz == "I":
        print("Kilepek.")
        sys.exit()
    else:
        print("Nem lepek ki.")
