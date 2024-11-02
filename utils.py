from foglalasirendszer import FoglalasiRendszer
from legitarsasag import LegiTarsasag
from belfoldijarat import BelfoldiJarat
from nemzetkozijarat import NemzetkoziJarat
from jegyfoglalas import JegyFoglalas


def inicializal():

    foglalasi_rendszer = FoglalasiRendszer()
    print(foglalasi_rendszer)

    airlinesone = LegiTarsasag("AirLinesOne")
    print(airlinesone)
    foglalasi_rendszer.legitarsasagok.append(airlinesone)

    airlinesone_1 = BelfoldiJarat("AirLinesOne", 1, "Budapest", "Debrecen", "2024-11-01 12:30:00", 100, 50000)
    print(airlinesone_1)
    # TODO: avoid storing jarat at 2 places, store only in legitarsasagok
    airlinesone.jaratok.append(airlinesone_1)
    foglalasi_rendszer.jaratok.append(airlinesone_1)

    airlinesone_2 = BelfoldiJarat("AirLinesOne", 2, "Budapest", "Miskolctapolca", "2024-11-02 11:00:00", 10, 5000)
    print(airlinesone_2)
    airlinesone.jaratok.append(airlinesone_2)
    foglalasi_rendszer.jaratok.append(airlinesone_2)

    airlinesone_3 = NemzetkoziJarat("AirLinesOne", 3, "Budapest", "Trieste", "2024-11-03 13:00:00", 150, 150000)
    print(airlinesone_3)
    airlinesone.jaratok.append(airlinesone_3)
    foglalasi_rendszer.jaratok.append(airlinesone_3)

    print(airlinesone)

    letrehoz_foglalas("Utas Egy", 1, foglalasi_rendszer)
    letrehoz_foglalas("Utas Ketto", 1, foglalasi_rendszer)
    letrehoz_foglalas("Utas Harom", 2, foglalasi_rendszer)
    letrehoz_foglalas("Utas Negy", 2, foglalasi_rendszer)
    letrehoz_foglalas("Utas Ot", 3, foglalasi_rendszer)
    letrehoz_foglalas("Utas Hat", 3, foglalasi_rendszer)

    for foglalas in foglalasi_rendszer.foglalasok:
         print(foglalas)

def letrehoz_foglalas(utasnev: str, jaratszam: int, foglalasi_rendszer: FoglalasiRendszer):
    ujfoglalas = JegyFoglalas(utasnev, jaratszam)
    # TODO: reduce capacity in the jarat
    foglalasi_rendszer.foglalasok.append(ujfoglalas)
    print(ujfoglalas)
