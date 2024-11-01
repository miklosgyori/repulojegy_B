from jarat import Jarat


class JegyFoglalas:
    """
    A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

    Attributumok:
        szam (int): foglalas szama
        nev (str): utas neve
        jarat (Jarat): jarat
    """

    foglalasok_szama: int = 0

    def __init__(self, nev: str, jarat: Jarat):
        self.szam = self.__class__.foglalasok_szama + 1
        self.nev = nev
        self.jarat = jarat
        self.__class__.foglalasok_szama += 1
