from foglalasirendszer import FoglalasiRendszer
from legitarsasag import LegiTarsasag
from belfoldijarat import BelfoldiJarat
from nemzetkozijarat import NemzetkoziJarat
from jegyfoglalas import JegyFoglalas


def inicializal(foglalasi_rendszer: FoglalasiRendszer):

    airlinesone = LegiTarsasag("AirLinesOne")
    print(airlinesone)
    foglalasi_rendszer.legitarsasagok.append(airlinesone)

    letrehoz_belfoldijarat("AirLinesOne", "Budapest", "Debrecen", "2024-11-01 12:30:00", 100, 50000, foglalasi_rendszer)
    letrehoz_belfoldijarat("AirLinesOne", "Budapest", "Miskolctapolca", "2024-11-02 11:00:00", 10, 5000, foglalasi_rendszer)
    letrehoz_belfoldijarat("AirLinesOne", "Budapest", "Alsogod", "2024-11-04 14:00:00", 15, 30000, foglalasi_rendszer)
    letrehoz_nemzetkozijarat("AirLinesOne", "Budapest", "Trieste", "2024-11-03 13:00:00", 150, 150000, foglalasi_rendszer)

    print("\nLegitarsasagok lista tartalma:")
    for legitarsasag in foglalasi_rendszer.legitarsasagok:
        print(legitarsasag)

    letrehoz_foglalas("Utas Egy", 1, foglalasi_rendszer)
    letrehoz_foglalas("Utas Ketto", 1, foglalasi_rendszer)
    letrehoz_foglalas("Utas Harom", 2, foglalasi_rendszer)
    letrehoz_foglalas("Utas Negy", 2, foglalasi_rendszer)
    letrehoz_foglalas("Utas Ot", 3, foglalasi_rendszer)
    letrehoz_foglalas("Utas Hat", 3, foglalasi_rendszer)

    print("\nFoglalasi lista tartalma:")
    for foglalas in foglalasi_rendszer.foglalasok:
        print(foglalas)


def letrehoz_foglalas(utasnev: str, jaratszam: int, foglalasi_rendszer: FoglalasiRendszer):
    ujfoglalas = JegyFoglalas(utasnev, jaratszam)
    # TODO: reduce capacity in the jarat
    foglalasi_rendszer.foglalasok.append(ujfoglalas)
    print(ujfoglalas)


def letrehoz_belfoldijarat(legitarsasagnev: str, indulasiallomas: str, celallomas: str, indulas: str, kapacitas: int,
                           jegyar: int, foglalasi_rendszer: FoglalasiRendszer):
    uj_belfoldi_jarat = BelfoldiJarat(legitarsasagnev, indulasiallomas, celallomas, indulas, kapacitas, jegyar)
    valasztott_legitarsasag = next(
        (legitarsasag for legitarsasag in foglalasi_rendszer.legitarsasagok if legitarsasag.nev == legitarsasagnev),
        None)
    if valasztott_legitarsasag:
        uj_belfoldi_jarat.jaratszam = foglalasi_rendszer.jaratok_szama + 1
        valasztott_legitarsasag.jaratok.append(uj_belfoldi_jarat)
        foglalasi_rendszer.jaratok_szama += 1
        print(f"\nBelfoldi jarat #{uj_belfoldi_jarat.jaratszam} letrejott.")
        print(uj_belfoldi_jarat)
    else:
        print("Nincs ilyen nevu legitarsasag! Letrehozott jarat torolve!")
        del uj_belfoldi_jarat


def letrehoz_nemzetkozijarat(legitarsasagnev: str, indulasiallomas: str, celallomas: str, indulas: str, kapacitas: int,
                             jegyar: int, foglalasi_rendszer: FoglalasiRendszer):
    uj_nk_jarat = NemzetkoziJarat(legitarsasagnev, indulasiallomas, celallomas, indulas, kapacitas, jegyar)
    valasztott_legitarsasag = next(
        (legitarsasag for legitarsasag in foglalasi_rendszer.legitarsasagok if legitarsasag.nev == legitarsasagnev),
        None)
    if valasztott_legitarsasag:
        uj_nk_jarat.jaratszam = foglalasi_rendszer.jaratok_szama + 1
        valasztott_legitarsasag.jaratok.append(uj_nk_jarat)
        foglalasi_rendszer.jaratok_szama += 1
        print(f"\nNemzetkozi jarat #{uj_nk_jarat.jaratszam} letrejott.")
        print(uj_nk_jarat)
    else:
        print("Nincs ilyen nevu legitarsasag! Letrehozott jarat torolve!")
        del uj_nk_jarat
