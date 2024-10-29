from foglalasirendszer import FoglalasiRendszer
from legitarsasag import LegiTarsasag
from belfoldijarat import BelfoldiJarat
from nemzetkozijarat import NemzetkoziJarat

if __name__ == '__main__':
    foglalasi_rendszer = FoglalasiRendszer()
    print(foglalasi_rendszer)

    airlinesone = LegiTarsasag("AirLinesOne")
    print(airlinesone)

    airlinesone_1 = BelfoldiJarat("AirLinesOne", 1, "Budapest", "Debrecen", "2024-11-01 12:30:00", 100, 50000)
    print(airlinesone_1)
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
